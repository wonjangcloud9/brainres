<!-- Q: How do I get better at code reviews? -->

Review in a fixed order (intent, correctness, design, tests, style) and study the bugs that slip past you, because judgment comes from repetition with feedback.

1. **Read the description and tests first.** You can't judge whether code is right until you know what it is meant to do. If the intent is unclear, ask before reading the diff.
2. **Check in order of cost to fix later.** Correctness and design mistakes are expensive, while naming and formatting are cheap. Leave formatting to a linter so your attention goes to logic, edge cases, error handling, and security.
3. **Write comments that name the problem and offer a fix.**
   - Weak: "This is confusing."
   - Strong: "`retry()` loops forever if the server returns 429 without `Retry-After`. Could we cap it, e.g. `for _ in range(5)`?"

   Mark optional nits as "nit:" so the author knows what blocks the merge.
4. **Learn from misses.** When a bug ships after you approved it, ask which check would have caught it and add that check to your list. Over time the list becomes your personal checklist.

Two habits help too. Read reviews that senior teammates leave on your own PRs and note what they catch that you don't. Also review small diffs often, since a huge diff gets skimmed rather than reviewed.

Next step: pick one open PR and run the four steps above on it. If you paste a diff here, I'll review it and show you what I'd flag and why.
