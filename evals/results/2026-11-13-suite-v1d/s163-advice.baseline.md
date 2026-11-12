<!-- Q: How do I get better at code reviews? -->

Getting better at code reviews mostly comes down to a few habits:

**Before you read the code**
- Understand the intent first: read the PR description, linked issue, or ticket. You can't judge whether a change is right without knowing what it's for.
- Look at the overall shape (files touched, size, tests added) before diving into lines.

**While reviewing**
- Review in layers: design and approach first, then correctness and edge cases, then readability, and style last. Don't spend energy on nits if the design is wrong.
- Ask "what could break?" Think about null/empty inputs, error paths, concurrency, backwards compatibility, migrations, and performance on large data.
- Check the tests: do they actually cover the new behavior and failure cases, or just the happy path?
- Look for what's missing, not just what's present: missing validation, logging, docs, cleanup, rollback paths.
- Pull the branch and run it when the change is non-trivial. Reading alone misses a lot.
- Let linters and formatters handle style so you can focus on logic.

**How you communicate**
- Be specific and actionable: "This will throw if `user` is null on line 42; consider an early return" beats "needs error handling."
- Ask questions instead of issuing verdicts when you're unsure: "What happens if this is called twice?"
- Label severity: prefix minor items with `nit:`, and make clear what's blocking vs. optional.
- Explain the why, and suggest an alternative when you push back.
- Call out good work too. It builds trust and makes critical feedback land better.
- Critique the code, not the person.

**Process habits**
- Keep reviews small and timely. Review in sessions of under ~60 minutes, and ideally under 400 lines at a time; effectiveness drops sharply beyond that.
- Use a checklist for recurring concerns (security, error handling, API changes, test coverage) until it becomes instinct.
- Read others' reviews on code you wrote or on PRs you're not part of. Seeing what experienced reviewers catch is one of the fastest ways to learn.
- Review your own PRs before requesting review; you'll catch a surprising amount and learn what you tend to miss.
- Track escaped bugs: when something slips through to production, ask what review question would have caught it, and add it to your habits.
- Read good open-source PRs and project review guidelines (e.g., Google's "Code Review Developer Guide" is a solid public reference).

**As an author too**
- Writing small, well-described PRs with context makes you more aware of what makes a PR easy to review, which feeds back into your reviewing.

If you'd like, I can help build a personal review checklist tailored to your language or stack, or review a real diff with you and talk through my reasoning.
