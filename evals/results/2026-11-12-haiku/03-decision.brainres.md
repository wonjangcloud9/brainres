<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

**Use REST.** With one frontend and one team, GraphQL's main benefit, letting many clients request different data shapes, has little value. You would pay for its costs (schema definition, resolvers, caching that is harder than plain HTTP, and more setup) without getting much back.

REST fits because:

- You can call endpoints with `fetch` and inspect them in the browser or with `curl`.
- HTTP caching and status codes work without extra tooling.
- Your frontend and API change together, so a fixed response shape is easy to maintain.

Choose GraphQL only if the frontend needs deeply nested data and you find yourself making many round trips to assemble one screen, or if you expect several clients with different data needs soon.

If the screens need a few combined resources, add a dedicated endpoint, such as `GET /api/dashboard`, instead of switching to GraphQL. For example, if the page shows a user and their last five orders, one `GET /api/users/:id?include=recent_orders` call usually covers it.
