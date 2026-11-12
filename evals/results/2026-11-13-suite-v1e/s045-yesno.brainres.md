<!-- Q: Does git pull overwrite my uncommitted changes? -->

No, `git pull` never silently overwrites uncommitted changes. If the incoming commits touch a file you've modified, git aborts with "Your local changes to the following files would be overwritten by merge" and leaves your work intact.

If the incoming commits touch different files than your edits, the pull succeeds and your changes stay in the working tree.

Untracked files work the same way: git refuses if a pulled file would replace one of yours.

When it aborts, you have three options:

1. `git stash`, then `git pull`, then `git stash pop` keeps your changes and reapplies them on top (may produce conflicts you resolve by hand).
2. `git commit` your work first, then pull (merge or rebase as usual).
3. `git pull --autostash` does the stash and pop in one step. Add `--rebase` if you prefer that.

The only way to lose changes is by explicitly discarding them, e.g. `git reset --hard` or `git checkout -- <file>` after a failed pull.

Next step: run `git status` before pulling to see what's modified, then pick option 1 or 3 if it overlaps with upstream.
