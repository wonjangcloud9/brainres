<!-- Q: Does git pull overwrite my uncommitted changes? -->

Usually no. Git refuses to overwrite uncommitted changes and aborts instead.

**Cases:**

- **Your modified files don't overlap with files the pull changes:** the pull succeeds and your local edits stay as they are.
- **Your modified files overlap with files the pull changes:** git aborts with an error like `Your local changes to the following files would be overwritten by merge`. Nothing is changed.
- **Untracked files that the pull would create:** git also aborts (`untracked working tree files would be overwritten`).

**Ways to handle the overlap case:**

1. **Stash, pull, reapply** (the usual approach):
   ```
   git stash
   git pull
   git stash pop
   ```
   If the same lines changed, `stash pop` may produce conflicts you resolve by hand. Your stash is kept in that case.

2. **Autostash:**
   ```
   git pull --autostash
   ```
   This does the same thing in one step. Set it permanently with `git config pull.autostash true` (and `rebase.autoStash true` if you use rebase).

3. **Commit first**, then pull. Conflicts then show up as normal merge or rebase conflicts.

**What can lose work:**

- `git reset --hard`, `git checkout -- <file>`, and `git clean -fd` discard uncommitted changes. People often run these to get past the abort error, and they're irreversible for uncommitted work.
- `git pull --force` isn't a thing for this, but `git fetch` + `git reset --hard origin/<branch>` will wipe your changes.

Note that the current directory here isn't a git repo, so there's nothing at risk in this session. The behavior above applies in any repo.
