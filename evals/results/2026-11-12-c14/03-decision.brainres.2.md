<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

Use REST. For one frontend and a small internal API, GraphQL's main benefits (flexible queries across many clients, avoiding over/under-fetching, a typed schema shared between teams) mostly don't apply, and it adds a schema layer, resolver code, and caching and N+1 problems you'd have to manage.

**When GraphQL would be worth it:**
- The frontend screens need data from many related resources, and you'd otherwise make 4+ REST calls per page.
- You expect more clients (mobile, partners) with different data needs soon.
- The data is a deeply nested graph, such as users → orders → items → reviews.

**Cheap ways to get GraphQL's upsides with REST:**
- Write endpoints shaped for screens (e.g. `GET /dashboard`) instead of strictly per-resource ones. You control both sides, so this is fine.
- Generate types from an OpenAPI spec (FastAPI, NestJS, or `tsoa` produce one automatically) to get end-to-end type safety.
- Add `?include=` or `?fields=` only if a specific over-fetching problem shows up.

I'm assuming the team is small and there's no existing GraphQL experience. If someone already knows GraphQL well, the setup cost shrinks and the choice is closer.

Next step: pick your backend framework and I can show how to get an OpenAPI spec and a typed frontend client generated from it.
