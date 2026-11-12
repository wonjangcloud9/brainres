# Catalog round 3: how people read LLM answers (2025–2026)

Compiled 2026-11-12 during a research round (backlog was empty). Prefix `LR-`. Each source was checked against its arXiv or proceedings abstract.

**Gap that remains:** we found no controlled study comparing bullets with prose, or markdown with plain text, for *comprehension* of chatbot answers. Only benchmarks and preference work exist.

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| LR-01 | Medium length helps catch wrong answers | When the LLM was wrong, medium-length explanations gave higher human accuracy than short or long ones; with correct outputs, length didn't matter | Friedman et al. 2026, "Not Too Short, Not Too Long", IUI MIRAGE workshop (N=24, within-subjects, mixed-effects) | W | Yes | When you might be wrong, keep the key reasoning steps visible. Don't compress to a bare verdict, and don't pad | core |
| LR-02 | Reading patterns track preference | Eye-movement measures differ between preferred and non-preferred LLM responses | OASST-ETC, ETRA 2025 (N=24) | M | No | Descriptive dataset; no writing rule follows from it | n/a |
| LR-03 | Markdown residue in prose | Em dashes persist when markdown is suppressed (0–9.1 per 1k words across 12 models); a fine-tuning signature | Freeburg 2026, "The Last Fingerprint" (arXiv:2603.27006; no human study) | W | No | An AI-style tell, not a comprehension effect; brainres optimizes understanding, not passing as human | n/a |
| LR-04 | Markdown awareness benchmark | LLMs vary in using markdown "for readability" | MDEval, WWW 2025 | W | No | Benchmark of model behavior; no reader comprehension measured | n/a |
| LR-05 | Response outlining | Professionals switch to asking for an outline after an unsatisfying first answer | NN/g response-outlining study (qualitative) | W | Partial | For long deliverables (reports, plans), start with a short outline and fill it in; if the first attempt missed, offer the outline before rewriting | long-form |
| LR-06 | Implicit feedback from gaze and mouse | Gaze and mouse signals improved a reward model from 55% to 64%; gaze behavior was "very diverse" | Chang et al. 2026, arXiv:2606.20482 (N=59) | M | No | Alignment method. A search summary claimed an "early-part attention" finding, but the abstract does not support it, so it is not used | n/a |
