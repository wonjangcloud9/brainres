<!-- Q: URGENT: our checkout API is returning 503 for every request and we're losing orders. What do I do first? -->

Roll back the most recent deploy or config change now, because a 503 on every request usually means a bad release or no healthy backends, and rollback is the fastest safe fix.

1. **Check what changed.** Look at deploys, config or feature-flag changes, and infra changes in the last few hours. If anything lines up with the first 503, revert it before diagnosing further.
2. **Check backend health.** Look at your load balancer or ingress target health. If all targets are unhealthy, look at why the health check fails (crashed pods, failed startup, wrong port, bad health endpoint).
3. **Check dependencies.** Look at the database (connection limit hit, failover), cache, and payment provider. A shared dependency down can fail every request at once.
4. **Check capacity.** Look for out-of-memory kills, CPU saturation, exhausted connection pools, or autoscaling stuck at its max. If it's overload, scale up or restart the service.
5. **Read the logs.** The first error after the last healthy request names the cause.

While you work, post a status note so support and sales know, and if you have a maintenance or fallback page, enable it so customers don't see raw errors.

I can't see your infrastructure from here (this directory isn't a git repo and has no deploy tooling), so I can't run these checks for you. Paste the error from the load balancer or service logs, plus what you deploy on (Kubernetes, ECS, a VM, etc.), and I'll help pin down the cause. If the code is on this machine, give me the path and I'll look at recent changes.

Start with step 1 now.
