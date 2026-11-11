# r/ClaudeAI post

**Title:** I turned 725 cognitive-science findings into a Claude Code plugin that makes answers easier to understand (not just shorter)

**Body:**

Caveman-style skills cut tokens, and humanizer skills remove AI tells. I wanted answers my brain could parse faster, so I built **brainres**.

- **Coverage:** 725 findings from 7 research areas. Each one is either a concrete writing rule or excluded with a reason. 596 of 596 applicable findings are applied, and a coverage script in CI enforces it.
- **Always on:** 418 tokens per session plus a 79-token reminder each turn (measured), so the rules don't fade.
- **Situation files:** debugging, decisions, risk numbers, emotional support, accessibility and Korean get their own rules. They load only when needed.
- **Anti-sycophancy:** it checks your premise and agrees only with evidence.
- **`brainlint`:** scores any answer out of 100. Every check maps to a paper.

Install: `claude plugin install brainres --marketplace wonjangcloud9/brainres`

Before/after is in the README. I'd really like cases where it makes answers *worse*. The next step is a human comprehension benchmark, because "applied" currently means "cited by a rule", not "proven".

https://github.com/wonjangcloud9/brainres
