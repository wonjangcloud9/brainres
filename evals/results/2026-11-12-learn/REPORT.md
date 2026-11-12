# Eval report (2026-11-12-learn, model=sonnet, 4 prompts × 2 sample(s))

| Metric | baseline | brainres | plugin |
|---|---:|---:|---:|
| Mean Brain Score | 94.8 | 100.0 | 100.0 |
| Median words | 76 | 85 | 93 |
| Mean output tokens | 490 | 409 | 481 |
| No preamble / buried answer | 8/8 | 8/8 | 8/8 |

| Prompt | Type | baseline score | brainres score | plugin score | baseline words | brainres words | plugin words |
|---|---|---:|---:|---:|---:|---:|---:|
| l01-learner-py | learn | 100 | 100 | 100 | 65 | 61 | 68 |
| l02-learner-js | learn | 100 | 100 | 100 | 196 | 188 | 175 |
| l03-learner-py-ko | learn | 86 | 100 | 100 | 88 | 108 | 106 |
| l04-learner-c-ko | learn | 93 | 100 | 100 | 65 | 65 | 78 |
