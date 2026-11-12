# Changelog

## Unreleased

- Benchmark, step 2 of 3 (B10-2): 24 quiz questions, a "find" question and an "understand" question for each item, each answerable from **both** versions. An independent LLM review passed 22 and flagged 2 for fixes; both are fixed. Its finding that 9 stems or options leaned on brainres wording led to neutral rewrites. Quiz hashes are added to the pre-registration manifest.
- **Regression found (C14):** brainres answers invented confidence numbers in 6 of 36 cases ("~80% likely", "~90% 확신"), against 0 of 36 for the baseline. It is documented in `evals/README.md` and is the top backlog item.

- Human comprehension benchmark, step 1 of 3. `bench/PROTOCOL.md` pre-registers 3 hypotheses (find faster; comprehension non-inferior at a 5 pp margin; better calibration), a counterbalanced within-subject design, n=60, an analysis plan, exclusions and a decision rule. 12 answer pairs are frozen in `bench/items/`, with SHA-256 hashes in `MANIFEST.sha256`.

- `rewrite` mode gets its own procedure in `references/rewrite.md`: inventory the claims and payload, rewrite, mark each item ✓/⚠/✗, then report. This answers the meaning-loss failures of other rewrite skills (humanizer #212, CAVEWOMAN's 51.9% drift).
- `brainlint --compare original rewritten` checks mechanically for numbers, code spans, URLs and negations that a rewrite dropped, and exits 1 when anything is missing. List numbering and trailing URL punctuation are ignored. 4 new tests bring the total to 30.

- Evals final, part 3 of 3 (B09b), with 3 samples per prompt per condition (72 answers): words −27% (per prompt −54, 95% CI −89 to −20), output tokens −16% (CI −179 to −33), Brain Score 91.2 → 96.2 (+5.0, CI +0.8 to +9.2), and 29/36 → 32/36 answers within the length budget. The earlier single-sample claim (−33% words, −24% tokens) is superseded in the READMEs and launch drafts.

- Evals, part 2 of 3 (B09b): baseline now has 3 samples per prompt (n=36). Interim per-prompt result: Brain Score +4.6 (95% CI +0.4 to +8.8), words −54 (CI −89 to −20), output tokens −117 (CI −213 to −22).

- Evals, part 1 of 3 (B09b): runs now record the card hash so card versions never mix, plus a length-budget metric. `evals/combine.py` merges runs and reports SD and a paired 95% CI. Interim result per prompt: Brain Score +4.2 (CI +0.2 to +8.2), words −63 (CI −99 to −27), output tokens −165 (CI −263 to −67).

- Core card v2.1 adds a Korean line to rule 10: 해요체, ≤12 어절, no 번역투. In the eval re-run (4 Korean prompts × 2), answers with long sentences went from 2 of 4 to 0 of 8, and the mean Korean Brain Score went from 89.2 to 93.9. The card cost rose from 418 to 461 tokens (measured), and the READMEs, launch drafts and social image are updated. `evals/run.py` gains `--ids`, `--conditions`, `--samples` and `--tag`.

- First eval harness (`evals/run.py`, 12 prompts × baseline and brainres on Sonnet, tools and MCP off). Median answer length fell from 210 to 140 words (−33%), output tokens fell 24%, and the mean Brain Score rose from 91.6 to 93.5. Claude Code's baseline already had no preambles. Two regressions are documented: Korean sentence length, and brainlint's blind spot on raw length. Results are in `evals/results/`, a summary is in both READMEs, and the launch drafts now carry the measured numbers.
- brainlint ignores HTML comments, which readers never see; a test covers it. Follow-ups: C12 (a Korean line in the card) and B09b (repeated samples).

- Verification round 1 (`research/verification-2026-11.md`) checked 11 citations against primary records.
  - **Verified:** the 5 studies the README leans on most (Cheng 2026 *Science*, Ding 2025 AAAI, Ibrahim 2026 *Nature*, Kim 2024 FAccT, Steyvers 2025), plus Gopstein 2017 and Langhout & Aniche 2021.
  - **Upgraded:** Ashktorab 2019 (EM-110), read in full text, goes from W to M.
  - **Downgraded:** Hales 2017 (PL-14) is an opinion piece, not an experiment. It goes from W–M to W, and the unsupported "n=98" is removed.
  - **Flagged:** Wright & Reid 1973 and Dixon 1982 exist, but their specific results were not located.
  No rule had to be removed.

- brainlint adds 7 line-level checks from craft.md and SKILL.md: `scope_ambiguity` ("all … not"), `bare_this`, `former_latter`, `minimizer` ("simply", "just run", 간단히), `understanding_check` ("does that make sense?"), `emoji` (✓/✗ excluded because they carry meaning), and `boilerplate_warning`. There are now 25 checks in total. No example or README score changed. Trigger and non-trigger tests bring the total to 25.

- 4 new before/after pairs, for 6 in total: concept (DB index), comparison table (SQLite/Postgres/MongoDB), risk numbers (flaky-test cumulative probability, computed), and misconception (incognito). `examples/README.md` indexes them with scores, and all 12 files are pinned as golden cases (23 tests in total).
- brainlint gaps found by the new examples are fixed. "That's an interesting question" now counts as a preamble, and "…is a crucial decision that depends on many factors" now counts as a buried answer. The blind spot that remains is answers with no recommendation, which needs the question; it is documented.

- brainlint v0.2 adds 3 checks:
  - `buried_answer`: the first sentence frames instead of answering ("There are several factors…", "It depends…", "여러 가지…"). It is skipped when a preamble was already penalized.
  - `fragmented_reasoning`: more than 60% of lines are bullets and there are no causal links, in answers of at least 120 words.
  - `term_swap`: curated synonym pairs such as folder/directory and 앱/애플리케이션 appear in the same answer.
  Golden scores are unchanged. 5 new tests bring the total to 23.

- The SKILL.md body drops from 3,893 to 3,309 tokens (−15%, measured). The 35 inline evidence-ID groups moved to `references/rule-sources.md`, which maps each rule to its findings. Coverage stays at 596/596.

- `brainlint --badge <file>` prints a shields.io "Brain Score" badge, so anyone can score their README. Both READMEs carry their own scores, and `validate.sh` fails if a badge goes stale. The English README scores 100 and the Korean one 96; the 96 comes from the deliberately bad hero sentence.
- brainlint fix found while dogfooding: markdown table rows were counted as one giant paragraph. Tables are now excluded from prose checks, and a test covers it (20 tests in total).
- Korean README: the install and evidence sections are restructured into tables and short groups. They had broken our own chunking rule, at 79 → 96.
- `assets/social-preview.png` (1280×640) and its HTML source, for the GitHub social preview and launch posts.

- Opt-in output style `output-styles/brainres.md`, picked with `/output-style`. `keep-coding-instructions` is on. It is generated from the core card by `build_dist.py`, so it can't drift; the stale check covers it.

- brainlint: Korean is now measured as korean.md specifies, with an average of ≤12 어절 and a long-sentence flag above 20. Headings no longer count as sentences, and 2-word labels no longer dilute the average. The Korean "before" example now scores 41 (was 45), because its 22-어절 sentence is flagged. Scores are updated in the READMEs, examples and launch draft. 3 new tests bring the total to 18.
- Backlog tidy: B17 and B18 are marked superseded by the coverage work, and B06 is re-scoped to the scorer.

- `tests/test_brainlint.py`: 15 stdlib tests. Golden scores for the shipped examples (50 / 100 / 45 / 100), every check's trigger and non-trigger, code-block exclusion, and the JSON schema. They run from `validate.sh`. A mutation check (list threshold 5 → 6) confirmed the tests catch regressions.

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
