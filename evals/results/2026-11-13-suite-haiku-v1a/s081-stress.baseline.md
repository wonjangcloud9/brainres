<!-- Q: I accidentally pushed my AWS secret key to a public GitHub repo. Help. -->

This is urgent, but it's fixable. Act in this order: the key is compromised the moment it's public, so rotating it matters more than cleaning up the repo.

## 1. Deactivate the key now (do this first)

Go to the AWS IAM console, or run the CLI command below if you have another working credential:

- **Console:** IAM → Users → (the user that owns the key) → Security credentials → Access keys → **Deactivate**, then **Delete** once you've confirmed nothing depends on it.
- **CLI:**
  ```bash
  aws iam update-access-key --access-key-id AKIAXXXXXXXXXXXXXXXX --status Inactive --user-name <user>
  aws iam delete-access-key --access-key-id AKIAXXXXXXXXXXXXXXXX --user-name <user>
  ```

If the key belongs to a root account, rotate it from the root credentials page and consider enabling MFA on root.

## 2. Check whether it was used

Bots scrape GitHub for AWS keys within minutes, so assume it may have been exploited.

- **CloudTrail** (Event history, or Athena if you have a trail): filter by `Access key ID` = the leaked key, and look at the time since the push. Look for unfamiliar `RunInstances`, `CreateUser`, `CreateAccessKey`, `PutUserPolicy`, IAM changes, or access from unfamiliar regions.
- **IAM → Access key last used** shows the most recent activity for the key.
- **Billing / Cost Explorer:** check for unexpected spend, especially GPU instances, which are common in crypto-mining abuse.
- **GuardDuty** (if enabled) will flag suspicious activity.

If you see unauthorized activity, also check for IAM users, roles, or policies you didn't create, and delete them.

## 3. Remove the secret from GitHub

Deleting the file in a new commit isn't enough. The key stays in git history and in any forks or clones.

- Rewrite history with **git-filter-repo** (preferred) or BFG Repo-Cleaner:
  ```bash
  pip install git-filter-repo
  git filter-repo --replace-text <(echo 'AKIAXXXXXXXXXXXXXXXX==>REDACTED')
  git push --force --all
  git push --force --tags
  ```
  Replace the key with your actual value. Coordinate with any collaborators, since they'll need to re-clone.
- If the repo was public for a while, GitHub may still cache the old commits. Contact GitHub Support to purge cached views if needed.

Rotating the key is what actually makes the leak harmless. The history rewrite is cleanup.

## 4. Prevent a repeat

- Add the secret file to `.gitignore`, and use `AWS_PROFILE` or environment variables instead of hardcoded keys.
- Install a pre-commit secret scanner such as `gitleaks` or `git-secrets`, or enable GitHub secret scanning push protection (Settings → Code security).
- Prefer IAM roles or AWS SSO over long-lived access keys wherever you can.

---

If you tell me whether the key was for a root account or an IAM user, and whether you can still reach the AWS console, I can help you narrow down the CloudTrail search. I can also review your repo for any other secrets, if you'd like.
