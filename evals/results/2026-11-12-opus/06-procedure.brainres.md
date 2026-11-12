<!-- Q: How do I undo my last git commit but keep the changes? -->

Run `git reset --soft HEAD~1`. It removes the last commit and keeps its changes staged, ready to recommit.

| Command | Commit | Changes end up |
|---|---|---|
| `git reset --soft HEAD~1` | removed | staged |
| `git reset HEAD~1` | removed | unstaged, still in your files |

**Worked example:**

```bash
git log --oneline -2        # confirm which commit you're undoing
git reset --soft HEAD~1     # undo it, keep changes staged
git status                  # changes show as "Changes to be committed"
```

If you just want to fix the message or add a forgotten file, `git commit --amend` is simpler than resetting.

**If you already pushed** that commit, resetting rewrites shared history. You'd need `git push --force-with-lease`, which can disrupt collaborators. On a shared branch, use `git revert HEAD` instead.

Your current directory isn't a git repo, so `cd` into your project first, then run `git log --oneline -2` to check the commit.
