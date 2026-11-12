<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

Use REST. With one frontend you control both sides, so GraphQL's main benefit (each client asks for exactly the fields it needs) is something you can get by shaping endpoints to the screens.

GraphQL also adds costs that a small team feels directly:

- **Server setup:** a schema, resolvers, and usually a DataLoader to avoid N+1 queries.
- **Caching:** everything is a `POST /graphql`, so you lose simple HTTP caching and per-endpoint logs.
- **Abuse limits:** you need query depth and cost limits, even on an internal API.
- **Tooling:** a client library (Apollo, urql) and codegen on the frontend.

`★ Insight ─────────────────────────────────────`
GraphQL solves a coordination problem: many clients with different data needs and teams that can't change the backend quickly. With one frontend and one team, that problem doesn't exist, so you pay for the solution without the benefit.
`─────────────────────────────────────────────────`

GraphQL starts to win if one of these is true:

1. Screens need deeply nested, varied slices of the same data, and you keep adding one-off endpoints.
2. A second client (mobile app, partner integration) is coming soon.
3. The frontend team iterates much faster than the backend team and is blocked on endpoint changes.

If you want typed contracts without GraphQL, generate an OpenAPI spec and a typed client from it (for example `openapi-typescript`), or use tRPC if both ends are TypeScript. Both give you end-to-end types with far less machinery.

What's your backend and frontend stack? With that I can suggest the lightest setup for typed REST.
