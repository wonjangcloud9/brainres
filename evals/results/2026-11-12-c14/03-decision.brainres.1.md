<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

Use REST. For one frontend and a small internal API, GraphQL's main benefits (flexible queries across many clients, avoiding over-fetching for varied consumers) don't pay for their cost.

**Why REST fits here:**
- You control both sides, so you can shape endpoints to exactly what the frontend needs, including one-off "view" endpoints that return a screen's worth of data.
- It needs less setup: no schema layer, resolvers, or N+1 handling (DataLoader), and caching, logging, and debugging work with ordinary HTTP tools.
- Fewer moving parts is easier to maintain for a small team.

**When GraphQL would be the better choice:**
- The frontend has many screens that each need different slices of deeply nested data, and you're adding endpoints constantly.
- You expect more clients (mobile app, partners) with different data needs.
- You want a typed schema as the contract and your team already knows the tooling.

If you want type safety without GraphQL, generate an OpenAPI spec from your backend and produce a typed client for the frontend (e.g., with `openapi-typescript`), or use tRPC if both sides are TypeScript. These give most of the contract benefit at lower cost.

Next step: sketch the 5–10 screens your frontend needs. If most map cleanly to one or two endpoints each, start with REST.
