<!-- Q: How do I undo my last git commit but keep the changes? -->

Run:

```
git reset --soft HEAD~1
```

This removes the last commit but leaves all its changes staged, so you can recommit right away or adjust first.

Variants:

- `git reset HEAD~1` (the default, `--mixed`): undoes the commit and unstages the changes, but keeps them in your working directory.
- `git reset --hard HEAD~1`: **discards** the changes entirely. Don't use this if you want to keep them.

Notes:

- If you've already pushed the commit, resetting rewrites history. You'd need `git push --force-with-lease` afterward, which is only safe on branches no one else is using. On shared branches, use `git revert HEAD` instead, which adds a new commit that undoes the old one.
- If you make a mistake, `git reflog` shows the previous HEAD, and `git reset --soft <hash>` restores it.

Note that the current working directory isn't a git repository, so run these in your actual project folder.
