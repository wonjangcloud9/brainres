<!-- Q: How do I undo my last git commit but keep the changes? -->

Run `git reset --soft HEAD~1`. This removes the commit but leaves your changes staged, so you can edit and recommit right away.

If you'd rather have the changes unstaged (still in your working tree, just not staged), use `git reset HEAD~1` (the default `--mixed` mode).

**Avoid `--hard`**, because it discards the changes along with the commit.

If you already pushed the commit, resetting rewrites history, so a push would need `--force-with-lease`. On a shared branch, use `git revert HEAD` instead, which adds a new commit that undoes the old one.

Note that the current directory isn't a git repository, so run this from inside your project folder. Next step: run `git status` afterward to confirm your changes are still there.
