<!-- Q: How do I undo my last git commit but keep the changes? -->

Use a soft reset:

```bash
git reset --soft HEAD~1
```

This removes the last commit and leaves its changes **staged**, so you can edit and re-commit.

**Variations:**

- **Keep changes but unstage them** (the default "mixed" mode):
  ```bash
  git reset HEAD~1
  ```
- **Just fix the last commit** (message or contents) without undoing it:
  ```bash
  git add <files>        # optional: add more changes
  git commit --amend
  ```

**If you've already pushed the commit**, resetting rewrites history, and you'd need `git push --force-with-lease` afterward. That can disrupt anyone else working on the branch. On a shared branch, use this instead:
```bash
git revert HEAD
```
It creates a new commit that undoes the last one and keeps history intact. It does not keep the changes in your working tree, though.

**If you reset by mistake**, `git reflog` shows the previous commit hash, and `git reset --soft <hash>` restores it.
