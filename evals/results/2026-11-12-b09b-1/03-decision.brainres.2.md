<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

Use REST. For one frontend and a small internal API, GraphQL's main payoffs (many clients with different data needs, avoiding over/under-fetching across teams) don't apply, and it adds a schema layer, resolver code, and N+1 and caching concerns you'd have to manage.

**Why REST fits here:**
- You control both ends, so you can shape endpoints to exactly what each screen needs, including a purpose-built endpoint like `GET /dashboard` when a page needs data from several resources.
- Tooling is simpler: plain HTTP caching, easy debugging with curl, and less to learn for whoever maintains it.
- If you want type safety, generate types from an OpenAPI spec (or use tRPC if both sides are TypeScript) and you get most of GraphQL's developer experience without the server complexity.

**When I'd switch to GraphQL:** the frontend has deeply nested, highly variable data needs (many screens each wanting different slices of a graph), or you expect more clients, such as mobile, soon. I'm ~80% confident that neither applies to your case as described; if either does, tell me and I'll reconsider.

Next step: sketch the 5–10 endpoints your frontend's main screens need. If that list feels clean, REST is settled.
