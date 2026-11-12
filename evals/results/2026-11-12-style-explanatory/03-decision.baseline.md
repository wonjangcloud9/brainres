<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

**Recommendation: REST.** For one internal frontend and a small API, it's the lower-overhead choice.

`★ Insight ─────────────────────────────────────`
GraphQL's main wins (flexible queries across many clients, avoiding over/under-fetching, a typed schema shared between teams) mostly matter when you have multiple consumers with different data needs. With one frontend you control both sides, so you can just shape endpoints to what the UI needs.
`─────────────────────────────────────────────────`

**Why REST fits here**
- **Less setup:** no schema layer, resolvers, or client library required. Plain `fetch` and a few routes work.
- **Simpler operations:** standard HTTP caching, logging, and error codes. GraphQL's single `/graphql` endpoint makes these harder (everything is a `POST` returning `200`).
- **No N+1 pitfalls:** GraphQL resolvers can easily produce N+1 database queries unless you add something like DataLoader.
- **Security surface:** GraphQL needs query depth/complexity limits; REST doesn't.
- **Over-fetching is a non-issue:** since you own the frontend, add a field or a purpose-built endpoint (e.g. `/dashboard-summary`) when needed.

**When GraphQL would be worth it**
- The UI has deeply nested, highly variable data needs (many screens each wanting different slices of a graph).
- You expect more clients soon (mobile app, other teams).
- You want generated types and a strongly typed contract, and you're willing to pay the tooling cost.

**Middle path:** if what you really want is end-to-end type safety, you can get it with REST by using an OpenAPI spec with generated clients, or a typed RPC layer like tRPC if both ends are TypeScript.

`★ Insight ─────────────────────────────────────`
The choice is also reversible. A small REST API can later sit behind or alongside a GraphQL gateway if requirements grow, so starting simple doesn't lock you in.
`─────────────────────────────────────────────────`

If you tell me your stack (backend language, frontend framework), I can suggest a concrete setup.
