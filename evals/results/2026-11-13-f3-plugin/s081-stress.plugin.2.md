<!-- Q: I accidentally pushed my AWS secret key to a public GitHub repo. Help. -->

**Deactivate the key in AWS now, before you touch the repo.** Bots scrape GitHub for AWS keys within minutes, so deleting the commit won't help. Treat the key as stolen.

1. **Deactivate the key.** Go to IAM → Users → your user → Security credentials → the key → *Actions* → *Deactivate*. Or run `aws iam update-access-key --access-key-id AKIA... --status Inactive --user-name YOURUSER`.
2. **Check for abuse.** Open CloudTrail Event history and filter by that access key ID. Look at the Billing dashboard too. Common attacker moves are launching EC2 instances (crypto mining) in regions you don't use, creating new IAM users or keys, and reading S3 buckets. Terminate anything you don't recognize, and delete any IAM users or keys you didn't create.
3. **Create a new key and delete the old one.** Put the new key in environment variables, `~/.aws/credentials`, or a secrets manager. Do not put it in the repo. Then delete the old key.
4. **Clean the repo (optional, and only after steps 1–3).** Removing the key from git history is housekeeping, not security, because the key may already be copied. If you want to do it, use `git filter-repo` or BFG, then force-push. Forks and clones keep the old history.
5. **Prevent a repeat.** Add the file to `.gitignore`. Install `git-secrets` or `gitleaks` as a pre-commit hook, and turn on GitHub secret scanning push protection.

AWS often sends an "exposed key" email and may attach a `AWSCompromisedKeyQuarantine` policy to the user. If you got one, the key is already known to be exposed, so still do steps 1–3.

I can run the AWS CLI commands or clean the repo history if you want. Tell me which step to start with. For the repo, I'd need it cloned locally, because the current directory isn't a git repository.
