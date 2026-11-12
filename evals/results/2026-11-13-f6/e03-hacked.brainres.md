<!-- Q: Emergency: I think our admin account was hacked. There are logins from another country and new users I didn't create. -->

Treat it as a real breach: lock the admin account and kill all sessions first, then look at what the attacker created.

**Contain now (first 15 minutes)**
1. Change the admin password from a clean device, and revoke all active sessions, API keys and tokens.
2. Enable or reset MFA on the admin account. Use an authenticator app or hardware key, not SMS.
3. Disable (don't delete) the unknown users, so you keep the evidence.
4. If the attacker can still get in, block their IPs or the foreign country at the firewall or login provider.

**Preserve evidence**
- Export the login and audit logs now, before they rotate. Record the attacker IPs, timestamps, and what each new user did.

**Check what they touched**
- Look for new admin roles, changed permissions, new API keys or OAuth apps, forwarding rules, and altered billing or recovery email/phone.
- Rotate any secret the admin could see: database passwords, cloud keys, SMTP credentials.
- If the admin password was reused anywhere, change it there too, and scan the admin's laptop for malware, because a stolen password alone may not explain this.

**Later**
- Notify affected users or regulators if their data was accessed. Many jurisdictions set a deadline, often 72 hours, so check yours.

I don't know your platform, so I can't give exact menu paths or log commands. Tell me what the admin account is for (e.g. a WordPress site, AWS, Google Workspace, or a custom app), and I'll walk you through the specific steps. If the app's code or logs are in this directory, I can also help review them.
