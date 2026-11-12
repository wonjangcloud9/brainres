# Combined eval (card 48809c2654f3, model=sonnet, treatment=brainres)

Runs: 2026-11-13-suite-v1a (30 answers); 2026-11-13-suite-v1b (30 answers); 2026-11-13-suite-v1c (30 answers); 2026-11-13-suite-v1d (30 answers); 2026-11-13-suite-v1e (30 answers)

Paired prompts: 73. Baseline rows are card-independent; brainres rows only from card 48809c2654f3.

| Metric | baseline mean (SD, n) | brainres mean (SD, n) | brainres − baseline per prompt (95% CI) |
|---|---|---|---|
| Brain Score | 91.7 (6.5, 73) | 96.3 (4.8, 73) | +4.6 (+2.8 to +6.3) |
| Words | 194.7 (105.4, 73) | 139.6 (66.0, 73) | -55.2 (-69.5 to -40.9) |
| Output tokens (incl. hidden reasoning) | 674.3 (338.9, 73) | 578.8 (289.9, 73) | -95.5 (-134.3 to -56.6) |
| Visible output tokens | 670.4 (338.9, 73) | 483.3 (203.3, 73) | -187.2 (-228.7 to -145.6) |
| Within length budget | 54/73 | 66/73 | |
| No preamble / buried answer | 73/73 | 73/73 | |
