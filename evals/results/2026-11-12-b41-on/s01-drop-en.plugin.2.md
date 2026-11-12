<!-- Q: URGENT: I just ran DROP TABLE users on production by accident. What do I do? -->

**Stop all writes to the database now, and if your session is still inside an open transaction, run `ROLLBACK;`.** In Postgres and SQLite, `DROP TABLE` can be rolled back before commit. In MySQL it can't, because DDL auto-commits.

1. Pause the app, or put it in maintenance mode, so nothing else writes to the database.
2. Don't re-create the table, run migrations, or restart or resize the database. Those can overwrite the logs and snapshots you need for recovery.
3. Find your newest recovery source:
   - **Managed (RDS, Cloud SQL, Supabase, Neon):** use point-in-time restore to a time just before the drop. Restore to a **new instance**, not over production.
   - **Self-hosted Postgres:** use the latest `pg_dump` or base backup plus WAL replay to a timestamp just before the drop.
   - **Self-hosted MySQL:** use the latest dump plus binlog replay up to just before the `DROP`.
4. Check the restored copy: count rows in `users` and spot-check recent signups.
5. Copy `users` back into production with `pg_dump -t users` or the MySQL equivalent. Then re-enable the app.

The restore goes to a new instance because it lets you verify the data before touching production. It also keeps your options open if the first restore point turns out to be wrong. Every write after the drop makes recovery harder, so pausing the app comes first.

Tell me which database and host you use, and whether you have PITR or backups enabled. I'll give you the exact commands.
