# LOOP.md — autonomous iteration protocol

This file drives the 20-minute improvement loop. One run = one iteration.
Keep each iteration small enough to finish, verify, commit and push in ~15 minutes.

## Iteration steps

0. **Lock check.** If `.loop-lock` exists, another session is mid-build: end this iteration without changes.
1. **Sync.** `cd` to the repo root, then `git pull --rebase --quiet`.
2. **Pick.** Open `BACKLOG.md`. Take the `todo` item with the highest RICE score.
   Ties: lower Effort first, then lower ID.
   If the item is too big for one iteration, split it into sub-items (re-score them), do the first one.
3. **Implement.** Make the change. Ground every new rule in `research/` (cite the concept name + source).
   No rule enters `SKILL.md` without a source in `research/cognitive-principles.md`.
4. **Verify.** Run `bash scripts/validate.sh`. It must pass. If it fails, fix the cause, not the check.
5. **Record.**
   - Mark the backlog item `done` with the date.
   - Add a line to `CHANGELOG.md` under `## Unreleased`.
   - Append one line to `LOOP_LOG.md`: `- YYYY-MM-DD HH:MM · <item id> · <what changed>` (same commit as the change; one commit per iteration).
6. **Ship.** `git add -A && git commit` (conventional message, e.g. `feat(skill): add given-new ordering rule`,
   ending with the `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` line) then `git push origin main`.
   If push is rejected: `git pull --rebase` and push once more. Never force-push.

## When the backlog has no `todo` items

Run a **research round** instead of an implementation round:

1. Pick 1–2 topics from `research/queue.md` (or find new ones: new trending output-style skills,
   new cognitive-science findings, user feedback in GitHub issues via `gh issue list`).
2. Write findings into `research/` (new file or append), with sources and evidence strength.
3. Turn findings into new backlog items, each scored with RICE (see below). Commit + push.

## RICE scoring (used in BACKLOG.md)

`score = Reach × Impact × Confidence ÷ Effort`

| Factor | Scale |
|---|---|
| Reach | share of Claude answers affected: 10 = every answer, 5 = most, 2 = some types, 1 = rare |
| Impact | comprehension gain per affected answer: 3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal |
| Confidence | evidence strength: 1.0 = meta-analysis / well replicated, 0.8 = solid, 0.5 = plausible, 0.3 = speculative |
| Effort | iterations needed: 0.5, 1, 2, 3 … |

Virality / growth items (README, demos, install UX, launch drafts) use the same formula with
Reach = share of potential users who would notice, Impact = effect on stars/adoption.
Keep roughly 1 growth item in every 3–4 iterations.

## Guardrails

- **Token budget.** `skills/brainres/SKILL.md` must stay under the limit in `scripts/validate.sh`.
  This skill teaches efficiency — it must be efficient itself. Move depth into `references/`.
- **Evidence over vibes.** Flag neuromyths; never cite learning styles, left/right brain, 10% brain, etc. as support.
- **Nothing outward-facing beyond this repo.** Push to `origin main` only. Do not post to social media,
  open PRs/issues on other repos, or create new repos. Launch posts are drafted in `launch/` for the owner to post.
- **No personal data** in any file or commit message.
- **Do not delete** research or examples to make validation pass.
- **Eval budget.** Any `claude -p` evaluation run: at most 30 calls per iteration, prefer `--model sonnet`.
- If something is blocked (auth failure, repeated push failure), write it in `LOOP_LOG.md` and stop that iteration.
