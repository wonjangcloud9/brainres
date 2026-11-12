# r/ClaudeAI post

**Title:** I turned 801 cognitive-science findings into a Claude Code plugin that makes answers easier to understand (not just shorter)

**Body:**

Caveman-style skills cut tokens, and humanizer skills remove AI tells. I wanted answers my brain could parse faster, so I built **brainres**.

- **Coverage:** 801 findings from 7 research areas. Each one is either a concrete writing rule or excluded with a reason. 659 of 659 applicable findings are applied, and a coverage script in CI enforces it.
- **Always on:** 500 tokens per session (measured). An extra line of about 25 tokens is added only on learner or emergency messages.
- **Situation files:** debugging, decisions, risk numbers, emotional support, accessibility and Korean get their own rules. They load only when needed.
- **Anti-sycophancy:** it checks your premise and agrees only with evidence.
- **Eval (80-prompt suite, 16 answer types, 78 valid pairs):** answers 29% shorter, 28% fewer visible output tokens and +5.1 Brain Score, all with 95% CIs. It was about even or slightly behind in 3 of 16 types (debugging, stress, formal docs), and that is published too.
- **`brainlint`:** scores any answer out of 100. Every check maps to a paper.

Install: `claude plugin install brainres --marketplace wonjangcloud9/brainres`

Before/after is in the README. I'd really like cases where it makes answers *worse*. The next step is a human comprehension benchmark, because "applied" currently means "cited by a rule", not "proven".

https://github.com/wonjangcloud9/brainres
