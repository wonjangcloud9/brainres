# Card ablation results (V3)

Each group's lines were removed from the card and the 15-prompt V1a subset was re-run (Sonnet, card proxy, 1 sample). Δ = ablated − full card, per prompt, on the same prompts. Noise, measured from 36 repeat-sample pairs of the same prompts: SD of a single-prompt difference is 4.7 points and 25 words, so the SE of a 15-prompt mean difference is about 1.2 points and 7 words. A Δ inside ±2.4 points or ±14 words is not a measurable effect. These prompts are general; rules aimed at specific situations (math in sentence 1, false premises, Korean speech level, invented confidence) were measured by their own evals and must be judged there too.

| Group removed | n | Δ Brain Score | Δ words | Δ thinking tokens | answer-first fails | question-check fails (ablated vs full) | checks that fire more without the group |
|---|---:|---:|---:|---:|---:|---|---|
| G1: 1 sentence-1 answer + 2 agree only with evidence | 15 | +0.9 | -7 | +7 | 0 | yesno_not_first 0→1 | term_swap 0→1 |
| G2: 3 fit expertise + 4 be concrete | 15 | +1.3 | +1 | +14 | 0 | none | long_sentences 0→2 |
| G3: 5 length + 6 ≤4 items + 7 prose/steps/tables + 11 end on next action | — | not run yet | | | | | |
| G4: 8 uncertainty once + 9 keep exact + 10 plain sentences/bold/Korean | — | not run yet | | | | | |
