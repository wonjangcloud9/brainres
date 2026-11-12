<!-- Q: Postgres or MongoDB for a small SaaS app? -->

Postgres. A small SaaS app almost always has relational data (users, orgs, subscriptions, invoices) that needs transactions and joins, and Postgres handles that while also covering flexible data through its `jsonb` columns.

**Why Postgres wins for this case**
- **Relational by default:** tenants, billing, and permissions are naturally linked tables, and foreign keys keep them consistent.
- **Schema flexibility when needed:** `jsonb` with GIN indexes covers the "document" cases (settings, webhooks payloads, custom fields) without a second database.
- **Ecosystem:** managed options (Neon, Supabase, RDS, Fly) are cheap at small scale, and most ORMs and auth/billing libraries assume Postgres first.
- **Fewer migrations of regret:** moving from Postgres to Mongo later is rare, while moving from Mongo to Postgres once you need joins and transactions is a common, painful rewrite.

**Strongest case for MongoDB**
Your core data is truly document-shaped, with deeply nested records that are read and written as a unit and have highly variable structure (e.g., a CMS or event store). Even then, Postgres with `jsonb` is usually enough at small scale.

**Next action:** tell me your main entities and access patterns, and I can sketch a starter schema. If you already have a project directory, I can scaffold the Postgres setup there.
