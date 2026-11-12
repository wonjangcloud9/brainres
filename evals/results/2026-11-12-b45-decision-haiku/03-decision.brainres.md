<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

**Use REST.** With one frontend that you control, GraphQL's main benefit, letting many clients shape their own queries, doesn't apply, and it adds schema, resolver, and tooling overhead.

REST fits better here because:

- **Less setup:** Endpoints, HTTP caching, and standard tools like `curl` and browser devtools work without extra libraries.
- **Simpler errors and auth:** Status codes and middleware handle most cases directly.
- **Shared types are still possible:** If both sides are TypeScript, a shared type package or a tool like tRPC or OpenAPI codegen gives you end-to-end type safety without GraphQL.

Consider GraphQL only if the frontend needs many differently shaped views of deeply nested data, or if you expect several clients soon. Switching later is possible but costly, so decide based on what you know now.

What stack is the frontend and API in? I can suggest a concrete setup.
