<!-- Q: How do I undo my last git commit but keep the changes? -->

This is a general git question, and the working directory isn't a git repository, so I'll answer from git's standard behavior.

To undo the last commit and keep its changes staged, run:

```bash
git reset --soft HEAD~1
```

- `--soft` moves `HEAD` back one commit and leaves the index and working tree untouched, so all the changes stay staged.
- To keep the changes but unstage them, use `git reset HEAD~1` (the default `--mixed` mode).
- To discard the commit and its changes entirely, use `git reset --hard HEAD~1`. This is destructive, so avoid it unless you mean it.

If the commit was already pushed, rewriting it will require a force push, which affects anyone else working on the branch. If you're in a git repo, I can run `git status` and `git log` to check the state before you reset.
