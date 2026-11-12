# LOOP.md — autonomous iteration protocol

This file drives the 20-minute improvement loop. One run = one iteration.
Keep each iteration small enough to finish, verify, commit and push in ~15 minutes.

## Direction (owner, 2026-11-13): measure outputs, verify and prune

Research coverage is saturated: 801 findings reviewed, and recent rounds added about 2 findings each. Improvement now comes from **measuring what brainres actually does to real outputs across many prompts**, then fixing or removing rules based on that.

- **The main instrument is `evals/suite.jsonl`:** 80 prompts, 16 answer types × 5, 32 of them in Korean. Results accumulate across iterations by prompt id, and `combine.py --prompts suite.jsonl` pairs them.
- **Priority order:**
  1. Suite runs.
  2. An information-coverage check, so shorter answers don't drop needed facts.
  3. A per-category weakness report.
  4. Targeted fixes.
  5. Pruning rules that change nothing.
- **Every change to the card or hooks is re-measured** on the affected suite categories, before and after, against a rule stated in advance.
- **Human studies** stay available in `bench/` but are not on the loop's path.

## Iteration steps

0. **Lock check.** If `.loop-lock` exists, another session is mid-build: end this iteration without changes.
1. **Sync.** `cd` to the repo root, then `git pull --rebase --quiet`.
2. **Pick.** Open `BACKLOG.md`. Take the `todo` item with the highest RICE score.
   Ties: lower Effort first, then lower ID.
   If the item is too big for one iteration, split it into sub-items (re-score them), do the first one.
3. **Implement.** Make the change. Ground every new rule in `research/` (cite the concept name + source).
   No rule enters `SKILL.md` without a source in `research/cognitive-principles.md`.
4. **Verify.** Run `bash scripts/validate.sh` and judge it by its **exit status**: run it on its own, or use `set -o pipefail`. Never pipe it into `grep`, because that once let a failing validation through to a push. It must pass. If it fails, fix the cause, not the check. The owner can optionally enforce this with `scripts/install-hooks.sh`, but the loop does not install hooks. A passing validation does not prove the edits ran: a failed edit script must stop the chain before `git commit`, so chain with `&&` or `set -e`. On 2026-11-12, an edit script failed on its first line, validation still passed, and the commit message described docs that weren't in it.
5. **Record.**
   - Mark the backlog item `done` with the date.
   - Add a line to `CHANGELOG.md` under `## Unreleased`.
   - Append one line to `LOOP_LOG.md`: `- YYYY-MM-DD HH:MM · <item id> · <what changed>` (same commit as the change; one commit per iteration).
6. **Ship.** `git add -A && git commit` (conventional message, e.g. `feat(skill): add given-new ordering rule`,
   ending with the `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` line) then `git push origin main`.
   If push is rejected: `git pull --rebase` and push once more. Never force-push.

## Coverage rule

The goal is that **every applicable finding in `research/` is applied** in a skill file.
`python3 scripts/coverage.py --write` shows the gaps. The ratchet in `validate.sh` forbids lowering coverage.
New findings go into `research/catalog-*.md` tables with `ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation`.
A finding marked `No` must state why (not text-applicable, contested, neuromyth, unethical).

## When the backlog has no `todo` items

First, **generate items from measurements.** Read the latest suite results (`combine.py --prompts suite.jsonl` and per-category tables). Find the categories where brainres is worse than baseline, or where both fail, on score, length, information coverage or answer-first. Turn each into a RICE-scored item. Commit + push.

Only if the measurements give nothing new, run a **research round**:

1. Pick 1–2 topics from `research/queue.md`, or one that a measured failure needs grounding for.
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
