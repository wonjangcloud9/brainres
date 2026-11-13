<!-- Q: Draft a technical spec for rate limiting our public API. We use Node/Express and have Redis available. -->

# Technical Spec: Public API Rate Limiting

**Status:** Draft | **Stack:** Node.js, Express, Redis

## 1. Goals and non-goals

**Goals**
- Protect the API from abuse and accidental overload (runaway clients, scrapers, credential stuffing).
- Give fair per-client quotas with clear, machine-readable feedback.
- Add minimal latency (target p99 < 3 ms overhead per request).
- Be correct across multiple Node instances (shared state in Redis).

**Non-goals**
- DDoS mitigation (handled at the CDN/WAF/load balancer layer).
- Billing or usage metering (a separate system, though it can consume the same metrics).

## 2. Algorithm

**Recommendation: token bucket, implemented as an atomic Redis Lua script.**

| Option | Pros | Cons |
|---|---|---|
| Fixed window | Simplest | Boundary bursts (up to 2x the limit) |
| Sliding window log | Exact | O(n) memory per key |
| Sliding window counter | Cheap, smooth | Approximate |
| **Token bucket** | Allows controlled bursts, O(1) memory, simple to reason about | Slightly more complex state |

Each bucket has a `capacity` (burst size) and a `refillRate` (tokens/sec). State per key is two fields: `tokens` and `ts`.

## 3. Identification and keys

Key format: `rl:{scope}:{identity}:{route-group}`

Identity resolution, in order:
1. API key or authenticated principal ID (preferred)
2. Client IP (fallback for unauthenticated routes)

Notes:
- Set `app.set('trust proxy', N)` correctly so `req.ip` is the real client IP rather than the load balancer's. This is a common source of bugs.
- For IPv6, bucket by /64 to prevent trivial rotation.
- Hash API keys before using them in Redis keys, so raw secrets never appear in `MONITOR` or logs.

## 4. Tiers and limits (initial proposal, to be tuned)

| Tier | Identity | Limit | Burst |
|---|---|---|---|
| Anonymous | IP | 60 req/min | 20 |
| Free | API key | 300 req/min | 100 |
| Paid | API key | 3,000 req/min | 500 |
| Auth endpoints (login, reset) | IP + account | 5 req/min | 5 |

Per-route overrides are defined in config. Expensive endpoints (search, exports) can have a `cost` greater than 1 token per request.

## 5. Redis implementation

Lua script (atomic, one round trip):

```lua
-- KEYS[1] = bucket key
-- ARGV: capacity, refill_per_sec, now_ms, cost
local capacity = tonumber(ARGV[1])
local rate     = tonumber(ARGV[2])
local now      = tonumber(ARGV[3])
local cost     = tonumber(ARGV[4])

local data   = redis.call('HMGET', KEYS[1], 'tokens', 'ts')
local tokens = tonumber(data[1]) or capacity
local ts     = tonumber(data[2]) or now

tokens = math.min(capacity, tokens + ((now - ts) / 1000) * rate)

local allowed = 0
local retry_ms = 0
if tokens >= cost then
  tokens = tokens - cost
  allowed = 1
else
  retry_ms = math.ceil(((cost - tokens) / rate) * 1000)
end

redis.call('HSET', KEYS[1], 'tokens', tokens, 'ts', now)
redis.call('PEXPIRE', KEYS[1], math.ceil((capacity / rate) * 1000) * 2)
return { allowed, math.floor(tokens), retry_ms }
```

Details:
- Use the Redis server clock (`redis.call('TIME')`) instead of `now_ms` from the app if clock skew across app hosts is a concern.
- Load the script with `SCRIPT LOAD` and call it via `EVALSHA` (ioredis `defineCommand` handles this).
- TTL is about 2x the full-refill time, so idle keys expire on their own.
- **Redis Cluster:** each call touches a single key, so there are no cross-slot issues.

## 6. Express middleware

