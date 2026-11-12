# Changelog

## Unreleased

- Accuracy-cost eval, part 2 (B33b): 15 harder problems on Haiku (`evals/hard15.jsonl`, 30 calls) scored 15/15 in both conditions, with hard items checked by hand. Across all 48 trap and multi-step problems the score is 48/48 with and without brainres, so no accuracy cost is detectable (a ceiling result). The "brevity applies to the final answer" card line was not added, since there is no evidence it's needed. Both READMEs gain an accuracy line.

- Accuracy-cost eval, part 1 (B33a): 15 multi-step word problems on Haiku, with answers computed in Python, 30 calls. Both conditions scored 15/15, so no accuracy cost was observed, but that is a ceiling result. One brainres explanation contained a slip ("Seoul is 9 hours ahead of UTC-8") alongside a correct final answer. `tricky.py` gains a first-sentence-or-last-lines check for multi-step sets. B33b is rescoped to harder problems.

- Research round on LLM-side risk (`research/llm-side-effects.md`). Strict format restrictions degrade LLM reasoning (Tam 2024), and "be concise" prompts trade accuracy for length (Lee 2025). Our evals have shown no accuracy loss on 18 single-step traps, and on Opus brainres moved effort into hidden reasoning. Multi-step problems are untested. New backlog: B33a/B33b (accuracy cost on 30 multi-step problems) and B32 (agentic coding check).

