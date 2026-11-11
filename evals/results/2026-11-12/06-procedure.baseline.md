<!-- Q: How do I undo my last git commit but keep the changes? -->

Use a soft reset:

```
git reset --soft HEAD~1
```

This removes the last commit but leaves all its changes staged, so you can edit them and recommit.

Variants:

- **Keep changes unstaged** (working tree only):
  ```
  git reset HEAD~1
  ```
  (a mixed reset, which is the default)

- **Discard the changes entirely** (destructive, so be careful):
  ```
  git reset --hard HEAD~1
  ```

Notes:

- If you've already pushed the commit, rewriting history requires a force push (`git push --force-with-lease`). Avoid this on shared branches; use `git revert HEAD` instead, which creates a new commit that undoes the old one.
- If you only want to change the commit message, use `git commit --amend`.
- If you reset by mistake, `git reflog` shows the previous HEAD so you can recover with `git reset --soft <hash>`.

Also, the current directory isn't a git repository, so run these from inside your actual repo.
