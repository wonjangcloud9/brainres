# Before / after examples

Each folder holds a `question.md`, a typical verbose `before.md`, and a brainres `after.md`. Scores come from `brainlint` and are pinned by `tests/test_brainlint.py`.

| # | Type | Question | Before | After | Rules shown |
|---|---|---|---:|---:|---|
| 01 | Debugging | React component re-renders forever | 50 | 100 | answer first, causal chain, verify step |
| 02 | Decision (Korean) | Redis or in-memory cache, one server | 41 | 100 | one recommendation + when to switch, 해요체 |
| 03 | Concept | How a database index speeds queries | 50 | 100 | mechanism with numbers, analogy + where it breaks |
| 04 | Comparison | SQLite, Postgres or MongoDB for a todo app | 78 | 100 | verdict above the table, "wrong choice if…" |
| 05 | Risk numbers | 50 tests at 2% flakiness each | 66 | 100 | cumulative probability, natural frequencies |
| 06 | Misconception | Does incognito hide browsing from my ISP? | 71 | 100 | "No" first, refutation, who-sees-what table |

**Known blind spot:** brainlint can't see the question, so it can't tell that a "before" answer never recommends anything. Example 04 still scores 78 for that reason. That is why brainlint is a heuristic, not a comprehension test.
