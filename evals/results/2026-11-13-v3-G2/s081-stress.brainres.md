<!-- Q: I accidentally pushed my AWS secret key to a public GitHub repo. Help. -->

**Deactivate the key in AWS right now, before touching GitHub.** Bots scrape public repos within minutes, so assume the key is already stolen. Removing it from the repo does not make it safe again.

**Do these in order:**

1. **Disable the key.** In the IAM console, go to Users → your user → Security credentials → the key → Actions → Deactivate. Or run `aws iam update-access-key --user-name <USER> --access-key-id <AKIA...> --status Inactive`.
2. **Check for abuse.** Look in CloudTrail event history for activity from that key you don't recognize. Also check for new IAM users, new access keys, and EC2 instances in regions you don't use. Crypto miners are the usual result. Check the Billing dashboard too. AWS may also have emailed you or opened a support case, so look in your inbox.
3. **Create a new key and delete the old one.** Put the new key in environment variables, `~/.aws/credentials`, or a secrets manager. Never put it in the repo. If the key belonged to a role with broad permissions, shrink them to what the app needs.
4. **Clean the repo.** Do this last, because the old key is already dead and the cleanup is only tidiness. Use `git filter-repo --replace-text` or BFG to remove the secret from history, then force-push. Forks and clones keep the old commits, which is why step 1 is the one that protects you.

To prevent a repeat, add the secrets file to `.gitignore` and turn on GitHub secret scanning push protection in the repo settings.

Do you want me to run the CLI commands for steps 1 and 2? I would need your AWS CLI configured here and the key ID (the `AKIA...` part, not the secret).
