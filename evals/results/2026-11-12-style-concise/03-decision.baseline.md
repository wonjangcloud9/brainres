<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

Use REST. For one frontend and a small internal API, GraphQL's main benefits (flexible queries across many clients, avoiding over/under-fetching) don't pay for the added schema, resolver, and tooling overhead.

Pick GraphQL only if your data is deeply relational and the frontend needs varied nested shapes per screen, or if you expect more clients soon. If the REST endpoints start multiplying into one-per-screen, that's the signal to reconsider.
