# LLM-side risk: can answer-style rules hurt the model's own accuracy?

Research round, 2026-11-12, run because the backlog was empty. The catalogs cover how *people* read. This file covers what style instructions do to the *model*. These findings guide what we test; they are not writing rules, so they are not counted in the coverage ledger.

| Finding | Source | Ev | What it means for brainres |
|---|---|---|---|
| Strict format restrictions degrade LLM reasoning; looser format instructions hurt less, and classification can even improve | Tam et al. 2024, "Let Me Speak Freely?", EMNLP Industry (arXiv 2408.02442) | M | brainres states formats as guidance ("prose for reasoning, steps numbered"), not as rigid schemas. Keep it that way, and don't add hard output templates to the card |
| A universal trade-off between reasoning length and accuracy; "be concise" prompts cut length but cost some accuracy, and sit far from the best achievable trade-off | Lee, Che & Peng 2025 (arXiv 2503.01141), citing Jin 2024, Renze & Guven 2024, Han 2024 | M | Real risk for models without hidden reasoning: shortening the *written* answer can shorten the *reasoning*. Not yet measured on multi-step problems → B33 |
| Longer chain-of-thought is not always better; there is an optimal length | Wu et al. 2025 (arXiv 2502.07266) | M | Brevity isn't automatically harmful. Measure, don't assume |

## What we already know from our own evals

- On **Opus**, brainres raised hidden reasoning about 2.6× while visible output fell 36% (B28c). That is the desirable split: think fully, write briefly.
- On **18 trap prompts on Haiku** (B31/B31b), accuracy was identical with and without brainres (18/18 both). These were mostly single-step traps, though, not long multi-step problems.

## B33a result: multi-step problems on Haiku

[`evals/math15.jsonl`](../evals/math15.jsonl) holds 15 problems with answers computed in Python: tax and discount, train catch-up, tank fill, compound interest, scaling, ages, work rate, time zones, server capacity, mixtures, two Korean word problems, disk growth and dice. Each was run with and without the card (30 calls). Results are in `evals/results/2026-11-12-math15-haiku/`.

| | Correct (first sentence or last 3 lines; spot-checked by hand) | Reason within the first 2 sentences | Median words |
|---|---:|---:|---:|
| baseline | 15 / 15 | 12 / 15 | 45 |
| brainres | 15 / 15 | 6 / 15 | 51 |

- **No accuracy cost was observed.** Both conditions hit the ceiling, though, so this run can't detect a small cost.
- **One reasoning slip appeared in a brainres explanation.** The time-zone answer said "Seoul is 9 hours ahead of UTC-8"; the correct gap is 17 hours, or 9 hours ahead of UTC. The final answer was still right, and the baseline explanation was correct. One case in 15 is not a pattern, but it's worth watching.
- **Next (B33b, rescoped):** problems hard enough that Haiku errs (5+ steps), so an accuracy difference can show.

## Open question → backlog

Does the card lower accuracy on **multi-step** problems for models that reason in the visible answer? B33 tests 30 multi-step word problems with computed answers, with and without the card.
