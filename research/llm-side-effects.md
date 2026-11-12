# LLM-side risk: can answer-style rules hurt the model's own accuracy?

Research round, 2026-11-12, run because the backlog was empty. The catalogs cover how *people* read. This file covers what style instructions do to the *model*. These findings guide what we test; they are not writing rules, so they are not counted in the coverage ledger.

| Finding | Source | Ev | What it means for brainres |
|---|---|---|---|
| Strict format restrictions degrade LLM reasoning; looser format instructions hurt less, and classification can even improve | Tam et al. 2024, "Let Me Speak Freely?", EMNLP Industry (arXiv 2408.02442) | M | brainres states formats as guidance ("prose for reasoning, steps numbered"), not as rigid schemas. Keep it that way, and don't add hard output templates to the card |
| A universal trade-off between reasoning length and accuracy; "be concise" prompts cut length but cost some accuracy, and sit far from the best achievable trade-off | Lee, Che & Peng 2025 (arXiv 2503.01141), citing Jin 2024, Renze & Guven 2024, Han 2024 | M | Real risk for models without hidden reasoning: shortening the *written* answer can shorten the *reasoning*. Not yet measured on multi-step problems → B33 |
| Longer chain-of-thought is not always better; there is an optimal length | Wu et al. 2025 (arXiv 2502.07266) | M | Brevity isn't automatically harmful. Measure, don't assume |
| Instructions drift within about 8 rounds of dialog. The cause is partly attention decay over long exchanges, and prompting alone is a weak fix | Li et al. 2024, COLM (arXiv 2402.10962) | M | This is the reason we have a per-turn reminder (84 tokens a turn), and we have never measured it on Claude. B46 tests it |
| Multi-turn, underspecified conversations cut task performance by 39% on average, from 90% to 65%. Most of the loss is unreliability (+112%), not aptitude (−16%). Recaps and lower temperature didn't fix it | Laban et al. 2025 (arXiv 2505.06120) | M | Supports "restate what matters from earlier turns" (AN-90). Our evals are mostly single-turn, which is a known blind spot |

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

## B33b result: harder problems

[`evals/hard15.jsonl`](../evals/hard15.jsonl) holds 15 harder problems with answers computed in Python, including inclusion–exclusion, digit sums, trailing zeros in 125!, clock angles, multiset permutations, 1000-day weekday, the probability of at least one six, digit-sum counting, loan amortization, 7^2025 mod 10, derangements and two Korean problems. There were 30 calls; results are in `evals/results/2026-11-12-hard15-haiku/`.

- Both conditions scored **15/15**, and four hard items were checked by hand.
- **Across all 48 problems** (18 traps + 30 multi-step), Haiku was 48/48 with brainres and 48/48 without. That is **no detectable accuracy cost**.
- **Limit:** every run hit the ceiling, so a small cost can't be ruled out. Finding problems Haiku actually fails would take a different source, such as a benchmark subset with known error rates. The card line "brevity applies to the final answer, not to working" was **not** added, because there is no evidence it's needed.
- **Side note:** on the derangement problem the baseline opened with framing ("This is a derangement problem."), while brainres answered first ("**44** of the 120 possible outcomes…").

## Open question → backlog

Does the card lower accuracy on **multi-step** problems for models that reason in the visible answer? B33 tests 30 multi-step word problems with computed answers, with and without the card.
