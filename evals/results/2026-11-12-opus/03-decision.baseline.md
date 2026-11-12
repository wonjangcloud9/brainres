<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

**Use REST** (or plain JSON-over-HTTP), unless one of the exceptions below applies.

**Why REST fits this case:**
- **One consumer means GraphQL's main benefit goes away.** GraphQL is most useful when many clients need different shapes of the same data. With one frontend you control both sides and can make each endpoint return exactly what the UI needs.
- **Less machinery.** You avoid writing a schema and resolvers, handling N+1 queries (DataLoader), limiting query depth and cost, and adding a client library like Apollo or urql.
- **Simpler operations.** HTTP caching, status codes, logging, and debugging with curl or browser devtools all work as usual. GraphQL sends everything as `POST /graphql` with a 200 response, which makes monitoring and error handling less clear.
- **Easy to onboard.** Anyone on the team can read and change it.

**When GraphQL would make sense instead:**
- Your data is deeply nested or graph-shaped, and the UI keeps needing new combinations, so you'd otherwise be adding endpoints constantly or making many round trips.
- You expect more clients (mobile, other teams) soon.
- Your team already knows GraphQL well and has tooling set up, so the overhead is close to zero.

**A middle option:** if your frontend and backend are both TypeScript, look at **tRPC** (or REST with an OpenAPI spec and generated types). You get end-to-end type safety, which is often the real thing people want from GraphQL, with much less setup.

If you tell me your stack and roughly what the data looks like, I can give a more specific recommendation.
