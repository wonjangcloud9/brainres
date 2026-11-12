# Combined eval (card 48809c2654f3, model=sonnet, treatment=brainres)

Runs: 2026-11-13-suite-v1a (30 answers); 2026-11-13-suite-v1b (30 answers); 2026-11-13-suite-v1c (30 answers)

Paired prompts: 44. Baseline rows are card-independent; brainres rows only from card 48809c2654f3.

| Metric | baseline mean (SD, n) | brainres mean (SD, n) | brainres − baseline per prompt (95% CI) |
|---|---|---|---|
| Brain Score | 92.3 (6.5, 44) | 96.6 (4.8, 44) | +4.2 (+1.8 to +6.6) |
| Words | 192.0 (113.3, 44) | 137.9 (66.9, 44) | -54.0 (-74.4 to -33.7) |
| Output tokens (incl. hidden reasoning) | 622.5 (309.2, 44) | 520.1 (258.9, 44) | -102.4 (-145.9 to -58.9) |
| Visible output tokens | 620.9 (310.8, 44) | 442.8 (160.7, 44) | -178.1 (-232.8 to -123.3) |
| Within length budget | 32/44 | 40/44 | |
| No preamble / buried answer | 44/44 | 44/44 | |
