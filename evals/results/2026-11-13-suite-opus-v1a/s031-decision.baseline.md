<!-- Q: Postgres or MongoDB for a small SaaS app? -->

**Postgres.** For a typical small SaaS app it's the safer default.

**Why Postgres fits SaaS well**
- **Relational data is the norm.** Users, organizations, memberships, subscriptions, invoices, and permissions are all naturally relational. Joins and foreign keys keep that data consistent without application-side bookkeeping.
- **Transactions and constraints.** Billing, plan changes, and seat counts need atomic updates and enforced uniqueness. Postgres does this out of the box. MongoDB has multi-document transactions now, but they're less idiomatic.
- **You still get document flexibility.** `jsonb` columns, with GIN indexes, let you store schemaless blobs like settings, integration payloads, or event metadata.
- **Multi-tenancy tooling.** Row-level security, schemas-per-tenant, and the `tenant_id` + composite index patterns are well documented.
- **Ecosystem.** Prisma, Drizzle, SQLAlchemy, Rails, and Django all treat Postgres as first-class. Managed options are cheap and plentiful: Neon, Supabase, RDS, Railway, Render. Extensions like `pgvector` (embeddings), `pg_cron`, and full-text search can save you from adding extra services early on.
- **Reporting.** Ad-hoc SQL for "how many orgs on the Pro plan churned last month" is trivial. In Mongo, the aggregation pipeline is clunkier.

**When MongoDB is a reasonable pick**
- Your core data really is document-shaped and rarely joined, such as a CMS, form builder, or event or log store.
- Each document's shape varies a lot and you'd mostly be using `jsonb` anyway.
- Your team already knows Mongo well and doesn't know SQL. Familiarity matters a lot at small scale.

**Practical note:** At small-SaaS scale, either will perform fine. The real cost of picking wrong is data-integrity bugs and awkward queries later, not speed. That risk is lower with Postgres.

If you tell me what the app does and what stack you're using, I can sketch a starter schema.
