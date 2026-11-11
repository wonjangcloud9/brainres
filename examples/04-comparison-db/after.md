Use SQLite to start, and move to Postgres when more than one server needs to write at the same time.

Your data is relational, because every todo belongs to a user. SQLite and Postgres both handle that with plain SQL joins.

| | SQLite | Postgres | MongoDB |
|---|---|---|---|
| Setup | none, one file | run a server | run a server |
| Writers at once | one | many | many |
| Users ↔ todos | SQL join | SQL join | manual or `$lookup` |
| Free hosting | yes | free tiers | free tiers |

SQLite would be the wrong choice if you expect many people writing at once from day one. In that case, start on Postgres.

Next step: create `app.db` with a `users` table and a `todos` table that has a `user_id` column.
