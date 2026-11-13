# brainres 0.2.0: release notes (owner publishes)

**How to release** (about 3 minutes):

1. `claude plugin tag --push .` creates and pushes the tag `brainres--v0.2.0`. It also checks that plugin.json and the marketplace entry agree.
2. On GitHub, go to **Releases → Draft a new release**, pick that tag, and paste the text below.
3. Optional: tick **Publish this Action to the GitHub Marketplace**. This is the README-scoring Action (`action.yml`); the first time, you'll be asked to accept the Marketplace agreement and use 2FA.

---

## brainres 0.2.0

Claude answers your brain can actually read, now measured on 80 prompts.

**Measured** (Sonnet, 78 valid pairs, 16 answer types, 32 prompts in Korean):

- Answers are 29% shorter.
- Visible output tokens fall 28%.
- Brain Score rises 4.6 points (95% CI +3.3 to +6.0).
- brainres leads in 14 of 16 answer types.
- **The cost:** blinded key-fact checks found 1.8 pp less detail; facts are rarely dropped. Haiku shows the same length effect (−27%).

**New:**

- **Situation lines:** a learner signal gets "fix their own line, end with a predict-first question", which moved learner endings from 0/8 to 8/8. An emergency signal gets "next action first", which raised action-first answers from 65% to 89% at about 4 pp of detail.
- **The always-on per-message reminder is now Haiku-only.** On Sonnet it changed nothing over 7 turns or about 30k tokens, so it was removed there. On Haiku it adds 4–6 points.
- **One-line install for Codex, Cursor and other agents:** `npx skills add wonjangcloud9/brainres`.
- **brainlint fixes, each backed by evidence:** short bold labels are no longer penalised, step lists no longer count as walls of text, and the Korean bold limit is scaled like the other Korean limits.
- **Eval tooling:** an 80-prompt suite, a blinded key-fact coverage judge, card ablation, multi-turn and latency harnesses, and a clean-install check.

**Known limits:** comprehension with human readers is not measured yet. The card makes Sonnet think in about 40% of answers, so the first visible text arrives about 0.5 s later, and total time is unchanged.

Full list: [CHANGELOG](../CHANGELOG.md#020--2026-11-13).
