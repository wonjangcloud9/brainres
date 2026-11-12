<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

**Use REST.** With one internal frontend, GraphQL's main strengths solve problems you don't have.

GraphQL pays off when many clients need different shapes of the same data, or when a frontend team moves faster than the backend team. Here you control both sides, so you can shape each REST endpoint to what the frontend needs. GraphQL also adds a schema layer, resolver code, N+1 query handling (usually via DataLoader), and harder HTTP caching. REST works with plain HTTP caching, standard tooling, and simple logs.

| Factor | REST | GraphQL |
|---|---|---|
| Setup cost | Low | Schema, resolvers, client library |
| Fits one known client | Yes | Overkill |
| HTTP caching | Built in | Needs extra work |
| Many clients with varied needs | Endpoint sprawl | Strong fit |

If both the frontend and backend use TypeScript, consider tRPC instead. It gives end-to-end types with no schema or codegen step. For other stacks, REST plus an OpenAPI spec gets you generated types.

Revisit GraphQL if a second or third client, such as a mobile app, starts needing different data from the same endpoints.

Next step: write the first few endpoints around your frontend's screens. Tell me your backend language and I'll sketch the structure.
