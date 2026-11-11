<!-- Q: How do I undo my last git commit but keep the changes? -->

Run `git reset --soft HEAD~1`. This removes the commit and leaves your changes staged.

Pick the variant by where you want the changes to end up:

| Command | Changes end up |
|---|---|
| `git reset --soft HEAD~1` | Staged, ready to commit again |
| `git reset HEAD~1` (same as `--mixed`) | In your working tree, unstaged |

Avoid `--hard`, because it **discards** the changes.

If you already pushed the commit, resetting only changes your local branch. Pushing afterward needs `git push --force-with-lease`, and that rewrites shared history. On a shared branch, use `git revert HEAD` instead, which adds a new commit that undoes the old one.

Note that the current directory (`/private/var/folders/.../tmpecdnb6mu`) isn't a git repository, so run the command from inside your project folder.

If you tell me which variant you want and where the repo is, I can run it for you.
