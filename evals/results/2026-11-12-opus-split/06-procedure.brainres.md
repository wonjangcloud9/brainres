<!-- Q: How do I undo my last git commit but keep the changes? -->

Run `git reset --soft HEAD~1`. It removes the last commit and leaves its changes staged, ready to recommit.

```bash
git reset --soft HEAD~1
```

**Variants**

| Command | Commit | Changes end up |
|---|---|---|
| `git reset --soft HEAD~1` | removed | staged |
| `git reset HEAD~1` (default `--mixed`) | removed | unstaged, still in your files |
| `git reset --hard HEAD~1` | removed | **deleted** |

Avoid `--hard` here, because it discards the changes you want to keep.

**If you already pushed the commit:** resetting rewrites history, so collaborators who pulled it will diverge. Use `git revert HEAD` instead, which adds a new commit that undoes the old one.

**If you only want to fix the commit message or add a file:** skip the reset. Stage the fix and run `git commit --amend`.

Your current directory isn't a git repository, so `cd` into your project first, then run `git log --oneline -3` to confirm which commit you're undoing.
