<!-- Q: How do I undo my last git commit but keep the changes? -->

Run `git reset --soft HEAD~1`. It removes the commit and leaves your changes staged.

If you'd rather have the changes unstaged, use `git reset HEAD~1` (the default mixed mode).

Two cautions:
- **Don't use `--hard`**, because it deletes your changes.
- If you already pushed the commit, resetting rewrites history, so you'd need `git push --force-with-lease`. Skip that on shared branches and use `git revert HEAD` instead.

Next step: run `git status` to confirm your changes are still there.
