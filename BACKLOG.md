# Backlog (RICE-ordered)

`score = Reach × Impact × Confidence ÷ Effort`. See [LOOP.md](LOOP.md) for scales.
Type: **Q** = answer quality · **T** = tooling/eval · **G** = growth/virality.
The loop always takes the highest-scoring `todo` item.

| ID | Item | Type | R | I | C | E | Score | Status |
|---|---|---|---|---|---|---|---|---|
| C13 | Stress prompt (eval 11) still bullet-heavy (82): check support.md stress mode reaches answers; consider a 1-line stress rule in the card | Q | 2 | 2 | 0.5 | 0.5 | **4** | todo |
| C09 | Research round 2: new domains (cross-cultural pragmatics, diagram cognition — Larkin & Simon, argumentation/Toulmin, journalism inverted-pyramid studies, numeracy individual differences) | Q | 5 | 1 | 0.5 | 1 | **2.5** | todo |
| C01 | **Full-coverage program.** Ingest the 6 domain catalogs (psycholinguistics, learning science, attention & neuro, judgment & trust, HCI & info design, emotion & pragmatics) into `research/catalog-*.md` with Applies/Situation columns | Q | 10 | 3 | 0.8 | 1 | **24** | done 2026-11-12 |
| C02 | Situation router in SKILL.md + one `references/<situation>.md` per situation, so every applicable finding has a home without bloating the always-on card | Q | 10 | 3 | 0.8 | 1 | **24** | done 2026-11-12 |
| C03 | Close **core** coverage gaps (see `research/coverage.md` → "Not yet applied", situation=core) | Q | 10 | 3 | 0.8 | 1 | **24** | done 2026-11-12 (596/596) |
| C04 | Close **explain / long-form / learn** coverage gaps | Q | 5 | 3 | 0.8 | 1 | **12** | done 2026-11-12 (596/596) |
| C05 | Close **decide / numbers / correction / procedure / code / voice** coverage gaps | Q | 5 | 3 | 0.8 | 1 | **12** | done 2026-11-12 (596/596) |
| C06 | Coverage badge in README ("N findings reviewed · X% applied") + explain the ledger | G | 8 | 2 | 1.0 | 0.5 | **32** | done 2026-11-12 |
| B17 | `references/learn.md`: prequestion → worked example with fading → retrieval checks | Q | 2 | 2 | 1.0 | 0.5 | 8 | superseded by C04 (learn.md covers it) |
| B18 | `references/uncertainty.md` | Q | 5 | 1 | 0.8 | 0.5 | 8 | superseded by C05 (numbers.md + rule 9) |
| B10-5 | **Owner:** enable GitHub Pages (Settings → Pages → main, root) and recruit ~60 participants (README/launch posts link the benchmark) | G | 10 | 3 | 0.5 | 1 | **15** | needs owner |
| B21 | Web playground (GitHub Pages): paste text → Brain Score (brainlint port to JS) | G | 8 | 2 | 0.5 | 2 | **4** | todo |
| B23 | Voice-mode rules (transient information effect, #9) | Q | 1 | 1 | 0.8 | 0.5 | **1.6** | todo |
| B20 | GitHub Action: brainlint on docs in PRs | T | 2 | 1 | 0.5 | 1 | **1** | todo |
| B07 | `README.ko.md` for Korean devs (GeekNews, Korean X) | G | 5 | 2 | 0.8 | 0.5 | 16 | done 2026-11-12 |
| B14 | Launch drafts in `launch/`: Show HN, X thread, GeekNews, r/ClaudeAI. Owner posts them | G | 8 | 2 | 0.5 | 0.5 | 16 | done 2026-11-12 |
| B25 | Measure and publish the token cost of the core card and reminder in the README (honest numbers) | G | 8 | 1 | 1.0 | 0.5 | 16 | done 2026-11-12 (card 631, reminder 79, skill 3,893 tokens) |
| C10 | Condensed core card v2: re-rank always-on rules by RICE across all 725 findings (currently 631 tokens measured; target ≤500) | Q | 10 | 2 | 0.8 | 1 | 16 | done 2026-11-12 (631 → 418 tokens) |
| B19 | Portable builds: `dist/system-prompt.md` (any LLM), AGENTS.md / Cursor rule, claude.ai skill zip | G | 8 | 2 | 0.8 | 1 | 12.8 | done 2026-11-12 |
| B12 | brainlint golden tests (`tests/`), run from validate.sh | T | 5 | 1 | 1.0 | 0.5 | 10 | done 2026-11-12 (15 tests) |
| B06 | brainlint: Korean sentence splitter + 어절-based long-sentence check (korean.md rules already shipped) | T | 5 | 1 | 0.8 | 0.5 | 8 | done 2026-11-12 |
| B08 | Opt-in output style `output-styles/brainres.md` for people who want it as their style | Q | 5 | 1 | 0.8 | 0.5 | 8 | done 2026-11-12 |
| B22 | Social preview image + "Brain Score" badge for READMEs | G | 8 | 1 | 0.5 | 0.5 | 8 | done 2026-11-12 |
| B26 | Trim SKILL.md token cost (3,893 measured): compact ID citations (e.g. one trailing cite line per rule) without losing coverage | Q | 5 | 1 | 0.8 | 0.5 | 8 | done 2026-11-12 (3,893 → 3,309 tokens) |
| B11 | brainlint v0.2: answer-first detection beyond preamble regex, causal-connective loss in bullets, term-swap detection | T | 10 | 1 | 0.8 | 1 | 8 | done 2026-11-12 |
| B13 | 4 more before/after examples: concept explanation, comparison table, risk numbers, misconception refutation | G | 10 | 1 | 0.8 | 1 | 8 | done 2026-11-12 (6 pairs) |
| C07 | brainlint v0.2: deterministic checks for new line-level rules — "all…not", bare "This", "former/latter", "simply/just/obviously", "great question", "Does that make sense?", emoji in technical answers, warning boilerplate | T | 10 | 1 | 0.8 | 1 | 8 | done 2026-11-12 |
| C08 | Research round 2: re-verify every W/C citation flagged "unverified" in the catalogs; up/downgrade grades | Q | 10 | 1 | 0.8 | 1 | 8 | done 2026-11-12 (11 checked: 9 verified, 1 upgraded, 1 downgraded) |
| B09 | Eval harness: 12 prompts × {baseline, brainres} via `claude -p`; report brainlint score, words, answer-in-sentence-1 rate | T | 10 | 2 | 0.8 | 2 | 8 | done 2026-11-12 (first run: −33% words, −24% tokens, score 91.6→93.5) |
| C12 | Korean line in the core card (eval 09: Korean answers exceed 어절 limits; card has no Korean rule) — keep card ≤1,350 chars | Q | 5 | 1 | 0.8 | 0.5 | 8 | done 2026-11-12 (KO long-sentence answers 2/4 → 0/8; card 418 → 461 tokens) |
| B09b | Re-run evals with 3 samples per prompt (variance) and a length-aware score; publish deltas with ranges | T | 8 | 1 | 0.8 | 1 | 6.4 | B09b-1 done 2026-11-12 (harness: card_sha, length budget, combine.py; brainres ×2) — split into B09b-2/3 |
| B09b-2 | Evals: 2 more baseline samples (24 calls) | T | 8 | 1 | 0.8 | 1 | 6.4 | done 2026-11-12 (baseline n=36) |
| B09b-3 | Evals: 1 more brainres sample (12 calls) + final combined report in READMEs | T | 8 | 1 | 0.8 | 1 | 6.4 | done 2026-11-12 (n=36 each: words −27%, tokens −16%, score +5.0 [+0.8,+9.2]) |
| B16 | `references/rewrite.md`: claim inventory → rewrite → lost-claim check (humanizer v3 lesson) | Q | 2 | 2 | 0.8 | 0.5 | 6.4 | done 2026-11-12 (+ brainlint --compare) |
| B10 | Human comprehension benchmark protocol: quiz + time-to-answer on paired answers. Nobody else measures this | T | 10 | 3 | 0.5 | 3 | 5 | B10-1 done 2026-11-12 (protocol + frozen items) — split into B10-2/3 |
| B10-2 | Benchmark: write 2 quiz questions per item (find + understand) answerable from BOTH versions; reviewer check | T | 10 | 3 | 0.5 | 1 | 15 | done 2026-11-12 (24 questions; LLM review 22 PASS/2 FIX, fixed; 9 wording-bias rewrites) |
| C14 | **Regression:** card rule 8 ("uncertainty as a number") makes Claude invent confidence %: 6/36 brainres answers vs 0/36 baseline ("~80% likely", "~90% 확신"). Reword: numbers only when grounded (measured rate, calculation); otherwise name what is uncertain + how to check (JD-33 spurious precision, #83). Add brainlint flag; re-run evals | Q | 5 | 2 | 0.8 | 0.5 | 16 | done 2026-11-12 (7/36 → 0/24; card 461 → 488 tokens) |
| B10-3 | Benchmark: static quiz page (bench/index.html, counterbalanced lists, timer, JSON export) + GitHub issue template for submissions | T | 10 | 3 | 0.5 | 1 | 15 | done 2026-11-12 (page + autotest + issue template) |
| C15 | Re-measure reminder tokens (text changed +13 chars in C14) with scripts/token_cost.sh; drop the README asterisk | T | 8 | 0.25 | 1.0 | 0.25 | 8 | done 2026-11-12 (card 488, reminder 84, skill 3,391) |
| B10-4 | Benchmark analysis script (bench/analyze.py): read submitted JSONs, apply exclusions, H1 mixed model (fallback Wilcoxon), H2 non-inferiority, H3 Brier; publish report | T | 10 | 3 | 0.5 | 2 | 7.5 | done 2026-11-12 (stdlib fallback analysis; simulation-validated; protocol v1.1 margin 5→10 pp) |
| B24 | Document interplay with Claude Code's built-in Concise/Explanatory styles | Q | 5 | 0.5 | 0.8 | 0.5 | 4 | done 2026-11-12 (measured: Explanatory −27% words, Insight kept; Concise +23%) |
| B05 | Per-turn micro-reminder hook (UserPromptSubmit, ≤300 chars) | Q | 10 | 2 | 0.8 | 0.5 | 32 | done 2026-11-12 |
| B01 | Core 10 rules in SKILL.md, each tied to evidence | Q | 10 | 3 | 0.8 | 1 | 24 | done 2026-11-12 |
| B02 | SessionStart hook so rules apply to every answer | Q | 10 | 2 | 0.8 | 0.5 | 32 | done 2026-11-12 |
| B03 | brainlint v0.1 scorer (EN + KO) | T | 8 | 1 | 0.8 | 1 | 6.4 | done 2026-11-12 |
| B04 | README with before/after hero and one-line install | G | 10 | 2 | 0.8 | 1 | 16 | done 2026-11-12 |
