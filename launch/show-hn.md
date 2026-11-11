# Show HN: brainres – Claude answers built from 725 cognitive-science findings

**URL:** https://github.com/wonjangcloud9/brainres

**Text:**

I found Claude's answers hard to read. They were long, opened with preamble, and the actual answer was buried in the middle. The popular fixes go in two directions. Caveman-style skills cut tokens. Humanizer-style skills remove "AI tells". Neither one asks the question I cared about: does a human understand the answer faster?

brainres is a Claude Code plugin that works on that question. I had agents survey seven research areas:

- working memory
- psycholinguistics (including Korean reading)
- learning science
- attention and neurodiversity
- decision science and human–AI trust
- information design
- conversational pragmatics

That produced 725 findings. Each one is either turned into a concrete writing rule or excluded with a reason: not applicable to text, failed replication, neuromyth, or manipulative. A coverage script enforces this. Right now 596 of 596 applicable findings are cited by a rule, and CI blocks any commit that lowers the count.

What it does in practice:

- The answer comes in sentence 1. A yes/no question starts with "Yes" or "No".
- Groups have at most 4 items. Reasoning stays in prose, and lists are only for parallel items.
- Uncertainty is stated once, inside the claim, as a number. Citations appear only when they're verified (random citations raise trust, Ding 2025).
- It doesn't agree with you without evidence. Sycophantic AI raises trust and harms judgment (Cheng 2026, Science).
- It adapts to the reader: experts get terse answers, novices get definitions and one worked example (expertise reversal).

The always-on card is 461 tokens (measured with Claude's tokenizer; script in the repo). Situation-specific rules (debugging, decisions, risk numbers, emotional support, accessibility, Korean) live in reference files the model reads only when needed.

There's also `brainlint`, a stdlib Python scorer that maps each check to a finding. A typical answer that opens with "Great question!", uses 7 bold bullets and ends with "Hope this helps!" scores 50/100. The rewrite scores 100.

First measurement (12 prompts × with/without, Sonnet, tools off): median answer length 210 → 140 words (−33%), output tokens −24%, Brain Score 91.6 → 93.5. Claude Code already avoided preambles in all 12 baseline answers, so the gain is mostly length and formatting. Two prompts regressed, and both are documented in evals/README.md.

Honest limits: nobody, including me, has run controlled studies of formatting rules on LLM chat answers. "Applied" currently means "cited by a rule", not "shown to improve comprehension". A human comprehension benchmark is the next big item. The repo is also being improved by a Claude Code loop every 20 minutes, and every iteration is logged in LOOP_LOG.md.

I'd love criticism of specific rules. Before/after pairs where brainres made an answer worse would be the most useful.
