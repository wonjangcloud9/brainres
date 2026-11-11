# Human comprehension benchmark: pre-registered protocol (v1, 2026-11-12)

**Question.** For the same question, do people find and understand answers faster and as accurately when Claude writes with brainres as when it writes by default?

Every eval so far counts rule violations (`brainlint`) or tokens. This benchmark measures people. It is the claim that no answer-style skill has tested yet ([survey](../research/trending-skills.md)).

## Hypotheses (fixed before any data)

| # | Hypothesis | Test |
|---|---|---|
| H1 | Readers find the key fact **faster** in brainres answers | Q1 time-to-correct, log-transformed, mixed model |
| H2 | Comprehension is **not worse** with brainres (non-inferiority margin: 5 percentage points) | Q2 accuracy, one-sided |
| H3 | Confidence is **better calibrated** with brainres (smaller confidence−accuracy gap) | Brier score on Q1+Q2 |
| E1 | Exploratory: which version readers prefer when shown both | Paired preference on 2 items |

**Decision rule.** README claims "improves comprehension" only if H1 is significant (α = .05) **and** H2 holds. Results get published whatever they show, including null and negative results.

## Materials

- **Items:** [`items/`](items/) holds 12 frozen answer pairs (8 English, 4 Korean) from [`evals/`](../evals/). The baseline is Claude Code's default; the brainres version uses the current card. Both are Sonnet answers to the identical question. File hashes are in [`items/MANIFEST.sha256`](items/MANIFEST.sha256), and these hashes are the pre-registration.
- **Questions:** 2 per item, in `items/<id>/quiz.json` (B10-2).
  - **Q1, find:** a fact that **both** versions contain. The answer stays visible, and we measure time to a correct answer.
  - **Q2, understand:** an inference or application question that **both** versions support. The answer is hidden, and we measure accuracy.
  - **Confidence:** 1–5 after each question.
- **Question fairness:**
  - Questions are written so both versions answer them. A second reviewer checks this before data collection.
  - Any item that one version can't answer is dropped before launch, and the drop is logged.

## Design

- **Within-subject, counterbalanced.** Each participant sees every item once, in one version. Lists A and B swap versions, so each participant sees half baseline and half brainres. Item order is randomized.
- **Language:** participants pick the English set (8 items) or the Korean set (4 items). The Korean set is exploratory because of its size.
- **Attention check:** one item with an instructed answer.

## Sample and power

- **Target:** 60 participants for the English set.
- **Power:** a within-subject effect of d = 0.4 on time needs about 52 for 80% power at α = .05, paired.
- **Exclusions, decided now:**
  - a failed attention check;
  - total time under 3 minutes;
  - not fluent in the chosen language (self-report).

## Analysis plan

- **H1:** linear mixed model, `log(time) ~ condition + (1|participant) + (1|item)`.
- **H2:** logistic mixed model, `correct ~ condition + (1|participant) + (1|item)`. Non-inferiority holds if the lower 95% bound of the difference is above −5 pp.
- **H3:** Brier score per participant × condition, compared with a paired Wilcoxon test.
- **Fallback if the models don't converge:** per-participant means of brainres items versus baseline items, with a paired Wilcoxon test.

## Privacy

There are no accounts or names. Each participant gets a random ID, and results contain only choices, confidence and timings. Submission is opt-in, by attaching the exported JSON to a GitHub issue (B10-3).

## Known threats

- The brainres author writes the questions. Mitigations: an independent reviewer, questions frozen by commit hash before collection, and the both-versions-answer rule.
- One sample per condition may favor or disfavor brainres by chance. Mitigation: items come from the first sample of each run, picked mechanically and not by quality.
- Volunteers recruited from the repo audience may prefer brainres. Mitigation: versions are unlabeled, and the primary measures are behavioral (time, accuracy), not preference.
