<!-- Q: How do I undo my last git commit but keep the changes? -->

Run `git reset --soft HEAD~1`, which removes the commit but leaves your changes staged.

Pick the variant that matches how you want the changes left:

| Command | Changes end up |
|---|---|
| `git reset --soft HEAD~1` | Staged, ready to recommit |
| `git reset HEAD~1` (same as `--mixed`) | Unstaged, still in your files |
| `git reset --hard HEAD~1` | **Deleted**, so don't use this to keep changes |

Two cautions:

- If you already pushed the commit, resetting rewrites history. You would need `git push --force-with-lease`, which affects anyone who pulled it. Use `git revert HEAD` instead for shared branches.
- If you reset by mistake, `git reflog` shows the old commit hash, and `git reset --soft <hash>` restores it.

Note that the current directory isn't a git repository, so run this inside your project folder.
