# Catalog round 7: streaming answers (and a gap)

Compiled 2026-11-12 in a research round (the backlog was empty). Prefix `ST-`. LLM chat answers appear token by token, so readers see sentence 1 before the rest exists. We searched for studies of how streaming changes reading, comprehension or trust.

**Main finding: the gap.** We found no controlled study comparing streamed with fully displayed LLM answers on comprehension or trust. The nearest work, listed below, is about pacing, response delay or showing several answers. Our rules for streaming therefore rest on general findings (#28, NW-06) and on our own eval failure C17, not on streaming experiments.

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| ST-01 | Readers act on partially streamed text | Practitioner reports: users read and act on the first streamed sentences before the answer finishes, so a claim the model later revises has already been read as final | tianpan.co engineering blog, 2026 (two posts; opinion, no experiment) | W | Partial | Sentence 1 must stand on its own. Never state a value and then correct it later in the same answer (see C17) | core |
| ST-02 | Cognitive-load-aware streaming pace | Pacing output by estimated reading load saved up to 16.8% compute in a crowdsourced study, with satisfaction monitored; comprehension was not measured | Xiao & Yang 2025, arXiv 2504.17999 (abstract) | W | No | A serving-side choice; the answer's text can't control pace | n/a |
| ST-03 | Chatbot response delay | Dynamic delays raised perceived humanness and satisfaction in one study (Gnewuch et al. 2018). Effects were opposing and differed between novices and experts in a 202-person lab study (Gnewuch et al. 2022, BISE) | Gnewuch et al. 2018 ECIS; 2022 BISE (abstracts) | M | No | System-level timing, not answer text | n/a |
| ST-04 | Showing several sampled answers | Showing 10 responses instead of 1 changed trust and reliance, and a cognitive-support aid moderated the effect | Swoopes, Holloway & Glassman 2025, arXiv 2503.16114 (abstract) | W | No | An interface design; brainres writes one answer | n/a |
