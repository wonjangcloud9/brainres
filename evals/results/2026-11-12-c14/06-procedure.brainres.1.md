<!-- Q: How do I undo my last git commit but keep the changes? -->

Run `git reset --soft HEAD~1`. This moves the branch back one commit and leaves your changes staged.

Pick the variant based on where you want the changes to end up:

| Command | Changes end up |
|---|---|
| `git reset --soft HEAD~1` | Staged, ready to recommit |
| `git reset HEAD~1` (same as `--mixed`) | Unstaged in your working tree |

**Never use `--hard`**, because it discards the changes.

If you already pushed the commit, resetting rewrites history, so you would need `git push --force-with-lease` and teammates who pulled it will be affected. In that case, `git revert HEAD` is safer because it adds a new commit that undoes the old one.

Note that the current directory (`/private/var/folders/.../tmpx976fho1`) isn't a git repository, so run this from inside your project folder. If you want to check first, `git log --oneline -3` shows the commit you're about to undo.
