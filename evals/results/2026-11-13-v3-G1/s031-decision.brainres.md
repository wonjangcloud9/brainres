<!-- Q: Postgres or MongoDB for a small SaaS app? -->

**Postgres.** For a small SaaS app it's the safer default.

**Why:**
- SaaS data is usually relational: users, orgs, subscriptions, invoices. Foreign keys and transactions keep that consistent without extra app code.
- Postgres has `jsonb`, so you still get flexible document fields where the schema is loose.
- One database can also cover full-text search, queues (`SKIP LOCKED`), and `pgvector`. That means fewer services to run.
- Hosted options (Neon, Supabase, RDS) are cheap and well supported.

**When MongoDB fits better:**
- Your data is mostly self-contained documents with little cross-referencing (e.g. a CMS or event/log store).
- You expect to shard horizontally early. Most small SaaS apps never reach that point.

The main risk with Mongo is that you end up rebuilding joins and integrity checks in application code as the product grows. Moving from Mongo to Postgres later is harder than the reverse.

If you tell me your core entities and what the app does, I can sketch a schema or check whether anything pushes you toward Mongo.
