<!-- Q: Postgres or MongoDB for a small SaaS app? -->

**Postgres.** For a small SaaS app, it's the safer default.

**Why:**
- **Relational data fits SaaS.** Users, orgs, subscriptions, invoices, and permissions are all related entities. Joins, foreign keys, and transactions keep that data consistent without extra application code.
- **It covers the flexible-schema case too.** `jsonb` columns with indexing handle semi-structured data, so you rarely need a document DB just for that.
- **Fewer moving parts.** Full-text search, queues (e.g. `SKIP LOCKED`), and row-level security for multi-tenancy are built in or available as extensions. That means fewer services to run early on.
- **Easy hosting.** Supabase, Neon, RDS, and Render all offer managed Postgres with good free or cheap tiers.
- **Hard to outgrow.** A single Postgres instance handles far more load than a small app will see.

**When MongoDB makes sense:**
- Your data is truly document-shaped with little cross-referencing (e.g. CMS content, event logs).
- Schemas change constantly and you don't want migrations.
- Your team already knows it well.

The usual regret runs one way: teams start on Mongo, then add relationships (billing, teams, reporting) and end up reimplementing joins and transactions in app code. Migrating from Postgres to Mongo is rarely needed.

If you tell me what the app does and what stack you're using, I can give more specific advice (schema design, ORM choice, multi-tenancy approach).
