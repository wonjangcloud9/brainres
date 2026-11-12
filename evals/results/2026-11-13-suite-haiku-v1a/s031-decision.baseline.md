<!-- Q: Postgres or MongoDB for a small SaaS app? -->

**Postgres**, for most small SaaS apps.

- **Your data is probably relational.** Users, orgs, memberships, subscriptions, invoices, and permissions all reference each other. Foreign keys and joins handle that cleanly, and Postgres enforces integrity so bad data can't slip in.
- **Schema changes are manageable.** Migrations are well understood, and the schema documents the app. Mongo's flexibility means the schema lives in application code, which tends to drift as the app grows.
- **It's a sound default for growth.** Postgres handles JSON via `jsonb` if you need semi-structured fields, full-text search, and row-level security. It scales well past where most small SaaS apps will ever be.
- **Hosting is easy.** Managed options like Supabase, Neon, RDS, and Render make it low-maintenance.

**Consider MongoDB** if your data is genuinely document-shaped with little cross-referencing, such as per-tenant blobs of varying structure, or your team already knows Mongo well and the app is mostly reads and writes of self-contained documents.

Unless one of those applies, pick Postgres. If you tell me what the app does and what your data looks like, I can give a more specific recommendation.
