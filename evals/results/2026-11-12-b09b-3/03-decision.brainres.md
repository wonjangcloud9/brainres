<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

Use REST. For one frontend, one team, and a small internal API, GraphQL's main benefits (clients picking their own fields, many clients with different data needs, avoiding versioned endpoints) mostly don't apply, and you'd pay for a schema layer, resolvers, and N+1 handling (usually via dataloaders) that REST doesn't need.

GraphQL starts to win when one of these is true:

- **Many round trips:** screens need data from 4+ related resources and you can't cheaply add a purpose-built endpoint.
- **Multiple clients:** mobile, web, and partners need different shapes of the same data.
- **Fast-changing UI:** the frontend changes shape weekly and backend changes are the bottleneck.

With one frontend you control, you can fix the first and third by adding an endpoint that returns exactly what a screen needs (e.g. `GET /dashboard`). That is cheaper than adopting GraphQL.

If you want type safety between frontend and backend without GraphQL, generate types from an OpenAPI spec, or use tRPC if both sides are TypeScript. I'm ~80% sure that covers what most small teams want from GraphQL.

Next step: tell me your backend language and frontend framework, and I can suggest a concrete REST setup, including the typing approach.