- C16: the refutation rules (SKILL.md, correction.md) now apply only to misconceptions the user stated or implied, and never to opening by knocking down an answer nobody proposed (#52). A new `brainlint --question` check, `preemptive_refutation`, flags sentence-1 openings like "X is wrong." / "X는 틀렸어요" when X isn't in the question. It catches the real Haiku answer from B31b and produces no false positives on the 12 example files. 1 new test.

- B31b: 10 harder prompts on Haiku, covering dates, letter counts, multiplication, Python aliasing, JS sort, pricing and leap years (20 calls). Checked by hand, Haiku answered all 10 correctly in both conditions. After 18 trap prompts, natural errors don't occur often enough to test the LR-01 risk, which would need answers that are wrong by construction. Reasoning visibility with brainres was equal or better. One artifact surfaced: an answer pre-emptively refuted a wrong answer nobody had proposed. This is logged as C16. `tricky.py --set` selects the prompt file.

- LR-01 risk check (B31; `evals/tricky.py`, 8 trap questions on Haiku, 16 calls). The result is inconclusive because both conditions answered all 8 correctly, so the "wrong answer" case never occurred. No hidden reasoning was observed: brainres attached a reason within the first 2 sentences in 4 of 8 answers, against 2 of 8 for the baseline. Tooling lessons: a whole-text regex misjudged correct answers, so correctness is now judged from sentence 1 and was verified by hand. Prompt t8 was contradictory. B31b follows with harder prompts.

- **Process fix.** Commit `a139844` was pushed while `validate.sh` failed on a stale README badge. Validation had been piped into `grep`, which hid its exit status. The English README measurement list was split, bringing its score from 94 back to 100. LOOP.md now says to judge validation by exit status. `scripts/install-hooks.sh` offers an optional pre-commit hook for the owner; the loop doesn't install it.

- Opus token puzzle resolved (B28c; 24 calls, with the thinking/visible split). With brainres, Opus writes less and thinks more. Visible output tokens fell by 308 per prompt (−36%, 95% CI −472 to −144). Hidden reasoning rose by 253 (about 2.6×, borderline CI), so total output is about flat. Pooled over both Opus runs: words −80 (−35%) and Brain Score +3.3 (not significant). The READMEs now say plainly that the bill doesn't shrink on Opus.

- Real-plugin eval (B29): `evals/run.py --conditions plugin` installs the plugin via `--plugin-dir`, with the Skill and Read tools available, and records turns. We ran 12 prompts × 2 against baseline: words −54 per prompt (95% CI −82 to −27) and Brain Score +5.0 (CI +0.0 to +10.0). Both match the card-append proxy (−54, +5.3), so the proxy is validated. The skill was auto-invoked in only 1 of 24 answers (the emergency prompt), so the effect comes from the always-on hooks. `combine.py --treatment` compares any condition.

- Generalization to Opus (B28b; 24 calls): per prompt, words −79 (−34%, 95% CI −117 to −41) and Brain Score +2.9 (CI −1.5 to +7.3, not significant). `output_tokens` rose 19% (CI includes 0) because they include hidden reasoning; one probe showed `thinkingTokens` in `modelUsage`. `run.py` now records `thinking_tokens` and `visible_output_tokens`, and `combine.py` reports visible tokens when available. B28c re-runs Opus with the split.

- Generalization to Haiku (B28a; 24 calls, 12 prompts × 2 conditions): per prompt, words −71 (−35%, 95% CI −114 to −28), Brain Score +3.9 (CI +0.1 to +7.7), output tokens −14% (CI includes 0), and 0 invented confidence numbers. `--question` caught one real slip, an answer that framed before recommending. Opus follows in B28b.

- `brainlint --question` (B27) adds question-aware checks. `yesno_not_first` fires when a yes/no question, including tag questions like "…, right?", doesn't get Yes or No as the first word. `no_recommendation` fires when sentence 1 of a choice question neither names an option nor recommends one. This closes the blind spot documented in `examples/README.md`: 04 "before" now scores 70 and 02 "before" 33, while every "after" stays at 100. Scores without `--question` are unchanged, and the goldens hold. Evals record `score_q` separately, and the playground has an optional question field. 9 new tests bring the total to 43.

- Research round 3 (the backlog was empty). `research/catalog-round3.md` adds 6 findings on how people read LLM answers. One applies as a new rule: when an answer might be wrong, keep the key reasoning visible, because medium-length explanations helped people catch LLM errors (Friedman 2026, LR-01). Another sets an outline-first approach for long deliverables (LR-05). Four are excluded with reasons, including one search-summary claim that the abstract didn't support. The gap is confirmed: no study yet compares bullets and prose for comprehension of chatbot answers. Coverage is 644/644 applicable findings (781 reviewed). New backlog items: B27–B31.

- Reusable GitHub Action (`action.yml`, B20): `uses: wonjangcloud9/brainres@main` scores markdown on every PR, fails below `min-score`, and writes a Brain Score table to the job summary. This repo's CI (`.github/workflows/ci.yml`) runs `validate.sh` and dogfoods the action on both READMEs (min 90). The `build_dist --check` now compares zip entries rather than bytes, so CI on Linux doesn't fail on zlib differences.
- Backlog: B23 (voice rules) is marked superseded, because `references/voice.md` already covers it.

- Research round 2 (C09, `research/catalog-round2.md`): 50 new findings on cross-cultural pragmatics, diagrams, argumentation, news structure and numeracy. Hall's high/low-context framework is excluded for weak validation. The catalog now has 775 findings reviewed, and all 642 applicable ones are applied. New rules:
  - Sentence 1 must be correct on its own (Ecker 2014, Gabielkov 2016).
  - Directness follows the user's own signals, not their nationality.
  - Korean answers keep the content direct and the ending polite, put a regret word inside the refusal sentence, state uncertainty as its own clause, and use 두괄식.
  - Numbers get a verdict and a benchmark, with at most 3 per recommendation. Use "N in 100", never "1 in X".
  - Diagrams must fit the question, have about 7 nodes or fewer, and give each arrow one meaning.
  - Every "not found" says where you looked.
- Two conflicts are resolved. CC-09 ("always add a number to Korean probability words") is reconciled with C14: the number must be grounded, or the answer says what is unverified. The "1 in 4" example in numbers.md becomes "25 in 100".

- Brain Score playground (`playground/index.html`, B21): paste text and get the score and findings in the browser. Instead of a port, it runs the real `brainlint.py` through Pyodide, so the scores can't diverge. Parity is verified: the browser and Python both give 50 with identical findings. The page is generated by `build_dist.py`. `scripts/check_playground.sh` runs as an opt-in network check, and both READMEs link the playground.

- Stress handling (C13, partial). The skill description now names emergencies and distress as triggers, so `support.md` can load. Real-plugin runs, 3 per condition: skill invoked 0/3 → 1/3, answers with ≤5 steps 2/3 → 3/3, Brain Score unchanged within noise. brainlint fixes: numbered steps no longer count as `fragmented_reasoning`, and nested items no longer inflate list length (+2 tests, 34 total). Golden scores are unchanged.

- Interplay with Claude Code's built-in output styles is now measured and documented (B24). `evals/run.py --style` sets the style, using 4 prompts with 1 sample each. With Explanatory, brainres cut words 27%, raised the Brain Score from 92.8 to 98.5, and kept all ★ Insight blocks. With Concise, brainres added 23% words (decision support) at an equal score. Both READMEs recommend Concise alone or `scan` for the shortest answers. Style runs are kept out of `combine.py`.

- Benchmark analysis (B10-4): `bench/analyze.py` is stdlib only. It reads local JSON files or `--from-issues` via `gh`, applies the pre-registered exclusions, and runs paired Wilcoxon and t-interval analyses for H1–H3, a sign test for E1, and the decision rule. 5 tests on simulated participants cover a planted effect, null data, an accuracy drop, exclusions, and an exact Wilcoxon value.
- **Protocol amendment v1.1, before any data:** the same simulation showed the 5 pp non-inferiority margin had only 28–68% power at n = 60, so it is widened to 10 pp (84–99% power). The reason and the simulation table are in PROTOCOL.md.

- Re-measured costs after C14 (`scripts/token_cost.sh`, median of 3): rule card 488 tokens, reminder 84 (was 79), skill body 3,391 (was 3,309). The README tables lose their "re-measure pending" asterisk, and a 20-message session is about 2,200 extra input tokens.

- Benchmark, step 3 of 3 (B10-3): `bench/index.html` is the participant page. It offers English or Korean, puts each participant on counterbalanced list A or B (50/50 versions, unlabeled), randomizes item and option order, and records timed find and understand questions with confidence, an attention check and 2 preference pairs. Results export as JSON. `build_dist.py` generates the page from the frozen items. `validate.sh` runs a headless-Chrome autotest through the whole study. Results are submitted through a GitHub issue form. Next: B10-4 (analysis) and B10-5 (the owner enables Pages and recruits).

- **Fixed the regression (C14):** card rule 8, SKILL rule 9 and numbers.md now forbid invented confidence percentages; numbers are allowed only when grounded (JD-33). A new `brainlint` check, `invented_confidence`, flags self-rated "~80% sure" and "(~90% 확신)" but not confidence intervals or calculations, with tests. Inline code is now treated as a quoted literal, so a README that *mentions* an anti-pattern isn't penalized for it (32 tests in total). The Korean README measurement section is split again after this change pushed it over the paragraph limit. Eval re-run: 7 of 36 answers flagged before the fix, 0 of 24 after, with length gains intact (words −54, CI −88 to −20). The card grew from 461 to 488 tokens. README, launch drafts and the social image are updated.

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
