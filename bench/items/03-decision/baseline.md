<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

**Use REST.** For one internal frontend with a small API, it's the lower-overhead choice.

**Why REST fits here:**
- You control both sides, so you can shape endpoints to exactly what the UI needs (including purpose-built "view" endpoints that return what a screen needs in one call).
- No extra schema, resolver, or client-library layer to build and maintain.
- Caching, logging, debugging, and auth all work with standard HTTP tooling.
- Less to learn and less to go wrong for a small team.

**When GraphQL would be worth it:**
- Many screens with very different data shapes, causing lots of over-fetching or round trips.
- Deeply nested, relational data the UI traverses in varied ways.
- You expect more clients (mobile, third parties) soon, each wanting different fields.
- Your team already knows GraphQL well and has the tooling set up.

**Tips to get GraphQL-like benefits with REST:**
- Add optional `?fields=` or `?include=` params only if you actually hit over-fetching.
- Define the API with OpenAPI and generate typed client code for the frontend.
- Make a few aggregate endpoints for screens that would otherwise need several calls.

If you later outgrow REST, you can put GraphQL in front of the same services without a rewrite.
