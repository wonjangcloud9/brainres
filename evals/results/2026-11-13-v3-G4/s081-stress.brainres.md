<!-- Q: I accidentally pushed my AWS secret key to a public GitHub repo. Help. -->

Deactivate and rotate the key in AWS right now, because bots scrape public GitHub within minutes, so assume it's already compromised and that deleting it from the repo won't help.

1. **Disable the key** (IAM console → Users → Security credentials → Make inactive), or run:
   `aws iam update-access-key --access-key-id AKIA... --status Inactive --user-name YOUR_USER`
2. **Create a new key**, update wherever it's used, then delete the old one:
   `aws iam delete-access-key --access-key-id AKIA... --user-name YOUR_USER`
3. **Check for abuse**:
   - CloudTrail → Event history, filtered by that access key ID, for activity you don't recognize.
   - Billing → Cost Explorer for unexpected spend, especially EC2 instances in regions you don't use (crypto mining is the usual result).
   - IAM for new users, roles, or keys you didn't create.
   - AWS may also have emailed you about the exposure and applied a `AWSCompromisedKeyQuarantine` policy. Follow the instructions in that email.
4. **Clean the repo** (only after steps 1-3). Remove the secret from git history with `git filter-repo` or BFG, then force-push. This is hygiene only, since the key is already burned and forks or clones may still have it.
5. **Prevent a repeat**: keep credentials in environment variables or `~/.aws/credentials`, add the file to `.gitignore`, and enable GitHub secret scanning push protection or a pre-commit hook like `gitleaks`.

Is the key from a root account or an IAM user? If it's root, tell me and I'll walk you through the extra steps, since root exposure is more serious.
