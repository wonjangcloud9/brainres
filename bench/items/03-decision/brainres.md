<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

Use REST. For one frontend and one team, GraphQL's main benefits (many clients with different data needs, avoiding over-fetching across a public surface) don't apply, while its costs do: a schema layer, resolvers, N+1 handling, query-complexity limits, and a heavier client setup.

**Strongest case for GraphQL:** if the frontend has deeply nested, highly variable views (say, dashboards that join 5+ entities differently per screen), you'll otherwise write many bespoke endpoints or make many round trips. If that describes your app, GraphQL starts to pay off. Roughly 80% of small internal tools don't look like that.

**How to keep REST pleasant:**
1. Shape endpoints around screens when needed, e.g. `GET /dashboard` returning exactly what that page uses. Internal APIs don't need purity.
2. Add an `?include=` or `?fields=` param only if over-fetching actually shows up.
3. Generate types from an OpenAPI spec (or use tRPC if frontend and backend are both TypeScript) to get the type safety people often want from GraphQL.

**Next action:** list your frontend's 3-5 most complex screens and count the distinct entities each needs. If most need 1-2 endpoints, go REST; if several need 4+ with varying shapes, prototype one in GraphQL before committing.
