<!-- Q: URGENT: our checkout API is returning 503 for every request and we're losing orders. What do I do first? -->

**Roll back the most recent deploy or config change now if there was one in the last few hours.** A 503 on every request usually means the service has no healthy backends, and a bad change is the most common cause.

1. **Declare the incident.** Tell your team in one message who is leading and who is communicating, so people don't debug in parallel and overwrite each other.
2. **Find out what changed.** Check the deploy log, feature flags, config, certificates and infrastructure changes. If something changed, roll it back before you diagnose further.
3. **Check where the 503 comes from.** Look at the load balancer or gateway for "no healthy upstream" or an empty target group, then at the app's health checks and logs. If the app is up but health checks fail, a dependency is the likely cause. Check the database, cache and payment provider.
4. **Stop the revenue loss.** If you can't fix it in minutes, show a maintenance message or queue orders for retry. Silent failures are worse than a clear message.
5. **Restart only after you know the cause.** If you don't have one yet, restart one instance, not the fleet.

**Don't blindly restart everything or scale up.** If a database or downstream service is the bottleneck, a mass restart sends a burst of reconnects that keeps it down. If the cause is a bad deploy, restarting just reloads the same bug.

I can't see your infrastructure from here. If you paste the load balancer error, the app logs, or the last deploy diff, I'll help you read them. Tell me your stack (Kubernetes, ECS, nginx, etc.) and I'll give you the exact commands.
