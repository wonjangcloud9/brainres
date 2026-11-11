# Evals

`python3 evals/run.py` asks the 12 questions in [`prompts.jsonl`](prompts.jsonl) twice. That takes 24 headless `claude -p` calls on Sonnet, with tools and MCP disabled, run from an empty directory.

- **baseline:** Claude Code's default behavior.
- **brainres:** the same call, with the plugin's rule card and per-message reminder appended to the system prompt. This stands in for the installed hooks.

Each answer is scored by `brainlint`. Answers, `summary.json` and `REPORT.md` go to `results/<date>/`.

## Repeated samples (B09b, in progress)

[`combine.py`](combine.py) merges runs made with the same core card. Answers from older cards are excluded because each run records `card_sha`. It reports means with SD and the per-prompt paired difference with a 95% t-interval. The interim result, with brainres at 2 samples and baseline at 3, is in [`results/combined-interim.md`](results/combined-interim.md):

| | brainres − baseline per prompt | 95% CI |
|---|---:|---|
| Brain Score | +4.6 | +0.4 to +8.8 |
| Words | −54 | −89 to −20 |
| Output tokens | −117 | −213 to −22 |

Answers within the length budget (≤100 words for yes/no and myth questions, ≤300 for everything else): 29/36 for baseline and 21/24 for brainres. The final numbers wait on 1 more brainres sample.

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
