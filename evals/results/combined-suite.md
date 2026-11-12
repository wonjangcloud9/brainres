# Combined eval (card 48809c2654f3, model=sonnet, treatment=brainres)

Runs: 2026-11-13-suite-v1a (30 answers); 2026-11-13-suite-v1b (30 answers)

Paired prompts: 29. Baseline rows are card-independent; brainres rows only from card 48809c2654f3.

| Metric | baseline mean (SD, n) | brainres mean (SD, n) | brainres − baseline per prompt (95% CI) |
|---|---|---|---|
| Brain Score | 93.3 (6.8, 29) | 96.0 (5.1, 29) | +2.7 (-0.3 to +5.7) |
| Words | 208.2 (128.0, 29) | 151.4 (74.3, 29) | -56.8 (-84.6 to -29.1) |
| Output tokens (incl. hidden reasoning) | 584.6 (311.3, 29) | 495.2 (255.6, 29) | -89.4 (-142.9 to -35.8) |
| Visible output tokens | 584.6 (311.3, 29) | 422.3 (169.8, 29) | -162.3 (-228.6 to -95.9) |
| Within length budget | 19/29 | 26/29 | |
| No preamble / buried answer | 29/29 | 29/29 | |
