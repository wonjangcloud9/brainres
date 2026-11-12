<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

Use REST. For one frontend that you also control, GraphQL's main benefit (letting many different clients ask for different shapes of data) doesn't apply, and it adds a schema, resolvers, and a client library you'd have to maintain.

The strongest case against REST is over-fetching and many round trips. If your screens need data from five or six related resources at once, REST can get chatty. But you can fix that cheaply by adding one endpoint per screen, such as `GET /dashboard`, that returns exactly what the page needs. Since you own both sides, that's easy to change.

Pick GraphQL instead only if one of these is true:

- **The data is a deeply connected graph.** Screens regularly walk several relationships, and per-screen endpoints would multiply.
- **The frontend changes shape often.** You want to change queries without touching the backend each time.
- **Other clients are coming soon.** A mobile app or third-party consumers would each want different fields.
- **Your team already knows it.** Then the setup cost is mostly paid.

If none of these fits, REST with a typed client (OpenAPI-generated types, or tRPC if both sides are TypeScript) gives you most of the safety people want from GraphQL at a fraction of the setup.

Next step: list your frontend's three or four most data-heavy screens and count how many REST calls each needs. If any needs more than three or four, add a dedicated endpoint for it. If most do, reconsider GraphQL.
