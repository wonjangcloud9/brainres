<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

**Use REST.** For a small internal API with a single frontend, it's the simpler choice and you give up very little.

**Why REST fits here**
- **Less machinery:** no schema layer, resolvers, or client library required. A framework's built-in routing plus `fetch` is enough.
- **Easy to debug and cache:** plain HTTP, curl-able, works with standard tooling and browser/HTTP caching.
- **Avoids GraphQL-specific pitfalls:** N+1 queries, query-complexity limits, and per-field authorization are real work you'd take on for little benefit.
- **You control both sides:** the main problems GraphQL solves (many different clients needing different data shapes, over/under-fetching across teams) mostly don't exist when one frontend consumes one backend.

**When GraphQL would be worth it**
- The frontend has screens that need deeply nested data from many resources, and you're making lots of round trips or creating many bespoke endpoints.
- You expect more clients (mobile, partners) with differing data needs soon.
- The data model is a genuine graph and the team already knows GraphQL well.

**Practical tips to get most of GraphQL's benefits with REST**
- Add purpose-built endpoints for screens that need aggregated data (e.g., `GET /dashboard`), rather than forcing strict resource purity.
- Support simple `?fields=` or `?include=` params only if you actually need them.
- Generate types from an OpenAPI spec (or share types if both sides are TypeScript) to get the type-safety benefit people like in GraphQL.

If the frontend later outgrows REST, you can put GraphQL in front of the same services incrementally, so choosing REST now isn't a dead end.
