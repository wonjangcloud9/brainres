<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

Use REST. With one frontend and one team, GraphQL's main benefits (clients choosing fields, many clients with different data needs) don't apply, and it adds a schema layer, resolvers, and N+1 query handling.

GraphQL would be worth it in three cases:
- Screens routinely need data from many resources, and you're making many round trips or writing many one-off endpoints.
- You expect more clients (mobile, partners) with different data shapes.
- Your team already knows GraphQL well, so the overhead is low.

If you want typed contracts without GraphQL, generate an OpenAPI spec from the server and a typed client from the spec (e.g. `openapi-typescript`). Alternatively, use tRPC if both sides are TypeScript. Either gives you most of the type safety with far less setup.

Next step: list the frontend's screens and the endpoints each one needs. If most screens need one or two calls, go with REST.
