# Changelog

## Unreleased

- Coverage ledger (`scripts/coverage.py`, `research/coverage.md`): every catalogued finding is applied in a skill file or excluded with a reason; validate.sh ratchets the count.
- Situation router + 9 reference files (explain, decide, numbers, code, procedure, learn, correction, long-form, voice). The original catalog is at 87/87 applicable findings applied.

- Per-turn reminder hook (UserPromptSubmit, 238 chars ≈ 60 tokens) so the rules hold across long sessions. Same opt-out as the session hook.

## 0.1.0 — 2026-11-12

- Core skill `brainres`: 10 evidence-linked rules, reader-expertise adaptation, explanation patterns, payload protection, modes (scan, learn, rewrite, score, off).
- Always-on: SessionStart hook injects a ~350-token core card (opt out with `BRAINRES=off` or `~/.claude/brainres.off`).
- `brainlint` v0.1: dependency-free readability scorer for English and Korean, each check mapped to a cognitive-science finding.
- Research: 90-concept cognitive-principles catalog with evidence grades; survey of trending output-style skills.
- Two before/after examples (EN debugging, KO decision).
