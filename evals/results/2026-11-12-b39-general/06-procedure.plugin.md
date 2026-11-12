<!-- Q: How do I undo my last git commit but keep the changes? -->

Run `git reset --soft HEAD~1`. It removes the last commit and leaves your changes staged.

Pick the variant that fits what you want:

| Command | Changes end up |
|---|---|
| `git reset --soft HEAD~1` | Staged, ready to re-commit |
| `git reset HEAD~1` (mixed, the default) | Unstaged, still in your files |
| `git reset --hard HEAD~1` | **Deleted**. Don't use this if you want to keep them. |

Example: you committed with a typo in the message. Run `git reset --soft HEAD~1`, then `git commit -m "corrected message"`. The files stay the same.

If you already pushed the commit, resetting rewrites history. Teammates who pulled it will be out of sync, so use `git revert HEAD` instead. It adds a new commit that undoes the old one.

Next step: run `git status` after the reset to confirm your changes are still there.
