<!-- Q: I accidentally force-pushed to main and overwrote my teammate's last 3 commits. Help! -->

Yes, the commits are almost certainly recoverable, because Git keeps the old objects, and you need the SHA of the old `main` tip to restore them.

Your current directory isn't a git repo, so I can't look yet. Run these in your clone, or tell me the repo path and I'll do it.

1. **Find the old tip in your reflog.** If you fetched before pushing, your remote-tracking ref remembers it:
   ```
   git reflog show origin/main
   ```
   The entry just before your push is the old tip. If that's empty, try `git reflog` and look for the last `pull` or `fetch` entry.

2. **Check it holds the 3 lost commits:**
   ```
   git log --oneline <old-sha> -5
   ```

3. **If your reflog doesn't have it, use another source:**
   - Your teammate's clone still has it. `git log origin/main` or `git reflog` on their machine shows the SHA, unless they have fetched since.
   - On GitHub, the repo's Activity view (Code tab, "Activity") lists the force push with before and after SHAs.
   - CI runs for those commits also show the SHAs.

4. **Restore main.** Tell your team first, because this rewrites `main` again. Then:
   ```
   git push --force-with-lease origin <old-sha>:main
   ```
   This puts `main` back exactly as it was. If you also had new commits you wanted to keep, instead create a branch from `<old-sha>`, cherry-pick your commits onto it, and push that.

5. **Have your teammate run `git fetch && git status`.** If they had already pulled your overwritten `main`, they should reset or rebase onto the restored one.

**Warning:** don't run `git gc --prune=now` before restoring, since that can delete the lost objects locally.

Send me the output of `git reflog show origin/main` and I'll pick out the right SHA with you.
