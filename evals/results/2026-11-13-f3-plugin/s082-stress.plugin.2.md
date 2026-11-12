<!-- Q: Our production database is at 100% CPU and customers are complaining. What do I do first? -->

**First, look at what the database is running right now, then stop the one query or client causing the load.** Don't restart it yet, because a restart drops your caches and connections and often makes the spike worse.

1. **See the top queries (about 1 minute).**
   - Postgres: `SELECT pid, now()-query_start AS runtime, state, left(query,100) FROM pg_stat_activity WHERE state <> 'idle' ORDER BY runtime DESC LIMIT 20;`
   - MySQL: `SHOW FULL PROCESSLIST;`
   - Managed (RDS, Cloud SQL): open Performance Insights or Query Insights. It shows the top SQL by load.

2. **Ask what changed.** Check for a deploy, migration, cron job, report or backfill in the last hour. A recent change is the most likely cause, so rolling it back or pausing it is the fastest fix.

3. **Stop the offender.**
   - Cancel a runaway query: Postgres `SELECT pg_cancel_backend(<pid>);` (use `pg_terminate_backend` only if cancel fails), MySQL `KILL <id>;`.
   - If one app or job is flooding the database, pause that job or scale the app down.
   - If connection count is huge, cap it or enable a pooler such as PgBouncer.

4. **Cut load while you diagnose.** Turn off non-critical traffic: analytics, exports, and batch jobs. If you have a read replica, point read-heavy endpoints at it.

5. **Scale up only as a stopgap.** A bigger instance buys time but won't fix a bad query. It works best when the cause is still unknown.

**Afterward:** run `EXPLAIN (ANALYZE)` on the culprit. A missing index or a changed plan is the usual cause.

I can't tell from here which database or host you use. If you tell me the engine and paste the output of step 1 (remove any sensitive values first), I'll help read it. What does it show?
