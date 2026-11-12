<!-- Q: I accidentally pushed my AWS secret key to a public GitHub repo. Help. -->

**Revoke the key now, in the AWS console.** Don't start by deleting the commit or the repo, because bots scrape public GitHub within minutes and the key is already compromised.

1. **Deactivate the key:** IAM → Users → your user → Security credentials → the access key → Actions → **Deactivate**. Then create a new key and update your apps.
2. **Check for abuse:**
   - CloudTrail → Event history, filtered by that access key ID.
   - Billing → Cost Explorer, for unexpected EC2, GPU or region usage.
   - Look for new IAM users, roles, keys or running instances you didn't create.
3. **Clean up anything the attacker made:** delete unknown resources and users, and check every region, not just your usual one.
4. **Delete the old key** once nothing depends on it.
5. **Remove it from the repo.** Do this after revoking, since the key stays in git history and in any forks or clones.
   - Rewrite history with `git filter-repo` or BFG, then force-push.
   - Treat the key as burned even after the rewrite.
6. **Check your email.** AWS usually sends a "compromised key" notice and may have attached a `AWSCompromisedKeyQuarantine` policy. Follow its instructions and open a support case if there are unexpected charges. AWS often credits fraud costs if you report quickly.
7. **Prevent a repeat:**
   - Use `git-secrets` or `gitleaks` as a pre-commit hook.
   - Turn on GitHub secret scanning and push protection.
   - Prefer IAM roles or SSO over long-lived keys.
   - Load secrets from env vars or a `.env` file listed in `.gitignore`.

Start with step 1. If you tell me what CloudTrail or billing shows, I can help you read it.
