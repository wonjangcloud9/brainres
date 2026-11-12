<!-- Q: How do I get better at code reviews? -->

Review in a fixed order (design, correctness, tests, style) and learn from what slips through, because most reviewers improve by getting feedback on their misses, not by reading more diffs.

**Habits that help**

1. **Read the description first.** Know what the change is meant to do before judging how it does it. Many bad reviews comment on code that was never the point.
2. **Review in layers.** Ask "is this the right approach?" before "is this line correct?" Design objections found late are expensive, and nitpicks on a doomed design are wasted.
3. **Hunt for what's missing.** Look for unhandled errors, absent tests, unchecked inputs, and callers the diff didn't update. Missing things are hard to see because the diff only shows what's there.
4. **Keep reviews small and timely.** Past about 400 changed lines, review quality drops. Ask authors to split large changes, and review within a day so the author still has context.

**Making comments land**

- Ask questions when you're unsure ("what happens if this is null?") and state facts when you're sure.
- Label severity: `blocking:`, `suggestion:`, `nit:`. Authors then know what must change.
- Explain why, not just what. Link the bug, the rule, or the failure case.
- Leave automatable style issues to linters and formatters so your attention goes to logic.

**Ways to improve over time**

| Practice | What you learn |
|---|---|
| After a bug ships, reread the review that approved it | Which category of defect you miss |
| Read strong reviewers' comments on your own PRs | Which questions they ask that you don't |
| Keep a personal checklist of your recurring misses | Turns misses into a habit |
| Review your own diff before requesting review | You see your code as a reviewer does |

Google's public "Code Review Developer Guide" is a good short reference for the standard of "improves code health" over "is perfect."

Next step: pick one merged PR that later had a bug, and write down what question would have caught it. That question becomes the first item on your checklist.
