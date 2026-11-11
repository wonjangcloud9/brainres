# Backlog (RICE-ordered)

`score = Reach × Impact × Confidence ÷ Effort`. See [LOOP.md](LOOP.md) for scales.
Type: **Q** = answer quality · **T** = tooling/eval · **G** = growth/virality.
The loop always takes the highest-scoring `todo` item.

| ID | Item | Type | R | I | C | E | Score | Status |
|---|---|---|---|---|---|---|---|---|
| C07 | brainlint v0.2: deterministic checks for new line-level rules — "all…not", bare "This", "former/latter", "simply/just/obviously", "great question", "Does that make sense?", emoji in technical answers, warning boilerplate | T | 10 | 1 | 0.8 | 1 | **8** | todo |
| C08 | Research round 2: re-verify every W/C citation flagged "unverified" in the catalogs; up/downgrade grades | Q | 10 | 1 | 0.8 | 1 | **8** | todo |
| C09 | Research round 2: new domains (cross-cultural pragmatics, diagram cognition — Larkin & Simon, argumentation/Toulmin, journalism inverted-pyramid studies, numeracy individual differences) | Q | 5 | 1 | 0.5 | 1 | **2.5** | todo |
| C10 | Condensed core card v2: re-rank always-on rules by RICE across all 725 findings (keep ≤500 tokens) | Q | 10 | 2 | 0.8 | 1 | **16** | todo |
| C01 | **Full-coverage program.** Ingest the 6 domain catalogs (psycholinguistics, learning science, attention & neuro, judgment & trust, HCI & info design, emotion & pragmatics) into `research/catalog-*.md` with Applies/Situation columns | Q | 10 | 3 | 0.8 | 1 | **24** | done 2026-11-12 |
| C02 | Situation router in SKILL.md + one `references/<situation>.md` per situation, so every applicable finding has a home without bloating the always-on card | Q | 10 | 3 | 0.8 | 1 | **24** | done 2026-11-12 |
| C03 | Close **core** coverage gaps (see `research/coverage.md` → "Not yet applied", situation=core) | Q | 10 | 3 | 0.8 | 1 | **24** | done 2026-11-12 (596/596) |
| C04 | Close **explain / long-form / learn** coverage gaps | Q | 5 | 3 | 0.8 | 1 | **12** | done 2026-11-12 (596/596) |
| C05 | Close **decide / numbers / correction / procedure / code / voice** coverage gaps | Q | 5 | 3 | 0.8 | 1 | **12** | done 2026-11-12 (596/596) |
| C06 | Coverage badge in README ("N findings reviewed · X% applied") + explain the ledger | G | 8 | 2 | 1.0 | 0.5 | **32** | done 2026-11-12 |
| B25 | Measure and publish the token cost of the core card and reminder in the README (honest numbers) | G | 8 | 1 | 1.0 | 0.5 | **16** | todo |
| B14 | Launch drafts in `launch/`: Show HN, X thread, GeekNews, r/ClaudeAI. Owner posts them | G | 8 | 2 | 0.5 | 0.5 | **16** | todo |
| B19 | Portable builds: `dist/system-prompt.md` (any LLM), AGENTS.md / Cursor rule, claude.ai skill zip | G | 8 | 2 | 0.8 | 1 | **12.8** | todo |
| B12 | brainlint golden tests (`tests/`), run from validate.sh | T | 5 | 1 | 1.0 | 0.5 | **10** | todo |
| B08 | Opt-in output style `output-styles/brainres.md` for people who want it as their style | Q | 5 | 1 | 0.8 | 0.5 | **8** | todo |
| B17 | `references/learn.md`: prequestion → worked example with fading → 1–2 retrieval checks (#68–70, #10) | Q | 2 | 2 | 1.0 | 0.5 | **8** | todo |
| B18 | `references/uncertainty.md`: verbal ↔ numeric probability table (EN/KO), local first-person hedges (#65, #82, #84) | Q | 5 | 1 | 0.8 | 0.5 | **8** | todo |
| B06 | `references/korean.md`: 번역투 catalog, 어절-based sentence length, 종결어미 consistency; improve Korean sentence splitter in brainlint | Q | 5 | 2 | 0.8 | 1 | **8** | todo |
| B11 | brainlint v0.2: answer-first detection beyond preamble regex, causal-connective loss in bullets, term-swap detection | T | 10 | 1 | 0.8 | 1 | **8** | todo |
| B13 | 4 more before/after examples: concept explanation, comparison table, risk numbers, misconception refutation | G | 10 | 1 | 0.8 | 1 | **8** | todo |
| B22 | Social preview image + "Brain Score" badge for READMEs | G | 8 | 1 | 0.5 | 0.5 | **8** | todo |
| B09 | Eval harness: 12 prompts × {baseline, brainres} via `claude -p`; report brainlint score, words, answer-in-sentence-1 rate | T | 10 | 2 | 0.8 | 2 | **8** | todo |
| B16 | `references/rewrite.md`: claim inventory → rewrite → lost-claim check (humanizer v3 lesson) | Q | 2 | 2 | 0.8 | 0.5 | **6.4** | todo |
| B10 | Human comprehension benchmark protocol: quiz + time-to-answer on paired answers. Nobody else measures this | T | 10 | 3 | 0.5 | 3 | **5** | todo |
| B24 | Document interplay with Claude Code's built-in Concise/Explanatory styles | Q | 5 | 0.5 | 0.8 | 0.5 | **4** | todo |
| B21 | Web playground (GitHub Pages): paste text → Brain Score (brainlint port to JS) | G | 8 | 2 | 0.5 | 2 | **4** | todo |
| B23 | Voice-mode rules (transient information effect, #9) | Q | 1 | 1 | 0.8 | 0.5 | **1.6** | todo |
| B20 | GitHub Action: brainlint on docs in PRs | T | 2 | 1 | 0.5 | 1 | **1** | todo |
| B07 | `README.ko.md` for Korean devs (GeekNews, Korean X) | G | 5 | 2 | 0.8 | 0.5 | 16 | done 2026-11-12 |
| B05 | Per-turn micro-reminder hook (UserPromptSubmit, ≤300 chars) | Q | 10 | 2 | 0.8 | 0.5 | 32 | done 2026-11-12 |
| B01 | Core 10 rules in SKILL.md, each tied to evidence | Q | 10 | 3 | 0.8 | 1 | 24 | done 2026-11-12 |
| B02 | SessionStart hook so rules apply to every answer | Q | 10 | 2 | 0.8 | 0.5 | 32 | done 2026-11-12 |
| B03 | brainlint v0.1 scorer (EN + KO) | T | 8 | 1 | 0.8 | 1 | 6.4 | done 2026-11-12 |
| B04 | README with before/after hero and one-line install | G | 10 | 2 | 0.8 | 1 | 16 | done 2026-11-12 |
