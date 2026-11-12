<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

**Use REST** for a small internal API with a single frontend.

**Why REST fits here:**
- **Less overhead.** No schema layer, resolvers, or GraphQL client library (Apollo/urql/Relay). You write handlers and call `fetch`.
- **GraphQL's main benefit doesn't apply.** GraphQL is most useful when many clients need different shapes of the same data. With one frontend, you control both ends and can shape each endpoint to exactly what the UI needs.
- **Easier operations.** HTTP caching, status codes, logs, rate limiting, and debugging with curl or browser devtools all work out of the box. GraphQL sends everything as `POST /graphql`, so you have to rebuild some of that.
- **Fewer pitfalls.** You avoid N+1 resolver queries, query-depth and complexity limits, and the usual "everything returns 200" error-handling confusion.

**To get most of GraphQL's type-safety benefit without the cost:**
- If you're full-stack TypeScript, look at **tRPC** or **ts-rest**. They give end-to-end types with no codegen and less ceremony than either option.
- Otherwise, use **OpenAPI** plus a generated client (e.g. `openapi-typescript`) for typed requests and responses.

**When I'd reconsider GraphQL:**
- More clients are coming soon (mobile, partners, other teams) with different data needs.
- The UI is very relational and screens pull deeply nested data from many entities, so REST would mean lots of round trips or many one-off endpoints.
- Your team already knows GraphQL well and has the tooling set up.

If none of those apply, start with REST (or tRPC). Switching later is manageable because it's internal and you own the only consumer.
