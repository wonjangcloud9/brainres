<!-- Q: Postgres or MongoDB for a small SaaS app? -->

Postgres, because a SaaS app almost always has relational data (users, orgs, subscriptions, invoices) where joins, transactions, and constraints matter, and Postgres also stores JSON via `jsonb` when you need flexible fields.

**Why not Mongo by default:** its main advantage is schema flexibility, but you rarely need that on day one. You often pay for it later with manual consistency checks and awkward cross-collection queries (e.g., "revenue per plan per org").

**Pick Mongo only if** your core data is document-shaped with deep nesting, varies a lot per record, and you rarely join across it (content or event stores, for example).

**Practical edge for a small team:** Postgres has managed options with generous free tiers (Neon, Supabase, RDS), one tool covers relational, JSON, and full-text search, and most ORMs and auth libraries target it first.

If you tell me what the app stores and your stack, I can confirm the choice or sketch a starting schema.
