<!-- Q: How do I undo my last git commit but keep the changes? -->

Run `git reset --soft HEAD~1` to undo the last commit and keep its changes staged.

- `--soft` moves `HEAD` back one commit and leaves the index and working tree untouched, so the changes stay staged.
- If you want them unstaged instead, use `git reset HEAD~1` (the `--mixed` default). To discard the commit's changes too, use `--hard`, but that deletes them, so avoid it here.

Check the result with `git status` and `git log --oneline -3`.

Note: the working directory isn't a git repository, so run this from inside your repo.
