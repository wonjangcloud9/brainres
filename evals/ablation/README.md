# Card ablation (V3)

Each file is `hooks/core-card.md` with one group of rule lines removed. Run with `evals/run.py --card evals/ablation/card-minus-G<n>.md`.

| File | Lines removed |
|---|---|
| card-minus-G1.md | 1 sentence-1 answer, 2 agree only with evidence |
| card-minus-G2.md | 3 fit their expertise, 4 be concrete |
| card-minus-G3.md | 5 length, 6 ≤4 items per group, 7 prose/steps/tables, 11 end on the next action |
| card-minus-G4.md | 8 uncertainty once, 9 keep exact, 10 plain sentences / bold / Korean |
