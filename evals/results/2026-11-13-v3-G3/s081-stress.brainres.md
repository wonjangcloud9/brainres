<!-- Q: I accidentally pushed my AWS secret key to a public GitHub repo. Help. -->

**Deactivate and rotate the key now, before anything else.** Bots scrape GitHub for AWS keys within minutes, so assume it is already compromised. Removing it from the repo does not undo that.

**1. Disable the key (do this first)**
```
aws iam update-access-key --user-name <USER> --access-key-id <AKIA...> --status Inactive
```
Or use the console: IAM → Users → your user → Security credentials → Make inactive.

**2. Create a new key and update your apps**
```
aws iam create-access-key --user-name <USER>
```
After everything works with the new key, delete the old one:
```
aws iam delete-access-key --user-name <USER> --access-key-id <AKIA...>
```

**3. Check for abuse**
- CloudTrail → Event history: look for calls from unfamiliar IPs, especially `RunInstances`, `CreateUser`, `CreateAccessKey`, `AttachUserPolicy`, and `PutUserPolicy`.
- Billing → Cost Explorer: look for new spend, especially EC2 in regions you don't use.
- Check for IAM users, roles, or keys you didn't create. Attackers often add these for persistence.
- AWS likely emailed you about the exposure and may have attached a `AWSCompromisedKeyQuarantine` policy. Follow any support case they opened.

**4. Clean the repo (only after rotating)**
Rewriting history is hygiene, not a fix, because the key may already be cloned or cached. Use `git filter-repo` or BFG to strip the file or string, then force-push. GitHub may still serve old commits by SHA, so contact GitHub Support to purge cached views if needed.

**5. Prevent a repeat**
- Add the file to `.gitignore`, and use env vars, AWS SSO, or IAM roles instead of long-lived keys.
- Turn on GitHub secret scanning and push protection.
- Add a pre-commit hook such as `gitleaks` or `git-secrets`.

This directory isn't a git repo, so tell me where the repo lives, or paste the output of `git log` and a grep for the key, and I can help rewrite the history. Never paste the secret itself here.
