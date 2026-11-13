<!-- Q: I accidentally pushed my AWS secret key to a public GitHub repo. Help. -->

# Revoke the key now, before cleaning anything up

Bots scrape GitHub for AWS keys within minutes. Deleting the commit won't help, because the key is already compromised. Your first job is to make the key useless.

## 1. Deactivate the key (do this first)

**Console:** IAM → Users → (the user) → Security credentials → Access keys → **Deactivate**, then **Delete**.

**CLI** (using a *different*, still-valid credential):
```bash
aws iam update-access-key --user-name <USER> --access-key-id <AKIA...> --status Inactive
aws iam delete-access-key --user-name <USER> --access-key-id <AKIA...>
```

If the key belongs to the **root account**, delete it and make sure MFA is on for root. If production depends on the key, create a replacement first, but don't let that delay revoking the leaked one.

## 2. Check for damage

- **Your email and AWS Support cases.** AWS often detects leaked keys and may have attached the `AWSCompromisedKeyQuarantine` policy. If they opened a support case, follow its steps.
- **CloudTrail:** see what the key did. IAM events are in `us-east-1`; check your other regions too.
  ```bash
  aws cloudtrail lookup-events --region us-east-1 \
    --lookup-attributes AttributeKey=AccessKeyId,AttributeValue=<AKIA...>
  ```
- **Things attackers commonly create:**
  - New IAM users, roles, or access keys (the most important check, since they let attackers keep access after you revoke the leaked key)
  - EC2 instances or GPUs for crypto mining, in **every region**
  - Lambda functions
  - Activity in S3, SES, or SageMaker
- **Billing:** look for unexpected charges. If you find any, open a support case. AWS frequently waives charges caused by a compromise.

## 3. Scrub the repo (secondary)

```bash
# with git-filter-repo (brew install git-filter-repo)
git filter-repo --replace-text <(echo '<THE_SECRET_KEY>==>REDACTED')
git push --force --all
```

This won't remove the key from forks, clones, or GitHub's cached views. For those, contact GitHub Support. This is also why step 1 is the step that actually protects you.

## 4. Prevent a repeat

- Add credential files (`.env`, etc.) to `.gitignore`.
- Turn on **GitHub push protection** (Settings → Code security).
- Add a pre-commit scanner such as `gitleaks` or `git-secrets`.
- Prefer short-lived credentials (IAM Identity Center/SSO, roles, OIDC for CI) over long-lived access keys.

---

I can help hands-on. If you have the AWS CLI set up with another credential, I can run the CloudTrail and resource checks across all regions. If you point me at the repo (the current directory isn't it), I can scrub the history. **Have you deactivated the key yet?**
