<!-- Q: Our production database is at 100% CPU and customers are complaining. What do I do first? -->

**Find the queries eating the CPU and kill or stop the worst offenders. Don't restart the database, because that drops your cache and usually makes the outage longer.**

1. **Check what changed.** A deploy, a traffic spike, a cron job or a failed-over replica in the last hour is the likely cause. If a deploy is the cause, roll it back first. That is faster than any DB tuning.
2. **See what is running now.**
   - Postgres: `SELECT pid, now()-query_start AS runtime, state, left(query,100) FROM pg_stat_activity WHERE state <> 'idle' ORDER BY runtime DESC LIMIT 20;`
   - MySQL: `SHOW FULL PROCESSLIST;`
3. **Cancel the runaway queries.** Postgres: `SELECT pg_cancel_backend(<pid>);`, and use `pg_terminate_backend` only if cancel fails. MySQL: `KILL QUERY <id>;`. Start with long-running analytics, reports or batch jobs, not customer-facing queries.
4. **Reduce incoming load.** Pause cron jobs and background workers, and rate-limit or shed traffic at the app layer. If connections are piling up, lower the pool size, because too many concurrent queries makes CPU contention worse.
5. **Add capacity if the cause isn't clear.** Scale the instance up, or route reads to a replica. On RDS or Cloud SQL this takes a few minutes, but it can involve a brief failover, so check that first.

Afterward, find the root cause with `pg_stat_statements` (Postgres) or the slow query log (MySQL). A missing index or a plan change after a stats update is a common culprit.

Tell me which database you're on (Postgres, MySQL, or managed RDS/Aurora) and paste the top few rows from step 2. I can then help you decide which queries to kill.
