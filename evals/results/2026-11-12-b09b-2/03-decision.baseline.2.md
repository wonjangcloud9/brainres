<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

**Use REST.** For a small internal API with a single frontend, it's the simpler choice.

**Why REST fits:**
- You control both sides, so you can shape endpoints to exactly what the frontend needs (including purpose-built endpoints that return composed data).
- Less setup: no schema layer, resolvers, or N+1/dataloader concerns, and standard HTTP caching and tooling just work.
- Easier to debug and monitor (curl, browser dev tools, logs per route).
- Fewer moving parts for a small team to maintain.

**When GraphQL would be worth it instead:**
- The frontend has many views that each need different slices of deeply nested data, and you're constantly adding or tweaking endpoints.
- You expect more clients (mobile, third parties) with divergent data needs.
- You want a strongly typed schema as the contract and are happy to invest in the tooling.

**Practical tips if you go REST:**
- Generate an OpenAPI spec (e.g., FastAPI, or tsoa/zod-openapi in TypeScript) and produce a typed client for the frontend. This gets you most of GraphQL's type-safety benefit.
- Allow optional `?include=` or `?fields=` params only if you actually hit over-fetching.
- If you're on TypeScript end to end, tRPC is also worth a look as an even lighter option.

If you tell me the stack and how many distinct screens/data shapes you have, I can give a firmer recommendation.
