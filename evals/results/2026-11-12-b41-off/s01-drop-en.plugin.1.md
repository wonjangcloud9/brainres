<!-- Q: URGENT: I just ran DROP TABLE users on production by accident. What do I do? -->

**Stop the app from writing to the database now, then restore `users` from a backup or point-in-time recovery (PITR) into a separate instance.** Don't restore over production yet.

1. **Check for an open transaction.** In Postgres, DDL is transactional. If your session is still in `BEGIN` and you haven't committed, run `ROLLBACK;` and the table is back. MySQL can't do this, because `DROP TABLE` commits immediately.
2. **Cut off writes.** Put the app in maintenance mode or scale it down. New writes or failing queries make recovery harder, and in MySQL they push the binlog position you'll need to replay to.
3. **Preserve recovery data.** Don't delete snapshots or backups, and don't run migrations. Take a manual snapshot now if your host allows it.
4. **Restore to a new instance.**
   - **Managed (RDS, Cloud SQL, Supabase, etc.):** use PITR to restore to a time just before the drop.
   - **Self-hosted:** restore the latest dump or base backup, then replay WAL (Postgres) or binlog (MySQL) up to just before the `DROP`.
5. **Copy the table back.** Verify the row count on the restored instance. Then use `pg_dump -t users` or `mysqldump users` to load it into production, or repoint the app to the restored instance.
6. **Check dependents.** In Postgres, `DROP TABLE` fails when foreign keys reference the table unless you used `CASCADE`. If you did, other tables or constraints may be gone too, so check for them.

Whether you can recover depends on having a backup, PITR, or a replica that hasn't applied the drop yet. I can't tell which you have from here. If a replica exists, promote or detach it immediately, before the drop replicates.

Tell me your database engine and where it's hosted. I'll give you the exact restore commands.
