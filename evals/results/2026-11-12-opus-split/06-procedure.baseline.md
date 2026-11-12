<!-- Q: How do I undo my last git commit but keep the changes? -->

Use `git reset --soft`:

```bash
git reset --soft HEAD~1
```

This removes the last commit but leaves its changes **staged**, ready to recommit.

**Variants:**

- **Keep changes but unstaged:**
  ```bash
  git reset HEAD~1        # same as --mixed, the default
  ```
- **Just fix the last commit** (message or add files) instead of undoing it:
  ```bash
  git add <files>
  git commit --amend
  ```

**Caveat:** If you've already pushed the commit, resetting rewrites history. You'd need `git push --force-with-lease`, which can disrupt anyone else using the branch. For shared branches, use `git revert HEAD` instead. It creates a new commit that undoes the last one without rewriting history, though it doesn't leave the changes in your working tree.

If you reset by mistake, `git reflog` shows the previous commit hash, and you can get back to it with `git reset --hard <hash>`.
