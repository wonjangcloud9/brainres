<!-- Q: How do I undo my last git commit but keep the changes? -->

Run:

```bash
git reset --soft HEAD~1
```

This removes the last commit but leaves all its changes staged, so you can edit and recommit.

Variants:

- **Keep changes unstaged:** `git reset HEAD~1` (the default `--mixed`)
- **Discard the changes entirely:** `git reset --hard HEAD~1` (destructive, so avoid it if you want to keep your work)

If you've already pushed the commit, resetting rewrites history. You'd need `git push --force-with-lease` afterward, which can affect collaborators. In that case, `git revert HEAD` is safer because it adds a new commit that undoes the change without rewriting history.

Note that the current working directory isn't a git repository, so run these in your actual project folder.
