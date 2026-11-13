# Show HN: brainres – Claude answers built from 805 cognitive-science findings

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

That produced 805 findings. Each one is either turned into a concrete writing rule or excluded with a reason: not applicable to text, failed replication, neuromyth, or manipulative. A coverage script enforces this. Right now 663 of 663 applicable findings are cited by a rule, and CI blocks any commit that lowers the count.

What it does in practice:

- The answer comes in sentence 1. A yes/no question starts with "Yes" or "No".
- Groups have at most 4 items. Reasoning stays in prose, and lists are only for parallel items.
- Uncertainty is stated once, inside the claim. Numbers appear only when grounded; an early version made Claude invent "~80% sure" figures, which we measured and fixed. Citations appear only when they're verified (random citations raise trust, Ding 2025).
- It doesn't agree with you without evidence. Sycophantic AI raises trust and harms judgment (Cheng 2026, Science).
- It adapts to the reader: experts get terse answers, novices get definitions and one worked example (expertise reversal).

The always-on card is 500 tokens (measured with Claude's tokenizer; script in the repo). Situation-specific rules (debugging, decisions, risk numbers, emotional support, accessibility, Korean) live in reference files the model reads only when needed.

There's also `brainlint`, a stdlib Python scorer that maps each check to a finding. A typical answer that opens with "Great question!", uses content-free headings and ends with "Hope this helps!" scores 56/100. The rewrite scores 100.

Measurement (an 80-prompt suite, 16 answer types including 32 Korean prompts, with/without, Sonnet, tools off, 78 valid pairs): answers 29% shorter (95% CI −42 to −70 words per prompt), visible output tokens −28%, Brain Score +4.6 (CI +3.2 to +6.1); brainres was about even in 2 of 16 types (formal docs, refusals), which we publish. Earlier 12-prompt run: Brain Score 91.2 → 96.2. Claude Code already avoided preambles, so the gain is length and readability violations. A single-sample run first showed −33%, and the larger sample shrank it. Both are in evals/README.md.

Honest limits: nobody, including me, has run controlled studies of formatting rules on LLM chat answers. "Applied" currently means "cited by a rule", not "shown to improve comprehension". A human comprehension benchmark is the next big item.

I'd love criticism of specific rules. Before/after pairs where brainres made an answer worse would be the most useful.
