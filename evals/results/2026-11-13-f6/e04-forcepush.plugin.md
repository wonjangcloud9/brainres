<!-- Q: I accidentally force-pushed to main and overwrote my teammate's last 3 commits. Help! -->

**Next action: don't push anything else, and ask your teammate to run `git log origin/main..main` (or just `git log -3`) in their clone.** Their local `main` still has the 3 commits unless they've pulled since your push.

Force-pushing only moves the branch pointer. The commits still exist, so you can get them back from any of these places:

1. **Teammate's clone (easiest).** They run `git push origin main:recovery`. This is a normal push to a new branch, so it overwrites nothing.
2. **Your reflog.** If you fetched before the push, `git reflog show origin/main` lists the old SHA. Then run `git push origin <old-sha>:refs/heads/recovery`.
3. **GitHub.** If you have no clone with the commits, the repo's Activity view shows the force-push with its "before" SHA. You can also run `gh api repos/OWNER/REPO/events` and look for the `before` field on the PushEvent. Push that SHA to `recovery` as in step 2.

Once the commits are on `recovery`, restore `main` in one of two ways:

- **Your push had nothing worth keeping:** run `git push --force-with-lease origin recovery:main`.
- **Your push had good commits too:** run `git switch main`, then `git rebase recovery` (or `git cherry-pick` your commits onto it), then `git push --force-with-lease origin main`.

Tell the team before resetting `main`, so nobody pulls the wrong history in between. Anyone who already pulled your version will need `git fetch && git reset --hard origin/main`, so check that they have nothing unpushed first.

To prevent a repeat, turn on branch protection for `main` and disallow force pushes (GitHub: Settings → Branches). Use `--force-with-lease` instead of `--force` from now on.

If you tell me which of the three sources you have, I can give you the exact commands.
