<!-- Q: Is it safe to commit my .env file with API keys to a private repo? -->

No, because a private repo limits who can read it today, but not who can read it later, and git history keeps the keys even after you delete the file.

**Why it fails in practice**
- Every collaborator, CI runner, and connected app with repo access gets the keys.
- Making the repo public by mistake, or a leaked clone or backup, exposes every key in the history.
- Deleting `.env` in a later commit doesn't remove it from earlier commits.

**What to do instead**
1. Add `.env` to `.gitignore` before the first commit.
2. Commit a `.env.example` with the variable names and empty values.
3. Store real values in your host's secret store (GitHub Actions secrets, Vercel/Fly env settings, AWS Secrets Manager, etc.).

**If `.env` is already committed:** rotate every key in it first, because rewriting history doesn't help if anyone has already cloned. Then remove the file from history with `git filter-repo --path .env --invert-paths` and force-push.

This directory isn't a git repo yet, so you can still set up `.gitignore` before your first commit. Want me to create the `.gitignore` and a `.env.example` from your current `.env`?
