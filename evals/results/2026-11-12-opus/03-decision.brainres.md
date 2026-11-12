<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

**Use REST.** With one frontend and a small surface, GraphQL's main benefit doesn't apply, and you'd still pay its setup and operating costs.

GraphQL is built for many clients with different data needs: mobile, web, and partners each fetching different shapes from one schema. You have one client, so you can shape each REST endpoint to match what that frontend needs. GraphQL also adds work REST gets for free:

- **Schema and resolvers:** you write and maintain them alongside your data layer.
- **HTTP caching:** most GraphQL traffic is POST to one URL, so CDN and browser caching need extra tooling.
- **N+1 queries:** nested resolvers need DataLoader or similar batching.
- **Debugging:** every request hits `/graphql`, so logs and network tabs are harder to read.

| | REST | GraphQL |
|---|---|---|
| Setup for a small API | Minimal | Schema, server, client library |
| Fits one known client | Yes, endpoints match its views | Flexibility goes unused |
| HTTP caching | Built in | Needs extra work |
| Typed contract | Via OpenAPI | Built in |

The strongest case for GraphQL here is a frontend with deeply nested, view-specific data that changes often. In that case, GraphQL saves you from adding endpoints or over-fetching. If that describes your app, GraphQL is defensible.

If the frontend and backend are both TypeScript, consider **tRPC**. It gives you end-to-end types with no schema or codegen, and that is often the real thing people want from GraphQL.

Next step: list the frontend's main screens and the data each one needs. If each maps to one or two simple endpoints, go with REST (or tRPC if you're all-TypeScript).