```js
function rateLimit({ tier, cost = 1, routeGroup }) {
  return async (req, res, next) => {
    const id = req.apiKeyId ?? ipKey(req);
    const cfg = limits[tier(req)];
    try {
      const [allowed, remaining, retryMs] = await redis.tokenBucket(
        `rl:${routeGroup}:${id}`, cfg.capacity, cfg.refillPerSec, Date.now(), cost
      );
      res.set({
        'RateLimit-Limit': cfg.capacity,
        'RateLimit-Remaining': remaining,
        'RateLimit-Reset': Math.ceil((cfg.capacity - remaining) / cfg.refillPerSec),
      });
      if (!allowed) {
        res.set('Retry-After', Math.ceil(retryMs / 1000));
        return res.status(429).json({
          error: 'rate_limited',
          message: 'Too many requests',
          retry_after_seconds: Math.ceil(retryMs / 1000),
        });
      }
      next();
    } catch (err) {
      metrics.increment('ratelimit.redis_error');
      return failOpen ? next() : res.status(503).end();
    }
  };
}
```

**Ordering:** mount a coarse IP limiter before authentication (cheap protection for the auth layer), then a per-key limiter after authentication.

## 7. Response contract

- **Status:** `429 Too Many Requests`
- **Headers (on all responses):** `RateLimit-Limit`, `RateLimit-Remaining`, `RateLimit-Reset` (following the IETF draft). On 429s, also `Retry-After`.
- **Body:** JSON error with a stable `error` code. Document this in the public API docs.

## 8. Failure modes

| Failure | Behavior |
|---|---|
| Redis unavailable or timeout (set a 50 ms command timeout) | **Fail open** for general routes, with an alert |
| Redis unavailable on auth/sensitive routes | **Fail closed**, or fall back to a per-instance in-memory limiter |
| Hot key | Single-key Lua ops are O(1), so it is fine. Monitor per-key rates |
| Clock skew | Use Redis `TIME` inside the script |

An in-memory fallback limiter (e.g., `rate-limiter-flexible`'s `RateLimiterMemory`) at roughly limit/instance-count gives degraded but non-zero protection during Redis outages.

## 9. Observability

- Metrics: `ratelimit.allowed`, `ratelimit.blocked` (tagged by tier and route group), `ratelimit.redis_latency`, `ratelimit.redis_error`.
- Logs: structured log on block, with hashed key ID, route, and tier. Sample these to avoid log floods.
- Alerts: block-rate spike, Redis error rate above 1%, Redis latency p99 above 10 ms.
- Dashboard: top blocked identities (useful for spotting abuse and for customer-support conversations).

## 10. Security considerations

- Don't trust `X-Forwarded-For` unless `trust proxy` is configured to match the real hop count.
- Rate-limit by account as well as IP on auth endpoints, to stop distributed credential stuffing.
- Never include raw API keys in Redis keys or logs.
- Keep 429 responses cheap, with no DB lookups on the rejection path.

## 11. Testing

- **Unit:** the Lua script against a real Redis (testcontainers) covering refill math, burst, cost > 1, and TTL expiry.
- **Concurrency:** fire N parallel requests and assert that exactly `capacity` succeed.
- **Integration:** header correctness and the 429 contract through Express with supertest.
- **Failure injection:** kill Redis mid-test and verify fail-open and fail-closed behavior.
- **Load test:** (k6 or autocannon) confirm the latency overhead target.

## 12. Rollout plan

1. **Shadow mode:** compute and log decisions and headers but never block. Run for about a week.
2. Review blocked-would-have-been data, then tune limits.
3. **Enforce** for anonymous and free tiers, then paid tiers (with customer comms beforehand).
4. Add a per-customer override mechanism (Redis hash or config) for approved exceptions.
5. Publish limits and 429 handling guidance in the API docs.

## 13. Open questions

1. What are the real current traffic percentiles per client? Limits above are placeholders.
2. Do we need org-level (shared across multiple keys) quotas in addition to per-key?
3. Is Redis shared with other workloads (sessions, cache)? If so, consider a dedicated instance or logical separation to avoid eviction of limiter keys (use `noeviction` or a volatile-TTL policy).
4. Should we also add a concurrency limit (max in-flight requests) for expensive endpoints?
5. Are there webhooks or internal service callers that should be exempt via allowlist?

---

I can save this as `docs/rate-limiting-spec.md` if you'd like, or tailor it further. If you point me at the codebase, I can adapt the middleware to your existing auth and routing structure.
