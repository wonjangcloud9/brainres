<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

For a small internal API used by one frontend, **use REST** unless you already know you need something GraphQL specifically solves.

**Why REST is the better default here:**
- **Less setup.** No schema, resolvers, or codegen pipeline to maintain.
- **Simpler caching and debugging.** Plain HTTP verbs and URLs work with browser devtools, curl, and standard HTTP caching.
- **Your over-fetching and under-fetching problems are small.** GraphQL pays off when many clients need different shapes of the same data. With one frontend you can shape endpoints around its screens.
- **Easier to hand off.** Most developers can read a REST API immediately.

**Choose GraphQL instead if:**
- The frontend has many views with deeply nested, varying data needs, and you're making lots of round trips.
- You want the frontend team to iterate on queries without backend changes.
- You plan to add more clients (mobile, partners) soon.
- You're already using a GraphQL stack (e.g., Apollo, Relay) and the tooling is paying off.

**A practical middle ground:** Start with REST and keep endpoints shaped around the frontend's actual screens. If you later find yourself adding many one-off endpoints or fighting over-fetching, migrating to GraphQL is a reasonable step at that point.

If you tell me the rough shape of the data and the frontend's main screens, I can give a more specific recommendation.
