<!-- Q: URGENT: I just ran DROP TABLE users on production by accident. What do I do? -->

**First, check whether your session is still in an open transaction. In Postgres, if you ran `BEGIN` and haven't committed, run `ROLLBACK;` and the table comes back.** MySQL can't do this, because DDL commits immediately.

If it's already committed:

1. **Stop writes now.** Pause the app or point it at maintenance mode so nothing new hits the database. Don't recreate an empty `users` table, because that lets new signups collide with the data you'll restore.
2. **Take a snapshot or backup of the current state** before you change anything.
3. **Restore to a new instance, not over production.** On RDS, Cloud SQL, or Azure, use point-in-time recovery to a moment just before the drop. On self-hosted Postgres or MySQL, restore the latest backup and replay WAL or binlog up to just before the `DROP`.
4. **Verify the restored `users` table**, then copy it back into production (`pg_dump -t users` / `mysqldump users`) or switch the app to the restored instance.
5. **Tell your team now**, so nobody runs a "fix" in parallel.

The order matters because point-in-time recovery depends on the logs, and extra writes and manual fixes make the recovery point harder to pick. Restoring to a new instance also leaves you a fallback if the first restore is wrong.

I don't know which database or host you're on, and the exact commands depend on that. Tell me which one it is (for example Postgres on RDS, or self-hosted MySQL) and I'll give you the exact commands for step 3.
