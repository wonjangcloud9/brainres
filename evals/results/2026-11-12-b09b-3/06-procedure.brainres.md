<!-- Q: How do I undo my last git commit but keep the changes? -->

Run `git reset --soft HEAD~1`. It removes the last commit and leaves all its changes staged.

If you'd rather have the changes unstaged (still in your working tree, just not staged for commit), use:

```
git reset HEAD~1
```

(This is the same as `--mixed`, the default.)

**Don't use `--hard`**, because it deletes the changes.

If you already pushed the commit, resetting rewrites history, so you'd need `git push --force-with-lease` afterward. On a shared branch, use `git revert HEAD` instead, which adds a new commit that undoes the old one.

Note that the current directory isn't a git repository, so run this from inside your repo.
