# Research round 10: ISO 24495-1 clause check (2026-11-13)

**Question:** does the ISO plain-language standard contain a guideline our answer rules miss?

**Sources:**
- The standard's table of contents, from a free DIN preview of ISO 24495-1:2023. Clause titles were extracted from the PDF.
- Public descriptions of the four governing principles.

The guideline texts themselves are paywalled and weren't read. Several 5.1, 5.2 and 5.4 subclause titles didn't extract from the PDF, so they are left out here rather than guessed.

**Result:** no new findings. Every guideline title we could verify maps to an existing rule or finding. The one gap is reader testing, which was already known.

| ISO 24495-1 clause (verified title) | Where brainres already covers it |
|---|---|
| 4 Governing principles: relevant, findable, understandable, usable | HC-87 (four-question check) |
| 5.1.6 Select content that readers need | Card rules 3 and 5 (fit expertise, length follows content); Y1 budgets |
| 5.2.2 Structure the document for readers | Card rules 1, 6 and 7 (answer first, ≤4 per group, steps numbered, tables) |
| 5.3.2 Choose familiar words | Card rule 3 (novices get terms defined first); U1 found few undefined terms |
| 5.3.3 Write clear sentences | Card rule 10 (one idea, active, positive) |
| 5.3.4 Write concise sentences | Card rule 10; `sentence_length` and `long_sentences` checks (S1) |
| 5.3.5 Write clear and concise paragraphs | `wall_of_text` check (K1) |
| 5.3.6 Consider including images and multimedia | Comparisons in tables (rule 7); diagram cognition in catalog-round2 |
| 5.3.7 Project a respectful tone | PN-01 (politeness); refutation that doesn't blame the person (#47, JD-78) |
| 5.3.8 Ensure that the document is cohesive | Card rule 7 (because/so/but); `fragmented_reasoning` check |
| 5.4.3 Evaluate the document further with readers | **Gap, already known:** `bench/` (study 1 and the pre-registered study 2) is ready but has no participants. It needs GitHub Pages (owner item D6) and people. |
| 5.4.4 Continue to evaluate readers' use of the document | The `[hard-to-read]` issue form feeds `evals/suite-community.jsonl` (D11) |

**Backlog:** nothing new for the loop. Testing with readers needs Pages and participants, both owner items.

**Saturation note:** rounds 6–10 added 0–2 findings each, and this round added none. Research is no longer where improvement comes from. The next scheduled scan is the monthly trending-skills check (2026-12).
