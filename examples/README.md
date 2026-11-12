# Before / after examples

Each folder holds a `question.md`, a typical verbose `before.md`, and a brainres `after.md`. Scores come from `brainlint` and are pinned by `tests/test_brainlint.py`.

| # | Type | Question | Before | After | Rules shown |
|---|---|---|---:|---:|---|
| 01 | Debugging | React component re-renders forever | 56 | 100 | answer first, causal chain, verify step |
| 02 | Decision (Korean) | Redis or in-memory cache, one server | 39 | 100 | one recommendation + when to switch, 해요체 |
| 03 | Concept | How a database index speeds queries | 48 | 100 | mechanism with numbers, analogy + where it breaks |
| 04 | Comparison | SQLite, Postgres or MongoDB for a todo app | 78 | 100 | verdict above the table, "wrong choice if…" |
| 05 | Risk numbers | 50 tests at 2% flakiness each | 66 | 100 | cumulative probability, natural frequencies |
| 06 | Misconception | Does incognito hide browsing from my ISP? | 71 | 100 | "No" first, refutation, who-sees-what table |

**Blind spot, now closable:** without the question, brainlint can't tell that a "before" answer never recommends anything, so example 04 scores 78. Run it with `--question` and `no_recommendation` fires: 04 drops to 70 and 02 to 31. brainlint is still a heuristic, not a comprehension test.
