# Which rules earn a place on the always-on card?

The card goes into every session (631 tokens in v1, measured), so each line has to earn its tokens.
Every candidate behavior from the 725-finding catalogs is ranked with the same RICE formula as the backlog:

- **Reach** is the share of answers the rule affects.
- **Impact** is the comprehension or decision gain per affected answer.
- **Confidence** is the evidence grade of the best supporting finding.
- **Effort** is fixed at 1 because every line costs about the same tokens, so score = R × I × C.

Rules that only matter in one situation stay in the skill's reference files. They load when that situation comes up.

| Rank | Behavior | Key findings | R | I | C | Score | On card v2 |
|---|---|---|---|---|---|---|---|
| 1 | Answer in sentence 1; yes/no first | #28, EM-102, PL-57, AN-49 | 10 | 3 | 0.8 | 24 | ✓ |
| 2 | Agree only with evidence; check the premise | JD-102 (S), JD-11 (S) | 10 | 3 | 0.8 | 24 | ✓ |
| 3 | Fit the reader's expertise | #8 (S), #40 (S) | 10 | 2 | 1.0 | 20 | ✓ |
| 4 | Concrete, with the user's own values; worked example | #41 (S), #49 (S), #10 (S) | 8 | 2 | 1.0 | 16 | ✓ |
| 5 | Length follows content; never pad | #83, HC-97, HC-99, #29 (S) | 10 | 2 | 0.8 | 16 | ✓ |
| 6 | ≤4 items per group | #1 (S), #2 (S) | 8 | 2 | 1.0 | 16 | ✓ |
| 7 | Prose for reasoning, lists for steps, tables for comparisons | #50, #36 (S), HC-13 | 8 | 2 | 0.8 | 12.8 | ✓ |
| 8 | Uncertainty once, in the claim, as a number, plus a check | #82 (S), #84, JD-95, #85 | 8 | 2 | 0.8 | 12.8 | ✓ |
| 9 | Keep code, numbers, errors, negations, safety verbatim | caveman/terse survey, PL-04 | 5 | 3 | 0.8 | 12 | ✓ |
| 10 | End on the next action | #25, #76 (S†) | 10 | 1 | 0.8 | 8 | ✓ |
| 11 | Plain sentences (one idea, active, positive) | #56 (S), #60 (S), PL-17 | 10 | 1 | 0.8 | 8 | ✓ |
| 12 | One word per concept; define before use | PL-33, #39 (S), #16 | 8 | 1 | 0.8 | 6.4 | ✓ (merged into 3) |
| 13 | Bold only the token that harms if misread | #26 (S), #27, PL-50 | 6 | 1 | 0.8 | 4.8 | ✓ (merged into 11) |
| 14 | No flattery / "simply / obviously" | EM-40, EM-34 | 5 | 1 | 0.5 | 2.5 | ✓ (merged into 2) |
| 15 | Clarify only if the answer would change | EM-109, EM-104 | 3 | 2 | 0.5 | 3 | — skill |
| 16 | Headings only past ~250 words | #14, #23 | 3 | 1 | 0.8 | 2.4 | — skill |
| 17 | Stress mode: one action first, ≤5 steps | AN-35 (S) | 1 | 3 | 1.0 | 3 | — skill (support.md) |
| 18 | Korean: one speech level, ≤12 어절, no 번역투 | PL-87, PL-88, PL-85 + eval | 5 | 2 | 0.8 | 8 | ✓ v2.1 (merged into 10) |

The cut line is a score of about 4, with merges, so the card holds 11 lines. Everything below the line is still applied: the skill and its references cite all 596 applicable findings.

**v2.1 (2026-11-12):** the first eval showed Korean answers running past the 어절 limit: 2 of 4 had sentences over 20 어절, because the Korean rules lived only in `korean.md`. Re-scored with that evidence (Reach 5 for a Korean-speaking owner and users, Confidence 0.8), the Korean line moved onto the card inside rule 10, at a cost of +43 tokens (418 → 461). In the re-run, 0 of 8 Korean answers had long sentences, and the mean Korean Brain Score went from 89.2 to 93.9 (`evals/results/*-c12-korean/`).
