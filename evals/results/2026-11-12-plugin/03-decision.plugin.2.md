<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

Use REST. For one frontend that your team owns, GraphQL's main benefits (many clients, flexible queries, public schema) don't apply, and it adds a schema layer, a resolver setup, and caching and N+1 problems that you'd have to manage.

The strongest case for GraphQL is that your frontend needs deeply nested, varied data and you're tired of adding or reshaping endpoints. If that's already hurting, GraphQL fits. If you're only guessing it might, wait. Moving to GraphQL later is easy because you can put it in front of the same data layer.

To keep REST pleasant:

1. Shape endpoints around screens, not tables. A `/dashboard` endpoint that returns exactly what the page needs avoids most over-fetching.
2. Generate types from an OpenAPI spec (for example with `openapi-typescript`) so the frontend gets the type safety people often want from GraphQL.
3. Add simple query params like `?include=owner` only when a screen needs them.

Next step: list the five or six screens your frontend has, and write one endpoint per screen. If that feels clumsy, revisit GraphQL then.
