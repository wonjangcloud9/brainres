# Combined eval (card 48809c2654f3, model=sonnet, treatment=brainres)

Runs: 2026-11-13-suite-v1a (30 answers); 2026-11-13-suite-v1b (30 answers); 2026-11-13-suite-v1c (30 answers); 2026-11-13-suite-v1d (30 answers); 2026-11-13-suite-v1e (30 answers); 2026-11-13-suite-v1f (10 answers)

Paired prompts: 78. Baseline rows are card-independent; brainres rows only from card 48809c2654f3.

| Metric | baseline mean (SD, n) | brainres mean (SD, n) | brainres − baseline per prompt (95% CI) |
|---|---|---|---|
| Brain Score | 92.6 (6.0, 78) | 97.4 (4.0, 78) | +4.8 (+3.3 to +6.4) |
| Words | 195.5 (105.6, 78) | 139.7 (65.3, 78) | -55.8 (-69.6 to -42.0) |
| Output tokens (incl. hidden reasoning) | 673.7 (333.9, 78) | 582.3 (307.4, 78) | -91.4 (-136.0 to -46.9) |
| Visible output tokens | 670.1 (333.9, 78) | 479.8 (200.6, 78) | -190.3 (-230.3 to -150.3) |
| Within length budget | 57/78 | 71/78 | |
| No preamble / buried answer | 78/78 | 78/78 | |
