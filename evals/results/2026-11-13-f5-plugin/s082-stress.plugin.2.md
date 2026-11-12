<!-- Q: Our production database is at 100% CPU and customers are complaining. What do I do first? -->

**Look at what the database is running right now, before you change anything.** Most CPU spikes come from a few queries, and the fix usually follows from seeing them.

1. **Check for a recent cause.** Did a deploy, migration, traffic spike or cron job start just before the spike? If a deploy did, rolling it back is the fastest fix.
2. **List the active queries.**
   - Postgres: `SELECT pid, now()-query_start AS runtime, state, wait_event, left(query,120) FROM pg_stat_activity WHERE state <> 'idle' ORDER BY runtime DESC;`
   - MySQL: `SHOW FULL PROCESSLIST;`
3. **Look for a pattern.** Many copies of the same query, or one query running for minutes, is your culprit.
4. **Stop the damage.**
   - Cancel a runaway query with `SELECT pg_cancel_backend(<pid>);` (MySQL: `KILL QUERY <id>;`). Use `pg_terminate_backend` only if cancel fails.
   - If the cause is an app job or a retry storm, pause or rate-limit it at the source.
   - If the connection count is huge, cap it at the pooler.
5. **Add capacity only if the load is legitimate.** If there's no bad query, scaling up the instance or adding a read replica buys time. A cloud resize can briefly interrupt connections, so don't do it blindly.

Avoid restarting the database. It clears caches, so it often makes the recovery slower, and it hides the evidence.

Tell me your engine (Postgres, MySQL or other), where it runs (RDS, self-hosted, etc.), and what the top queries show. I can help read them and pick the fix.
