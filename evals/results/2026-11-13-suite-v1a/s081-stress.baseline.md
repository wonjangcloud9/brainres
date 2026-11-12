<!-- Q: I accidentally pushed my AWS secret key to a public GitHub repo. Help. -->

Act in this order. Rotating the key matters most, and cleaning git history comes after.

**1. Deactivate and rotate the key now (do this first)**
- AWS Console → IAM → Users → your user → Security credentials → find the exposed access key → **Make inactive**, then create a new key and **Delete** the old one.
- Or via CLI (replace the placeholders):
  ```
  aws iam update-access-key --user-name <USER> --access-key-id <AKID> --status Inactive
  aws iam create-access-key --user-name <USER>
  aws iam delete-access-key --user-name <USER> --access-key-id <AKID>
  ```
- Update any apps or services that used the old key.

Bots scrape GitHub for AWS keys within minutes, so assume the key is already compromised. Removing it from the repo does not undo that.

**2. Check for abuse**
- **CloudTrail** → Event history: filter by the access key ID and look for unfamiliar activity (especially `RunInstances`, `CreateUser`, `CreateAccessKey`, `PutUserPolicy`, `AttachUserPolicy`).
- **Billing / Cost Explorer**: look for unexpected spend, particularly EC2 in regions you don't use.
- Check for new IAM users, roles, access keys, EC2 instances, Lambda functions, and S3 buckets you didn't create. Delete any you find.
- AWS often opens a support case and attaches a `AWSCompromisedKeyQuarantine` policy to the user. Follow the instructions in that case, and respond to it.

**3. Remove the secret from the repo**
This is secondary because the key is already revoked, but worth doing:
- Remove it from the code and use environment variables or AWS Secrets Manager instead.
- Rewrite history so it isn't sitting in old commits:
  ```
  pip install git-filter-repo
  git filter-repo --replace-text <(echo '<THE_SECRET>==>REMOVED')
  git push --force
  ```
- Forks, clones, and GitHub's cached views may still hold the old commits. This is another reason rotation is the real fix.

**4. Prevent a repeat**
- Add the file to `.gitignore` (e.g. `.env`).
- Enable GitHub **secret scanning** and **push protection** in the repo's Settings → Code security.
- Consider a pre-commit hook like `gitleaks` or `git-secrets`.
- Prefer IAM roles or short-lived SSO credentials over long-lived access keys.

I can help with any of these. The working directory I'm in isn't a git repo, so if you point me to the affected repo, I can search its history for the secret, and help with the filter-repo cleanup. Note that I won't force-push without your confirmation, since that's hard to reverse.
