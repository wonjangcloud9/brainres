<!-- Q: URGENT: I just ran DROP TABLE users on production by accident. What do I do? -->

**Stop all writes to the database now, then restore from a backup or point-in-time recovery (PITR).** Every new write can make recovery harder.

1. **Freeze the app.** Put it in maintenance mode, scale the app servers to 0, or revoke write access for the app's DB user. Don't run any more commands on the DB.
2. **Don't "recreate" the table yet.** If you create an empty `users` table, you may complicate a restore.
3. **Find your recovery source.** Check these in order:
   - **Managed DB (RDS, Cloud SQL, Supabase, Neon, PlanetScale):** use PITR and restore to a **new instance** at a time just before the drop. Don't restore over production.
   - **Self-hosted Postgres:** use a base backup plus WAL archive to recover to a timestamp before the drop.
   - **Self-hosted MySQL:** restore the last dump or snapshot, then replay binlogs up to just before the `DROP`.
   - **Last resort:** a nightly `pg_dump`/`mysqldump`, a volume snapshot, or a read replica that hasn't applied the drop. Replicas usually replay the drop within seconds, so check whether one has a delayed-replication setting.
4. **Restore into a separate instance, then verify.** Check the `users` row count and the newest `created_at` against what you expect.
5. **Move the data back.** Dump just the `users` table from the restored copy and load it into production. Then check foreign keys. If you ran `DROP ... CASCADE`, dependent objects, constraints and other tables may be gone too.
6. **Resume the app** only after you've checked the restored data.

I'm not sure which database or host you use, and the exact commands depend on that. Tell me which one it is (for example "Postgres on RDS") and I'll give you the exact restore commands. If you have shell access here, I can also check your backup config.
