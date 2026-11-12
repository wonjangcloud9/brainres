<!-- Q: I accidentally pushed my AWS secret key to a public GitHub repo. Help. -->

Assume the key is already compromised: bots scrape GitHub for AWS keys within minutes. Rotating the key matters more than cleaning the repo.

**Do these in order:**

1. **Deactivate the key now.** AWS Console → IAM → Users → your user → Security credentials → find the key → **Make inactive**. Or run:
   ```
   aws iam update-access-key --user-name <USER> --access-key-id <AKIA...> --status Inactive
   ```
2. **Check for abuse.** In CloudTrail (Event history), filter by that access key ID. Also look at Billing for unexpected EC2 instances, especially in regions you don't use, and for new IAM users, roles, or access keys you didn't create.
3. **Create a new key**, update wherever the old one was used, then **delete** the old key.
4. **Remove the secret from the repo.** Delete the file or line, and use `git filter-repo` or BFG to purge it from history, then force-push. This is cleanup only. The key stays exposed in forks, clones, and caches, so it is only safe because of step 1.
5. **Prevent a repeat.** Keep secrets in env vars or `~/.aws/credentials`, add the file to `.gitignore`, and enable GitHub secret scanning push protection. Better still, use IAM roles or SSO instead of long-lived keys.

AWS often sends an exposure notice and may attach a `AWSCompromisedKeyQuarantine` policy to the user. If you see that, it doesn't replace rotating the key.

I can help with the history purge, but this directory isn't a git repo. Tell me where the repo is, or paste the output of `git log --stat` for the commit with the key, and I'll give you the exact `git filter-repo` commands. Have you deactivated the key yet?
