<!-- Q: I accidentally pushed my AWS secret key to a public GitHub repo. Help. -->

Rotate the key now. Assume it's already compromised: bots scan public GitHub for AWS keys within seconds to minutes, so deleting the commit does not help on its own.

**Immediate steps:**

1. **Deactivate, then delete the key.** In the AWS console: IAM → Users → (user) → Security credentials → make the key *Inactive*, then delete it. Or from the CLI:
   ```bash
   aws iam update-access-key --access-key-id AKIA... --status Inactive --user-name <user>
   aws iam delete-access-key --access-key-id AKIA... --user-name <user>
   ```
2. **Check CloudTrail for misuse.** Look at events from that access key ID since the push time. Filter by `userIdentity.accessKeyId`. Look for new IAM users, new access keys, EC2 instances in unfamiliar regions, and unusual API calls.
3. **Create a replacement key** and update your apps and CI with it. Don't reuse the old value.
4. **Check the billing dashboard** for unexpected charges. Cryptominers are the common result.

**Cleaning up the repo:**

Removing the file in a new commit is not enough, because the key stays in git history. Options:

- **Rewrite history** with `git filter-repo --path <file> --invert-paths` (or BFG Repo-Cleaner), then force-push. This works, but anyone who cloned the repo still has the key, so the rotation in step 1 is still required.
- **Make the repo private or delete it** if you don't need it public. Forks and caches may still hold copies.
- **Enable GitHub secret scanning** under Settings → Code security, which alerts you on future pushes.

**Prevention:**

- Add `.env` and credential files to `.gitignore`.
- Use `git-secrets` or `gitleaks` as a pre-commit hook.
- Prefer IAM roles or AWS SSO over long-lived access keys.

If you tell me whether the key belonged to a root account, an IAM user, or a CI role, I can narrow down which CloudTrail queries and permission checks matter most.
