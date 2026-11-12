<!-- Q: Our production database is at 100% CPU and customers are complaining. What do I do first? -->

**First: find out what's running, not what to change.** Don't restart or scale blindly until you've seen the cause.

**1. See the active queries (1-2 minutes)**

Postgres:
```sql
SELECT pid, now() - query_start AS runtime, state, wait_event_type, left(query, 120)
FROM pg_stat_activity
WHERE state <> 'idle'
ORDER BY runtime DESC
LIMIT 20;
```

MySQL:
```sql
SHOW FULL PROCESSLIST;
-- or sorted:
SELECT id, time, state, left(info, 120) FROM information_schema.processlist
WHERE command <> 'Sleep' ORDER BY time DESC LIMIT 20;
```

Look for: many copies of the same query, one very long-running query, or a pile-up of connections.

**2. Check what changed**
- A deploy or migration in the last few hours (new query, missing index, dropped index)
- Traffic spike or a retry storm from a client or job
- A cron/batch job or backup/analytics query kicked off
- Autovacuum or a stats change (Postgres) causing bad plans

**3. Stabilize, in order of least to most disruptive**
1. **Stop the offender:** cancel the runaway query (`SELECT pg_cancel_backend(pid);`, escalate to `pg_terminate_backend(pid)`; MySQL: `KILL <id>;`). Pause the cron job or batch process if that's the source.
2. **Roll back** the recent deploy or feature flag if timing lines up.
3. **Shed load:** rate-limit or disable the expensive endpoint, lower app connection pool sizes, and put heavy reads on a replica.
4. **Add capacity:** scale up the instance (a stopgap, and on some managed services it causes a brief failover).
5. **Add a missing index** only if you've confirmed it's the cause. Use `CREATE INDEX CONCURRENTLY` in Postgres so you don't lock writes.

**4. Communicate**
Post a status page update now and name one person to run the investigation, with another handling customer comms.

**Avoid:** restarting the DB (you lose cache and the problem often returns immediately), running `VACUUM FULL` or big schema changes, or killing things you haven't looked at.

Tell me which database and host (RDS, Cloud SQL, self-hosted?) and paste the output of step 1 with anything sensitive removed. I'll help you identify the culprit and the safest fix. If you want, I can also look at the app code in this directory for the offending query, but this directory doesn't appear to be a git repo, so I'd need to know where the relevant code lives.
