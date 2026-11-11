# Changelog

## Unreleased

- Portable builds in `dist/` from one source (`scripts/build_dist.py`, deterministic): `system-prompt.md` for any LLM (fits ChatGPT custom instructions), `AGENTS.md`, Cursor rule `cursor/brainres.mdc`, and `brainres-skill.zip` for claude.ai. `validate.sh` fails if `dist/` is stale.

- Core card v2: 11 lines chosen by RICE across all 725 findings (`research/core-card-ranking.md`); 631 → 418 tokens (−34%, measured). Situation-only rules (clarifying questions, headings, stress mode, Korean) stay in the skill. `validate.sh` caps the card at 1,350 chars.

- Measured prompt cost with Claude's tokenizer (`scripts/token_cost.sh`): rule card 631 tokens per session, reminder 79 per message, full skill 3,893 when invoked. Earlier README estimates (~450 / ~60) are corrected.

- `launch/`: drafts for Show HN, an X thread, GeekNews (Korean) and r/ClaudeAI, plus a pre-posting checklist. These are for the owner to post; the loop never posts.

- **Full-coverage program:** 6 new domain catalogs bring the total to 725 reviewed findings. All 596 applicable findings are cited by a rule (100%); 129 are excluded with a reason (not text-applicable, failed replication, neuromyth, manipulative, or duplicate).
- New rule set "Honest, not agreeable" (anti-sycophancy, premise checks, no flattery, "I'd do X because Y") in SKILL.md and the always-on card.
- 4 new reference files: `support.md` (distress, worry, emergencies), `accessibility.md` (dyslexia, ADHD, autism, aphasia, older readers, screen readers), `korean.md` (Korean output and L2 readers), `craft.md` (line-level psycholinguistics). All 9 existing references expanded.
- 19 new neuromyths documented (e.g. "23 minutes to refocus", glucose willpower, word-shape reading).

- `README.ko.md`: Korean README with a Korean before/after hero (45 → 100), linked from the English README.

- Coverage ledger (`scripts/coverage.py`, `research/coverage.md`): every catalogued finding is applied in a skill file or excluded with a reason; validate.sh ratchets the count.
- Situation router + 9 reference files (explain, decide, numbers, code, procedure, learn, correction, long-form, voice). The original catalog is at 87/87 applicable findings applied.

- Per-turn reminder hook (UserPromptSubmit, 238 chars ≈ 60 tokens) so the rules hold across long sessions. Same opt-out as the session hook.

## 0.1.0 — 2026-11-12

- Core skill `brainres`: 10 evidence-linked rules, reader-expertise adaptation, explanation patterns, payload protection, modes (scan, learn, rewrite, score, off).
- Always-on: SessionStart hook injects a ~350-token core card (opt out with `BRAINRES=off` or `~/.claude/brainres.off`).
- `brainlint` v0.1: dependency-free readability scorer for English and Korean, each check mapped to a cognitive-science finding.
- Research: 90-concept cognitive-principles catalog with evidence grades; survey of trending output-style skills.
- Two before/after examples (EN debugging, KO decision).
