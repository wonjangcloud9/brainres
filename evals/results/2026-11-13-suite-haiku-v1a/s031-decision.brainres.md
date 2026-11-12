<!-- Q: Postgres or MongoDB for a small SaaS app? -->

Postgres, for most small SaaS apps.

Your data is almost certainly relational: users, accounts, subscriptions, invoices, and permissions reference each other. Postgres enforces those relationships with foreign keys and transactions, so a billing bug can't leave an orphaned row. MongoDB's flexible schema moves that checking into your application code, where it's easy to miss.

Choose MongoDB only if your core data is document-shaped and varies a lot per record, such as user-defined forms or CMS-style content with no fixed fields.

Postgres also covers JSON columns (`jsonb`) if you need some flexible fields later, so you rarely have to pick the document store for that alone.

Next step: if you tell me the main entities in your app (for example, the tables you expect), I can sketch a schema and confirm whether any part of it really needs a document model.
