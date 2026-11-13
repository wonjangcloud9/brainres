# Eval report (2026-11-13-u1b, model=sonnet, 4 prompts × 1 sample(s))

| Metric | baseline | plugin |
|---|---:|---:|
| Mean Brain Score | 98.8 | 98.0 |
| Median words | 782 | 473 |
| Mean output tokens | 3573 | 2490 |
| No preamble / buried answer | 4/4 | 4/4 |

| Prompt | Type | baseline score | plugin score | baseline words | plugin words |
|---|---|---:|---:|---:|---:|
| p1-offline-en | plan | 95 | 100 | 788 | 555 |
| p2-ratelimit-en | plan | 100 | 97 | 776 | 631 |
| p3-rbac-ko | plan | 100 | 100 | 621 | 312 |
| p4-retry-ko | plan | 100 | 95 | 862 | 391 |
