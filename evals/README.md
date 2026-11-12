# Evals

`python3 evals/run.py` asks the 12 questions in [`prompts.jsonl`](prompts.jsonl) twice. That takes 24 headless `claude -p` calls on Sonnet, with tools and MCP disabled, run from an empty directory.

- **baseline:** Claude Code's default behavior.
- **brainres:** the same call, with the plugin's rule card and per-message reminder appended to the system prompt. This stands in for the installed hooks.

Each answer is scored by `brainlint`. Answers, `summary.json` and `REPORT.md` go to `results/<date>/`.

## Final result (B09b): 3 samples per prompt per condition

[`combine.py`](combine.py) merges runs made with the same core card. Each run records `card_sha`, so answers from an older card are excluded automatically. The final report is [`results/combined-final.md`](results/combined-final.md), with baseline n=36 and brainres n=36:

| | baseline | brainres | per-prompt difference (95% CI over 12 prompts) |
|---|---:|---:|---|
| Words | 201.7 | 147.3 | −54.4 (−89.1 to −19.6), −27% |
| Output tokens | 662 | 556 | −106 (−179 to −33), −16% |
| Brain Score | 91.2 | 96.2 | +5.0 (+0.8 to +9.2) |
| Within length budget | 29/36 | 32/36 | |
| No preamble / buried answer | 36/36 | 36/36 | |

The length budget is ≤100 words for yes/no and myth questions and ≤300 for everything else. The single-sample first run below overstated the length effect (−33%). This repeated measure supersedes it.

## Real plugin vs the card-append proxy (B29)

All earlier runs appended the card and reminder to the system prompt. This run installs the real plugin (`--plugin-dir`, so hooks fire and the skill can be invoked with the `Skill` and `Read` tools) and asks the 12 prompts × 2 samples. Results are in [`results/combined-plugin.md`](results/combined-plugin.md).

| Per-prompt vs baseline (Sonnet) | Real plugin | Card-append proxy |
|---|---|---|
| Words | −54 (95% CI −82 to −27) | −54 (−88 to −20) |
| Brain Score | +5.0 (+0.0 to +10.0) | +5.3 (+0.4 to +10.2) |
| Invented confidence % | 0 / 24 | 0 / 24 |

- **The proxy is valid.** The installed plugin produces the same effect.
- **The hooks do the work.** The skill was auto-invoked in only 1 of 24 answers, the emergency prompt (11). This matches the cost table: the 3,391-token skill body loads rarely, while the 488-token card and 84-token reminder are always present.

## Other models (B28)

The same 12 prompts were run with and without brainres on the current card, 1 sample each. Per-prompt differences are given with 95% CIs ([`results/combined-haiku.md`](results/combined-haiku.md)).

| Model | Words | Brain Score | Output tokens | Invented confidence % |
|---|---|---|---|---|
| Sonnet (3 samples) | −27% (−54; −89 to −20) | +5.0 (+0.8 to +9.2) | −16% (CI excludes 0) | 0 / 24 after C14 |
| **Haiku** (1 sample) | **−35%** (−71; −114 to −28) | **+3.9** (+0.1 to +7.7) | −14% (CI includes 0) | 0 / 12 |
| **Opus** (1 sample) | **−34%** (−79; −117 to −41) | +2.9 (−1.5 to +7.3, CI includes 0) | +19% *including hidden reasoning* (CI includes 0) | 0 / 12 |

**Output tokens on Opus.** The visible answers were a third shorter, but `output_tokens` rose because it includes hidden reasoning (`modelUsage.thinkingTokens`). One probe call showed 79 thinking tokens. The card plausibly prompts more deliberation, but this run didn't record the split, so that is unverified. `run.py` now records `thinking_tokens` and `visible_output_tokens`, and B28c re-runs Opus with the split. For visible length, words are the reliable measure.

The question-aware check (`--question`) caught one real Haiku slip. In 12, the brainres answer opened with "다음 기준으로 고르면 됩니다." and put the recommendation in sentence 2 (`no_recommendation`).

## Stress prompt with the real plugin (C13)

Card-only evals can't reach `support.md` because skill references load only when the skill is invoked. We ran the emergency prompt (11, "I deleted a production table") through the real plugin (`--plugin-dir`, tools `Skill Read`), 3 times before and 3 times after adding stress triggers to the skill description:

| | Old description | Description with stress triggers |
|---|---|---|
| Skill invoked | 0 / 3 | 1 / 3 |
| ≤5 numbered steps (support.md rule) | 2 / 3 | 3 / 3 |
| Mean Brain Score (rescored with the fixed brainlint) | 87.7 | 87.3 |

This is a partial effect on a tiny sample. The description change costs nothing always-on, so we kept it. The stress rule stays off the always-on card because its RICE score (3) is below the card's cut line ([ranking](../research/core-card-ranking.md)).

While doing this, brainlint got two fixes. `fragmented_reasoning` now ignores numbered steps, because steps are the right shape for procedures (#15). Nested list items no longer count toward the parent list. Scores in older `summary.json` files were computed with the scorer as it stood at run time.

## Interplay with built-in output styles (B24)

The style is passed with `--style` (`--settings {"outputStyle": ...}`). We used 4 prompts (01, 03, 08, 10), 1 sample each, comparing each style alone with the same style plus brainres. Results are in `results/2026-11-12-style-*`.

| Style | Mean words: alone → + brainres | Mean Brain Score | Notes |
|---|---|---|---|
| Explanatory | 307 → 224 (−27%) | 92.8 → 98.5 | ★ Insight blocks kept in 4 of 4 answers |
| Concise | 125 → 154 (+23%) | 95 → 95 | brainres adds decision support (when to switch, next step) |

There were no invented confidence numbers in any condition. The Learning style was not tested. The sample is tiny, so this documents the direction only.

## Regression found while building the benchmark (C14)

While writing quiz questions, we noticed brainres answers stating confidence numbers with no basis, such as "~80% likely on Homebrew Python", "Roughly 80% of small internal tools…" and "(~90% 확신)". A count across all answers:

| | Answers with an ungrounded confidence % |
|---|---:|
| baseline | 0 / 36 |
| brainres | **6 / 36** |

The cause is card rule 8, "uncertainty … as a number". Our own catalog warns against exactly this: spurious precision signals false confidence (JD-33, Jerez-Fernandez 2014). We count it as a real harm introduced by brainres.

**Fixed (C14).** Rule 8 now reads: "say what is unsure and how to check it. Use a number only if grounded (a measured rate, a calculation, a source); never invent a confidence %". `brainlint` gained an `invented_confidence` check.

| Card | Answers flagged by `invented_confidence` |
|---|---:|
| baseline | 0 / 36 |
| v2.1 (old rule 8) | 7 / 36 |
| **v2.2 (fixed)** | **0 / 24** |

On card v2.2 the length gain held: per prompt, words −54 (95% CI −88 to −20) and Brain Score +5.3 (CI +0.4 to +10.2) ([`results/combined-c14.md`](results/combined-c14.md)). The card cost rose from 461 to 488 tokens.

## First run (2026-11-12)

| Metric | baseline | brainres |
|---|---:|---:|
| Mean Brain Score | 91.6 | 93.5 |
| Median words | 210 | 140 (−33%) |
| Mean output tokens | 710 | 537 (−24%) |
| No preamble / buried answer | 12/12 | 12/12 |

Per-prompt results are in [`results/2026-11-12/REPORT.md`](results/2026-11-12/REPORT.md).

What this does and doesn't show:

- **Claude Code already answers first.** The baseline had no preambles in any of the 12 answers, so brainres's measurable effect here is **shorter answers with fewer formatting violations**, not answer-first.
- **Two prompts regressed.**
  - 09 (Korean concept, 88 → 82): two sentences run over 20 어절. The always-on card has no Korean line; the Korean rules live only in the skill's references (follow-up C12).
  - 08 (HTTPS, 94 → 84): the brainres answer was 291 words against 456, but it drew wall-of-text and bold-lead-in penalties. brainlint barely penalizes raw length, so the longer baseline scored higher.
- **Follow-up C12 is done.** After the Korean line was added to the card, a re-run of the 4 Korean prompts × 2 samples gave 0 of 8 answers with sentences over 20 어절 (before: 2 of 4). The mean Korean score went from 89.2 to 93.9 ([results](results/)). The stress prompt (11) still overuses bullets (82), and that is next to check.
- **The sample is small.** It is 12 prompts with one sample each, and LLM output varies between runs. Treat the gaps as directional (follow-up B09b repeats each prompt).
- **brainlint is a proxy.** It measures rule violations, not comprehension. Measuring comprehension needs people (B10).
