<!-- Q: Postgres or MongoDB for a small SaaS app? -->

Postgres, unless your data is truly document-shaped with no relationships between records.

A small SaaS app almost always has users, accounts, subscriptions, and permissions. Those are relational, and you want joins, foreign keys, and transactions (billing and access control break badly without them). Postgres also has `jsonb`, so you can store flexible fields without leaving it.

The strongest case for MongoDB: your core data is large, nested documents that you read and write whole, and the schema changes often. Even then, `jsonb` columns cover most of it.

Practical reasons that also favor Postgres:
- Managed options are cheap or free to start (Supabase, Neon, RDS).
- Most ORMs, migration tools, and tutorials default to it.
- Moving later from a relational schema to documents is easier than the reverse, because relational constraints force you to define your data model early.

If you tell me what the app stores and how records relate, I can check whether it hits the Mongo exception.
