<!-- Q: Our production database is at 100% CPU and customers are complaining. What do I do first? -->

Look at what is running right now and cancel the runaway queries, because that relieves CPU faster than any fix to the code or the schema.

1. **See the top consumers.** I don't know your engine, so here are the two common ones:
   - Postgres:
     ```sql
     SELECT pid, now() - query_start AS runtime, state, wait_event, left(query, 120)
     FROM pg_stat_activity
     WHERE state <> 'idle'
     ORDER BY runtime DESC LIMIT 20;
     ```
   - MySQL:
     ```sql
     SHOW FULL PROCESSLIST;
     ```
2. **Look for the pattern.** One query repeated hundreds of times, or a few very long-running ones, usually points to a missing index, a bad plan, or a new deploy.
3. **Cancel the offenders.** In Postgres, use `SELECT pg_cancel_backend(<pid>);` first and `pg_terminate_backend(<pid>)` only if that fails. In MySQL, use `KILL <id>;`. **Only kill reads or known-safe queries.** Killing a long write forces a rollback, which can itself take a long time and use more CPU.
4. **Stop the source.** If the queries come from a recent deploy, cron job, or one client, roll back or pause it. Otherwise the same queries will start again right after you kill them.
5. **Reduce load while you recover.** Shed traffic, for example by rate-limiting, pausing batch jobs, or serving cached reads. If you have a read replica, point the heavy reads there.

Do not restart the database as a first move. It clears the buffer cache, so the load usually returns even higher and you lose the evidence of what caused it.

After CPU settles, check whether the culprit query changed plans (`EXPLAIN ANALYZE`) or lacks an index. Also check whether a deploy or traffic spike lines up with the start time.

Which database and host (RDS, Cloud SQL, self-hosted) are you on? Paste the output of step 1 and I'll help you pick what to kill.
