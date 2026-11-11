# Evals

`python3 evals/run.py` asks the 12 questions in [`prompts.jsonl`](prompts.jsonl) twice. That takes 24 headless `claude -p` calls on Sonnet, with tools and MCP disabled, run from an empty directory.

- **baseline:** Claude Code's default behavior.
- **brainres:** the same call, with the plugin's rule card and per-message reminder appended to the system prompt. This stands in for the installed hooks.

Each answer is scored by `brainlint`. Answers, `summary.json` and `REPORT.md` go to `results/<date>/`.

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
- **The sample is small.** It is 12 prompts with one sample each, and LLM output varies between runs. Treat the gaps as directional (follow-up B09b repeats each prompt).
- **brainlint is a proxy.** It measures rule violations, not comprehension. Measuring comprehension needs people (B10).
