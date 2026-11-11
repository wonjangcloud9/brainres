<!-- Q: How do I undo my last git commit but keep the changes? -->

Run `git reset --soft HEAD~1`. It removes the last commit and leaves your changes staged.

Pick the variant based on where you want the changes to end up:

| Command | Changes end up |
|---|---|
| `git reset --soft HEAD~1` | Staged, ready to recommit |
| `git reset HEAD~1` (mixed, the default) | In your working directory, unstaged |

Both keep your file edits. Avoid `--hard`, because it **discards** the changes.

If you already pushed the commit, resetting rewrites history, so a push then needs `--force-with-lease`. On a shared branch, use `git revert HEAD` instead, which adds a new commit that undoes the old one.

If you reset by mistake, `git reflog` shows the old commit hash, and `git reset --soft <hash>` brings it back.

Note that the current working directory here is not a git repository, so run the command from inside your repo.
