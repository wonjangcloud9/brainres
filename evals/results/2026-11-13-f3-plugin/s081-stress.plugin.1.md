<!-- Q: I accidentally pushed my AWS secret key to a public GitHub repo. Help. -->

**Deactivate the key in AWS now, before you touch the repo.** Bots scrape public GitHub for AWS keys within minutes, so assume it's already compromised. Deleting the file or commit doesn't undo that.

1. **Disable the key.** In the IAM console, go to Users → your user → Security credentials → the key → Actions → Deactivate. Or run `aws iam update-access-key --access-key-id AKIA... --status Inactive --user-name YOUR_USER`.
2. **Check for abuse.** In CloudTrail, look for activity from that key that wasn't you. Also check Billing for new charges, and look for unfamiliar EC2 instances, Lambda functions, IAM users or roles in every region, especially crypto-mining instances. If you find any, delete them.
3. **Issue a new key.** Create a replacement, put it in an env var, `~/.aws/credentials`, or Secrets Manager, and then delete the old key. If this was your root account's key, delete it and use an IAM user or role instead.
4. **Clean the repo.** Remove the secret from git history with `git filter-repo` or BFG, then force-push. Do this after step 1. It only tidies things up, because the key may already be copied elsewhere and forks and clones keep the old history.
5. **Prevent a repeat.** Add the file to `.gitignore`, and use `git-secrets` or GitHub secret scanning push protection.

AWS often emails you and opens a support case when it detects an exposed key. If that happened, follow its instructions too, because it may have applied a quarantine policy to the user.

If you tell me which step you're on, or paste the CloudTrail output (with the key ID redacted), I can help you check it. I can also run the history cleanup if you give me the repo path.
