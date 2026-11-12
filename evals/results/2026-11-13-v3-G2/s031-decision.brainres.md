<!-- Q: Postgres or MongoDB for a small SaaS app? -->

Postgres, because a SaaS app almost always has relational data (users, orgs, subscriptions, invoices) that benefits from joins, transactions, and constraints.

**Why Postgres fits small SaaS:**
- Multi-tenant data, billing, and permissions are relational, so foreign keys and transactions prevent bad states that you'd otherwise enforce in app code.
- It also has `jsonb`, so you get flexible schema where you need it without a second database.
- Managed hosting is cheap and common (Supabase, Neon, RDS, Render), and most ORMs and auth libraries target it first.

**When MongoDB wins instead:** your core data is truly document-shaped with varying structure (e.g. a CMS or event/catalog store), you rarely join across collections, and your team already knows it well. That's the minority case for SaaS.

**Strongest point against my pick:** if your schema is still changing weekly, Mongo's looseness feels faster at first. But Postgres migrations are cheap at small scale, and the `jsonb` column covers the truly unstructured parts.

If you tell me what the app stores and your stack, I can sketch a starting schema.
