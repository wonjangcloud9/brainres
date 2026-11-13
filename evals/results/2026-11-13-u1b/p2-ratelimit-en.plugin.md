<!-- Q: Draft a technical spec for rate limiting our public API. We use Node/Express and have Redis available. -->

**Recommendation: use a token-bucket limiter in Express middleware, with its state in Redis and updated by one atomic Lua script, keyed by API key (IP only for unauthenticated routes).** The draft spec follows. I haven't checked it against your codebase, so tiers, limits and route names are placeholders.

---

# Spec: Public API Rate Limiting

## 1. Goals and non-goals

**Goals**
- Protect the API and backing services from abuse and runaway clients.
- Give fair, predictable quotas per customer tier.
- Add under 2 ms p99 overhead per request (target; verify with a load test).

**Non-goals**
- DDoS defense. That belongs at the CDN/WAF layer.
- Billing-grade metering. Counts here are approximate by design.

## 2. Algorithm

| Option | Burst handling | Redis cost | Verdict |
|---|---|---|---|
| Fixed window | Allows 2× burst at window edges | 1 `INCR` | Too lossy |
| Sliding window log | Exact | O(n) memory per key | Too costly at scale |
| Sliding window counter | Close to exact | 2 keys | Acceptable |
| **Token bucket** | Explicit burst, steady refill | 1 hash, 1 script call | **Chosen** |

Token bucket gives each client a burst allowance (`capacity`) and a sustained rate (`refillPerSec`). Both are easy to explain in docs.

## 3. Identity and limits

1. **Key:** `rl:{<tier>}:<apiKeyId>:<routeClass>`. Unauthenticated requests use `rl:anon:<ip>`.
2. **Route classes:** `read` (cost 1), `write` (cost 5), `expensive` (cost 20, e.g. search/export).
3. **Tiers** (placeholder values):

| Tier | Refill/sec | Capacity |
|---|---|---|
| anon | 1 | 20 |
| free | 5 | 100 |
| pro | 50 | 1000 |
| enterprise | custom | custom |

4. **Config:** a tier table in code, with per-key overrides in your existing key store. The middleware reads the tier from the authenticated request, so it must run **after** auth.

## 4. Redis design

- One hash per key with fields `tokens` and `ts`.
- The Lua script reads time from Redis (`TIME`), not the app server, so clock skew between Node instances doesn't matter.
- The script refills, checks, decrements and sets the TTL in one atomic call.
- TTL is about 2× the time to refill a full bucket, so idle keys expire.
- On Redis Cluster, each key is self-contained, so there are no cross-slot problems.

```lua
-- KEYS[1]=key  ARGV: refillPerSec, capacity, cost
local t = redis.call('TIME')
local now = t[1] * 1000 + math.floor(t[2] / 1000)
local d = redis.call('HMGET', KEYS[1], 'tokens', 'ts')
local cap, rate, cost = tonumber(ARGV[2]), tonumber(ARGV[1]), tonumber(ARGV[3])
local tokens = tonumber(d[1]) or cap
local ts = tonumber(d[2]) or now
tokens = math.min(cap, tokens + (now - ts) / 1000 * rate)
local allowed, retry = 0, 0
if tokens >= cost then tokens = tokens - cost; allowed = 1
else retry = math.ceil((cost - tokens) / rate) end
redis.call('HSET', KEYS[1], 'tokens', tokens, 'ts', now)
redis.call('PEXPIRE', KEYS[1], math.ceil(cap / rate * 2000))
return { allowed, math.floor(tokens), retry }
```

## 5. Express middleware

```js
import Redis from 'ioredis';
const redis = new Redis(process.env.REDIS_URL, { commandTimeout: 50 });
redis.defineCommand('takeTokens', { numberOfKeys: 1, lua: LUA_SOURCE });

export function rateLimit(routeClass = 'read') {
  return async (req, res, next) => {
    const { id, tier } = req.apiKey ?? { id: req.ip, tier: 'anon' };
    const { rate, cap } = TIERS[tier];
    const cost = COSTS[routeClass];
    try {
      const [ok, remaining, retry] = await redis.takeTokens(
        `rl:{${tier}}:${id}:${routeClass}`, rate, cap, cost);
      res.set({
        'RateLimit-Limit': cap,
        'RateLimit-Remaining': remaining,
        'RateLimit-Reset': Math.ceil(cap / rate),
      });
      if (!ok) {
        res.set('Retry-After', retry);
        return res.status(429).json({
          error: 'rate_limited',
          message: 'Too many requests.',
          retry_after_seconds: retry,
        });
      }
    } catch (err) {
      metrics.increment('ratelimit.redis_error');
      // fail open, see §6
    }
    next();
  };
}
```

Set `app.set('trust proxy', <hops>)` to match your load balancer. Without it, `req.ip` is the proxy's address and all anonymous users share one bucket.

## 6. Failure behavior

- **Redis down or slow (>50 ms):** fail **open** and alert. A limiter outage shouldn't take down the API.
- **Exception:** for `expensive` routes, fall back to a per-process in-memory limiter (e.g. `rate-limiter-flexible`'s `RateLimiterMemory`) at roughly quota ÷ instance count.
- Revisit fail-open if abuse during a Redis outage is a real threat for you.

## 7. Client contract

- Status `429` with a JSON body, plus `Retry-After` (seconds).
- `RateLimit-Limit`, `RateLimit-Remaining`, `RateLimit-Reset` on **every** response, not just 429s. These follow the IETF draft names. The draft is still evolving, so pin the names in your API docs.
- Document the cost per route class and recommend exponential backoff with jitter.

## 8. Observability

- Metrics: allowed/denied count by tier and route class, Redis latency, Redis error count.
- Log denials with key ID (never the raw key).
- Alerts: denial rate above 20% for one key for 10 minutes (possible broken client); any Redis error spike.

## 9. Testing and rollout

1. Unit-test the Lua script: refill math, burst, exact-capacity edge, TTL.
2. Load-test with k6 or autocannon against a staging Redis to confirm the latency target.
3. Ship in **shadow mode** first: compute and log decisions, never return 429.
4. Review denial logs for a week, adjust tiers, then enforce for `anon`, then `free`, then the rest.
5. Add a kill switch (env flag) that disables enforcement without a deploy.

## 10. Open questions

- Real tier names and numbers: do you have current traffic data to size them?
- Do you need per-endpoint overrides beyond the three route classes?
- Is there an existing gateway (nginx, Cloudflare, Kong) that should own the anonymous/IP layer instead?
- Should enterprise customers get a self-service way to view usage?

---

**Next step:** answer the open questions, especially tier numbers and whether a gateway already exists. Then I can save this as `docs/rate-limiting-spec.md` and write the middleware and Lua tests against your actual route layout.
