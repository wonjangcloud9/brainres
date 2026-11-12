# Study 2: prose vs bullets for chat answers (pre-registered protocol v1, 2026-11-12)

**Question.** Does the format that brainres rule 5 prescribes help people understand? Rule 5 says reasoning goes in prose with *because / so*, and parallel items go in lists. No published study tests this for chatbot answers ([catalog-round3](../../research/catalog-round3.md)). The rule currently rests on general findings: causal connectives aid recall (#36), bullets fragment reasoning (HC-16), and bullets help item recall but hurt the surrounding text (PL-54).

## Hypotheses (fixed before any data)

| # | Hypothesis | Measure |
|---|---|---|
| H1 | **Interaction:** for *causal* content, prose gives higher "understand" accuracy than bullets; for *parallel* content the format gap is smaller or reversed | Q2 accuracy, format × content |
| H2 | For *parallel* content, bullets let readers find a fact **faster** without losing accuracy | Q1 time to a correct answer, log-transformed |
| E1 | Exploratory: for causal content, are bullets faster to *find* in even when they are worse to *understand*? | Q1 time, causal items |

**Decision rule.** README may say "human evidence supports rule 5" only if H1 holds at α = .05. Results get published whatever they show. If H1 fails, rule 5 keeps its literature basis, and the README says the human test didn't confirm it.

## Materials

- **[`items/`](items/):** 8 topics, each written twice with identical claims, as `prose.md` (with connectives) and `bullets.md` (one claim per bullet).
  - 4 are **causal**: a stale cache, inflation vs savings, a race condition, why HTTPS needs certificates.
  - 4 are **parallel**: speeding up a query, daily git commands, a pre-deploy checklist, account security.
  - Hashes are in `items/MANIFEST.sha256`, and they serve as the pre-registration.
- **Manipulation.** The causal bullet versions drop the explicit *because / so* links but keep every fact that Q2 needs. That is the variable under test, and it reflects how LLMs typically bullet reasoning.
- **Questions** (`quiz.json`):
  - **Q1 (find):** the answer stays visible; we measure time to a correct answer.
  - **Q2 (understand):** the answer is hidden; the question asks for an application or inference.
  - Both versions contain the facts needed for each question. An independent check runs before launch (B36b).

## Design

- **Within-subject.** Each participant reads all 8 topics once. Each topic appears in one format.
- **Balance per participant:** 2 causal-prose, 2 causal-bullets, 2 parallel-prose and 2 parallel-bullets. Lists A and B swap formats, and order is randomized.
- **Embedding.** The page reuses the Study 1 engine. The attention check, confidence ratings and JSON export work the same way.

## Sample, exclusions, analysis

- **Target n = 80.** There are only 2 items per cell per participant. A power simulation on synthetic participants, like the one in Study 1 amendment v1.1, must run **before launch**, and the target can be amended then, before any data.
- **Exclusions** are the same as Study 1: a failed attention check, under 3 minutes, or not fluent.
- **H1:** logistic mixed model, `correct_q2 ~ format * content + (1|participant) + (1|item)`. Fallback: per participant, compute (prose − bullets) accuracy for causal minus the same for parallel, then a one-sample Wilcoxon test against 0.
- **H2:** for parallel items, a paired comparison of log Q1 time on correct trials (bullets vs prose), with Wilcoxon, plus accuracy non-inferiority at a 10 pp margin.

## Known threats

- **The author wrote both versions,** which risks unequal quality. Mitigations: an identical claim inventory per item, an independent equivalence review before launch, and hashes frozen in the manifest.
- **The bullet versions are realistic but not optimal.** A skilled writer might keep connectives inside bullets. This study tests the *typical* LLM bullet style, which is the thing rule 5 targets.
- **Ceiling effects** are possible on the parallel items. H2 uses time as its primary measure for that reason.
