<!-- Q: Our production database is at 100% CPU and customers are complaining. What do I do first? -->

**First, see what is running right now, then stop the worst offender.** Don't restart the database yet, because a restart drops your cache and the load usually comes straight back.

1. **List active queries, longest-running first.**
   - Postgres: `SELECT pid, now()-query_start AS dur, state, left(query,100) FROM pg_stat_activity WHERE state <> 'idle' ORDER BY dur DESC;`
   - MySQL: `SHOW FULL PROCESSLIST;`
2. **Look for one pattern.** This could be one query repeated hundreds of times, a long-running report or batch job, or a pile-up behind a lock.
3. **Cancel it.**
   - Postgres: `SELECT pg_cancel_backend(<pid>);`. Use `pg_terminate_backend` only if cancel fails.
   - MySQL: `KILL <id>;`
4. **If the cause is outside the database, stop it at the source.** Check for a deploy in the last hour (roll it back), a cron job or analytics query (pause it), or a traffic spike or retry storm (rate-limit it).
5. **If nothing stands out and the load is just high,** add read replicas or scale up the instance. This buys time but doesn't fix the cause.

I'm assuming a standard relational database. If yours is a managed one such as RDS or Cloud SQL, its performance dashboard (Performance Insights or Query Insights) shows the top queries faster than the commands above.

Tell me your database engine and what the top queries show, and I'll help work out the fix. Also tell me whether anything was deployed recently.
