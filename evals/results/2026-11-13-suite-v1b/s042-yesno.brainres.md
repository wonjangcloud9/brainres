<!-- Q: Is it safe to commit my .env file with API keys to a private repo? -->

No, it's not safe: a private repo limits who can read the keys, but it doesn't protect them.

- **Wider access than you expect:** every collaborator, CI system, and connected app can read them, and so can anyone who gains access later.
- **Git history is permanent:** deleting `.env` in a later commit leaves the keys in old commits and in every clone.
- **Privacy can change:** one visibility toggle or a fork can make the repo public, and bots scrape new public repos for keys within minutes.
- **Leaks spread:** keys can end up in logs, backups, or screenshots.

Instead:

1. Add `.env` to `.gitignore` before the first commit.
2. Commit a `.env.example` with variable names and fake values.
3. Keep real values in a secret manager or in your CI's secrets store.
4. Turn on secret scanning (GitHub push protection or `gitleaks`).

If you already committed a `.env`, **rotate the keys first**. Cleaning history with `git filter-repo` comes second, because the old keys may already be copied elsewhere.

This directory isn't a git repo yet, so I can create the `.gitignore` and `.env.example` now if you want.
