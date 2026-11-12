<!-- Q: Emergency: I think our admin account was hacked. There are logins from another country and new users I didn't create. -->

**First, change the admin password and sign out all active sessions, from a device you trust.** Don't delete the unknown users yet, because that destroys evidence. Disable them instead.

1. **Lock the admin account.** Set a new, unique password. Use "sign out all sessions" or "revoke tokens" if the platform has it. Turn on MFA, preferably an authenticator app or a hardware key rather than SMS.
2. **Disable the new users.** Suspend them, don't delete them. Screenshot or export the user list and the login log first.
3. **Revoke other access paths.** Rotate API keys, app passwords, OAuth grants and SSH keys. Check for forwarding rules, new webhooks, and new admin or role grants. An attacker can keep access through these even after a password reset.
4. **Change the password on the email account used for admin recovery.** If that email is compromised, the attacker can reset everything again.
5. **Save the logs.** Export the login history (IPs, times, user agents) and the admin audit log before they roll over.

This order cuts off the attacker first and keeps the evidence you need to see what they did. If you reuse the admin password on other sites, change it there too.

I can't tell from here what system this is or whether the attacker got further in. If you tell me the platform (Google Workspace, Microsoft 365, AWS, WordPress, your own app), I'll give exact click-paths and the log queries to run. If the system runs on this machine, I can also check its logs and config for you.
