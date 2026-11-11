<!-- Q: How do I undo my last git commit but keep the changes? -->

Use a soft reset:

```
git reset --soft HEAD~1
```

This removes the last commit but leaves all of its changes staged, so you can edit and recommit right away.

Variations:

- **Keep changes unstaged instead:** `git reset HEAD~1` (the default is `--mixed`)
- **Discard the changes entirely (destructive):** `git reset --hard HEAD~1`

If you've already pushed the commit, resetting rewrites history. For a shared branch, prefer `git revert HEAD`, which adds a new commit that undoes the old one without rewriting history. If it's your own branch, you can reset locally and then `git push --force-with-lease`.

If you reset by mistake, `git reflog` shows the previous HEAD, and `git reset --soft <hash>` restores it.

Note that the current working directory isn't a git repository, so run these in your actual project directory.
