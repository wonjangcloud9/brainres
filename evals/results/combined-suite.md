# Combined eval (card 48809c2654f3, model=sonnet, treatment=brainres)

Runs: 2026-11-13-suite-v1a (30 answers); 2026-11-13-suite-v1b (30 answers); 2026-11-13-suite-v1c (30 answers); 2026-11-13-suite-v1d (30 answers)

Paired prompts: 58. Baseline rows are card-independent; brainres rows only from card 48809c2654f3.

| Metric | baseline mean (SD, n) | brainres mean (SD, n) | brainres − baseline per prompt (95% CI) |
|---|---|---|---|
| Brain Score | 91.4 (6.6, 58) | 96.3 (4.8, 58) | +4.9 (+2.9 to +7.0) |
| Words | 187.7 (111.1, 58) | 131.8 (64.8, 58) | -55.9 (-72.9 to -38.8) |
| Output tokens (incl. hidden reasoning) | 663.2 (323.7, 58) | 560.5 (280.2, 58) | -102.7 (-142.3 to -63.2) |
| Visible output tokens | 660.5 (324.6, 58) | 468.9 (177.1, 58) | -191.5 (-239.8 to -143.3) |
| Within length budget | 43/58 | 53/58 | |
| No preamble / buried answer | 58/58 | 58/58 | |
