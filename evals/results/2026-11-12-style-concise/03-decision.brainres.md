<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

Use REST. With one frontend and a small team, you control both sides, so GraphQL's main benefit (letting many different clients shape their own queries) buys you little, while its costs are real: a schema and resolver layer, N+1 query handling, harder caching, and more tooling to maintain.

GraphQL becomes worth it if the frontend makes many chained requests per screen, if you add more clients (mobile, partners) with different data needs, or if your data is a deeply nested graph. If you only hit the over-fetching problem on one or two screens, add a purpose-built endpoint for those rather than switching.

To keep REST pleasant, generate an OpenAPI spec from your backend and produce typed client code for the frontend, which gives you most of GraphQL's type safety.

If you tell me your stack, I can suggest the spec and codegen setup.
