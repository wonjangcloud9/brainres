# Eval report (2026-11-13-suite-v1f, model=sonnet, 5 prompts × 1 sample(s))

| Metric | baseline | brainres |
|---|---:|---:|
| Mean Brain Score | 92.8 | 98.8 |
| Median words | 196 | 124 |
| Mean output tokens | 666 | 633 |
| No preamble / buried answer | 5/5 | 5/5 |

| Prompt | Type | baseline score | brainres score | baseline words | brainres words |
|---|---|---:|---:|---:|---:|
| s125-compare | compare | 94 | 100 | 196 | 124 |
| s135-codex | code-explain | 100 | 100 | 115 | 122 |
| s145-write | write-code | 92 | 100 | 69 | 61 |
| s155-multi | multi-part | 92 | 100 | 341 | 212 |
| s165-advice | advice | 86 | 94 | 314 | 192 |
