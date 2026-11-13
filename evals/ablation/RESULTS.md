# Card ablation results (V3)

Each group's lines were removed from the card and the 15-prompt V1a subset was re-run (Sonnet, card proxy, 1 sample). Δ = ablated − full card, per prompt, on the same prompts. Noise, measured from 36 repeat-sample pairs of the same prompts: SD of a single-prompt difference is 4.7 points and 25 words, so the SE of a 15-prompt mean difference is about 1.2 points and 7 words. A Δ inside ±2.4 points or ±14 words is not a measurable effect. These prompts are general; rules aimed at specific situations (math in sentence 1, false premises, Korean speech level, invented confidence) were measured by their own evals and must be judged there too.

| Group removed | n | Δ Brain Score | Δ words | Δ thinking tokens | answer-first fails | question-check fails (ablated vs full) | checks that fire more without the group |
|---|---:|---:|---:|---:|---:|---|---|
| G1: 1 sentence-1 answer + 2 agree only with evidence | 15 | +0.3 | -7 | +7 | 0 | yesno_not_first 0→1 | term_swap 0→1 |
| G2: 3 fit expertise + 4 be concrete | 15 | +0.7 | +1 | +14 | 0 | none | long_sentences 0→2 |
| G3: 5 length + 6 ≤4 items + 7 prose/steps/tables + 11 end on next action | 15 | -2.1 | +9 | -21 | 0 | yesno_not_first 0→1 | double_negation 1→2, long_sentences 0→2, hedging 0→1, outro 0→1, list_overload 0→1 |
| G4: 8 uncertainty once + 9 keep exact + 10 plain sentences/bold/Korean | 15 | -0.9 | -13 | -40 | 0 | none | bold_overuse 1→3, long_sentences 0→3 |

*Scores re-scored with the current brainlint (K1, K2 and S1 applied to these runs on 2026-11-13); the old values are kept as `score_before_s1`. G3's wall of text was a K1 artifact. No decision changed.*

## Decision: keep every line

- **G3** (length, grouping, prose/steps/tables, ending on the next action) **and G4** (uncertainty, exact values, plain sentences/bold/Korean) do work. Removing either raises the checks those lines target. Without G3: list overload, sign-off outros, hedging, double negation and long sentences all rose, and the score was −2.1, at the edge of the noise. Without G4: bold overuse went 1 → 3 and long sentences 0 → 3.
- **G1** (sentence-1 answer, agree only with evidence) **and G2** (fit expertise, be concrete) show nothing on these 15 general prompts. They are situation rules with their own evidence: rule 1's math clause took sentence 1 to 9/9 correct (C17), rule 2 targets false premises and sycophancy, and rule 3 matches novice gains in coverage (V2: novice +10 pp). General prompts can't test them, so they stay.
- **Hidden reasoning:** the card adds about 100 thinking tokens per answer (V4), and no single group is the source. Removing G4 cut thinking the most (−40), then G3 (−21). Thinking-token noise was not measured, so treat these as directions only.

