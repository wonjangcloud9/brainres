<!-- Q: How do I undo my last git commit but keep the changes? -->

Run `git reset --soft HEAD~1`. This removes the commit but leaves your changes staged.

If you'd rather have the changes unstaged (still in your working tree), use the default mixed reset instead:

```
git reset HEAD~1
```

**Do not use `--hard`**: it deletes the changes along with the commit.

If you already pushed the commit, resetting only changes your local branch. You would need `git push --force-with-lease` to update the remote, and that rewrites shared history, so use `git revert HEAD` instead if others may have pulled it.

Note that the current directory here (`/private/var/folders/.../tmpx976fho1`) isn't a git repository, so run the command inside your actual project folder. Next step: `cd` into your repo and run `git reset --soft HEAD~1`, then check with `git status`.
