# Combined eval (card 0bd557e38b55, model=opus, treatment=brainres)

Runs: 2026-11-12-opus (24 answers); 2026-11-12-opus-split (24 answers)

Paired prompts: 12. Baseline rows are card-independent; brainres rows only from card 0bd557e38b55.

| Metric | baseline mean (SD, n) | brainres mean (SD, n) | brainres − baseline per prompt (95% CI) |
|---|---|---|---|
| Brain Score | 92.2 (4.9, 24) | 95.5 (4.8, 24) | +3.3 (-0.5 to +7.2) |
| Words | 232.7 (118.1, 24) | 152.3 (72.0, 24) | -80.3 (-112.7 to -48.0) |
| Output tokens (incl. hidden reasoning) | 985.3 (562.6, 24) | 1049.7 (773.5, 24) | +64.3 (-189.5 to +318.1) |
| Within length budget | 15/24 | 20/24 | |
| No preamble / buried answer | 24/24 | 24/24 | |
