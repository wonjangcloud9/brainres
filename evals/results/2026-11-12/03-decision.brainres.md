<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

Use REST. For one frontend, one team, and a small internal API, GraphQL's main benefits (flexible queries across many clients, avoiding over-fetching for varied consumers) don't apply, while its costs do: a schema layer, resolver plumbing, N+1 query handling, and harder caching and error handling.

The strongest case for GraphQL here is that the frontend has deeply nested, highly relational screens where REST would need many round trips or a pile of custom endpoints. If most of your screens need 3+ related resources at once, that's worth a look. I'm ~80% sure that isn't your situation, since "small" usually means flat CRUD-style data.

Quick check: list your five most complex screens and count the requests each would need under REST. If it's mostly 1-2, REST wins clearly. If several need 4+ and you can't fix that with a few purpose-built endpoints (e.g. `GET /orders/:id?include=items,customer`), reconsider.

If you go REST, generate an OpenAPI spec and a typed client from it, so you get the frontend type-safety people often pick GraphQL for.

Next action: sketch your endpoint list and the heaviest screen's data needs, and if you share them I'll tell you whether anything justifies GraphQL.
