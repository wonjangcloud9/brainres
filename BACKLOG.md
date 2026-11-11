# Backlog (RICE-ordered)

`score = Reach × Impact × Confidence ÷ Effort`. See [LOOP.md](LOOP.md) for scales.
Type: **Q** = answer quality · **T** = tooling/eval · **G** = growth/virality.
The loop always takes the highest-scoring `todo` item.

| ID | Item | Type | R | I | C | E | Score | Status |
|---|---|---|---|---|---|---|---|---|
| B05 | Per-turn micro-reminder hook (UserPromptSubmit, ≤300 chars). Rules decay over long sessions; claude-terse cut violations 11.1→1.1/1k words with this | Q | 10 | 2 | 0.8 | 0.5 | **32** | todo |
| B25 | Measure and publish the token cost of the core card and reminder in the README (honest numbers) | G | 8 | 1 | 1.0 | 0.5 | **16** | todo |
| B07 | `README.ko.md` for Korean devs (GeekNews, Korean X) | G | 5 | 2 | 0.8 | 0.5 | **16** | todo |
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
| B01 | Core 10 rules in SKILL.md, each tied to evidence | Q | 10 | 3 | 0.8 | 1 | 24 | done 2026-11-12 |
| B02 | SessionStart hook so rules apply to every answer | Q | 10 | 2 | 0.8 | 0.5 | 32 | done 2026-11-12 |
| B03 | brainlint v0.1 scorer (EN + KO) | T | 8 | 1 | 0.8 | 1 | 6.4 | done 2026-11-12 |
| B04 | README with before/after hero and one-line install | G | 10 | 2 | 0.8 | 1 | 16 | done 2026-11-12 |
