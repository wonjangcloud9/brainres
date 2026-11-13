<!-- Q: Our production database is at 100% CPU and customers are complaining. What do I do first? -->

Find the queries burning CPU right now and cancel the worst one, because that restores service faster than any root-cause work.

**1. See what's running** (I'm assuming Postgres or MySQL; tell me which if it's something else):

Postgres:
```sql
SELECT pid, now() - query_start AS runtime, state, left(query, 120)
FROM pg_stat_activity
WHERE state <> 'idle'
ORDER BY runtime DESC
LIMIT 10;
```

MySQL:
```sql
SHOW FULL PROCESSLIST;
```

**2. Cancel the offender.** Cancel before terminating, since it's gentler:

- Postgres: `SELECT pg_cancel_backend(<pid>);`, then `pg_terminate_backend(<pid>)` if it ignores you.
- MySQL: `KILL QUERY <id>;`

**3. Check what changed.** If many identical queries pile up rather than one long one, look for a recent deploy, a cache outage, a new cron job, or a traffic spike. Rolling back the deploy or pausing the job is often the real fix.

**4. If it's still pinned**, shed load: pause background workers, rate-limit the heaviest endpoint, or fail over to a replica. Scaling up the instance is a last resort, because it buys time but doesn't fix a bad query.

**Avoid** killing queries blindly (a long-running migration or backup may be one of them), and avoid restarting the database, which drops caches and usually makes the stampede worse.

After it's stable, use `pg_stat_statements` (or the MySQL slow query log) to find the query and add the missing index or fix it.

Run step 1 and paste the top rows here, with identifying values redacted, and I'll help you pick what to cancel.
