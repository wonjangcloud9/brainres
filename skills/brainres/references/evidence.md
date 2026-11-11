# Evidence behind each rule

Numbers match the full 90-concept catalog in the brainres repo (`research/cognitive-principles.md`).
Ev: S = strong (meta-analyses / many replications), M = moderate, C = contested, † = lab finding extrapolated to chat.

| # | Concept | Key source | Ev | Used in rule |
|---|---|---|---|---|
| 1 | Working memory holds ~4 chunks | Cowan 2001, 2010 | S | 4 |
| 2 | Chunking | Chase & Simon 1973; Gobet 2001 | S | 4 |
| 3 | Extraneous cognitive load | Sweller 1988; Sweller et al. 2019 | S | 1 |
| 6 | Split-attention / spatial contiguity | Chandler & Sweller 1991; Schroeder & Cenkci 2018 (meta) | S | code |
| 8 | Expertise reversal | Kalyuga et al. 2003 | S | fit the reader |
| 10 | Worked example effect | Sweller & Cooper 1985; Barbieri 2023 (g=.48) | S | 7 |
| 14 | Signaling | Schneider et al. 2018 (g≈.53); Alpizar 2020 (d=.38) | S | 6 |
| 15 | Segmenting | Rey et al. 2019 (meta) | M | 5 |
| 16 | Pre-training (define parts first) | Mayer 2020 | M | 8 |
| 21 | Most readers scan (79%; ≤28% of words read) | Nielsen 1997, 2008 | M | self-check |
| 23 | Layer-cake scanning by headings | NN/g (Pernice) | M | 6 |
| 25 | Serial position (primacy/recency) | Murdock 1962; Glanzer & Cunitz 1966 | S† | 2 |
| 26 | Isolation (von Restorff) effect | Hunt 1995 | S | 6 |
| 27 | Signal dilution | Lorch 1989 | M | 6 |
| 28 | BLUF / inverted pyramid | AR 25-50; Kieras 1980 | M | 1 |
| 29 | Reading rate ~238 wpm | Brysbaert 2019 (meta) | S | 3 |
| 35 | Situation model | Kintsch 1988; Zwaan & Radvansky 1998 | S | explaining |
| 36 | Causal connectives aid recall | Trabasso & van den Broek 1985; Sanders & Noordman 2000 | S | 5 |
| 37 | Reverse cohesion (experts) | McNamara et al. 1996 | M | fit the reader |
| 38 | Referential clarity | Gernsbacher 1989 | M | 8 |
| 39 | Lexical entrainment | Brennan & Clark 1996 | S | 8 |
| 40 | Curse of knowledge | Camerer et al. 1989; Birch & Bloom 2007 | S | 8 |
| 41 | Concreteness effect | Sadoski et al. 1993 | S | 7 |
| 43 | Analogy as structure mapping | Gentner 1983; Gick & Holyoak 1983 | S | explaining |
| 44 | Contrasting cases | Alfieri et al. 2013 (meta, d≈.50) | S | explaining |
| 46 | Narrative advantage | Mar et al. 2021 (meta) | S | explaining |
| 47 | Refutation text | Schroeder & Kucera 2022 (g=.41) | S | explaining |
| 48 | Order of mention | Clark & Clark 1968 | M | explaining |
| 49 | Self-reference effect | Symons & Johnson 1997 (meta) | S | 7 |
| 50 | Cognitive fit (format ↔ task) | Vessey 1991 | M | 5 |
| 52 | Illusory truth (repetition) | Hasher 1977; Dechêne 2010 (meta) | S | explaining |
| 56 | Center-embedding difficulty | Martínez, Mollica & Gibson 2022 | S | 10 |
| 57 | Sentence length, nominalization | Coleman 1964; Spyridakis & Isakson 1998 | W/M | 10 |
| 60 | Negation processing cost | Clark & Chase 1972; Kaup 2006 | S | 10 |
| 61 | Word frequency effect | Brysbaert et al. 2018 | S | 10 |
| 63 | Natural frequencies | Gigerenzer & Hoffrage 1995; McDowell & Jacobs 2017 (meta) | S | numbers |
| 64 | Absolute vs relative risk | Akl 2011 (Cochrane) | S | numbers |
| 65 | Verbal probability is vague ("likely" = 55–90%) | Budescu & Wallsten 1985 | S | 9 |
| 68–70 | Generation, retrieval practice, prequestions | Bertsch 2007; Rowland 2014; St. Hilaire 2024 | S/M | learn mode |
| 71 | Supplied summaries | Reder & Anderson 1980 | M | 3 |
| 76 | Peak-end rule | Kahneman 1993; Alaybek 2022 | S† | 2 |
| 77 | Choice overload (moderated) | Scheibehenne 2010; Chernev 2015 | C | options |
| 78 | Defaults / recommendations | Jachimowicz 2019 (d=.68) | S | options |
| 80 | Anchoring | Tversky & Kahneman 1974 | S | numbers |
| 82 | Numeric uncertainty costs little trust | van der Bles 2020 (n=5,780) | S | 9 |
| 83 | Longer LLM answers raise confidence regardless of accuracy | Steyvers et al. 2025 | M | 3 |
| 84 | First-person hedging reduces overreliance | Kim et al. 2024 (FAccT, preregistered) | M | 9 |
| 85 | Explanations raise acceptance even when wrong | Bansal 2021 | M | 9 |
| 86 | Illusion of explanatory depth | Rozenblit & Keil 2002 | S | explaining |
| 89 | Bionic Reading null result | Snell 2024 | S | evidence discipline |

## Neuromyths brainres refuses to use

Learning styles · left/right-brain people · 8-second attention span · 10-minute attention limit · Dale's cone percentages · "images processed 60,000× faster" · "dopamine hits" from formatting · 10% of the brain · Miller's 7±2 as a hard limit · Bionic Reading / Sans Forgetica · avoiding corrections because of a "backfire effect".

## Honest limits

No controlled study has tested formatting rules on LLM chat answers specifically. Thresholds (≤4 items, ≤100/300/500 words, 15–20 words per sentence) are engineering defaults derived from the findings above, to be tuned by evaluation.
