<!-- Q: Postgres or MongoDB for a small SaaS app? -->

**Use Postgres.** Most SaaS data is relational: users belong to organizations, organizations have subscriptions, and subscriptions have invoices. Postgres models that directly and enforces it with foreign keys and transactions. It also covers the main reason people pick MongoDB, because `jsonb` columns store flexible, schemaless data and can be indexed.

| Concern | Postgres | MongoDB |
|---|---|---|
| Multi-tenant data (orgs → users → billing) | Joins and foreign keys built in | Manual references or denormalization |
| Flexible fields | `jsonb` with GIN indexes | Native |
| Transactions | Default, mature | Supported since 4.0, less idiomatic |
| Reporting and analytics | Full SQL, window functions | Aggregation pipeline |
| Managed hosting | Supabase, Neon, RDS, Render | Atlas |
| Ecosystem (ORMs, auth, Stripe sync) | Larger | Smaller |

**The strongest case for MongoDB:** your core data is document-shaped and rarely joined. Examples are CMS content, event logs, or user-defined form schemas. Your team might also already know Mongo well. Even then, a `jsonb` column in Postgres usually covers those cases without a second database.

**A cost to watch with Postgres:** schema changes need migrations. Use a migration tool from day one, such as Prisma, Drizzle, Alembic, or Rails migrations.

Next step: pick a managed Postgres host. Supabase or Neon are cheap starting points with free tiers. Define your `organizations`, `users`, and `memberships` tables first, because tenant isolation is the hardest part to retrofit.
