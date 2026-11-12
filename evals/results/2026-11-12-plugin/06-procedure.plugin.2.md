<!-- Q: How do I undo my last git commit but keep the changes? -->

Run `git reset --soft HEAD~1`. It removes the commit and leaves your changes staged.

If you'd rather have them unstaged (still in your working directory), use `git reset HEAD~1`. This is the same as `--mixed`, which is the default.

**Don't use `--hard`**, because it deletes the changes.

If you already pushed the commit, resetting rewrites history. In that case, `git revert HEAD` is safer because it adds a new commit that undoes the old one.

Next step: run `git status` to confirm your changes are still there.
