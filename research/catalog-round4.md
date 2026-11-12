# Catalog round 4: Korean readability research

Compiled 2026-11-12 during a research round (the backlog was empty). Prefix `KR-`. Sources were found through KCI and koreascience abstracts and the 국립국어원 site. Full texts were mostly paywalled.

**Main finding: the gap.** No study was found that manipulates Korean sentence length in 어절 and measures comprehension. brainres's Korean thresholds (an average of ≤12 어절, flagged above 20) are therefore **engineering defaults** derived from general findings (#57, PL-85), not Korean experimental cutoffs.

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| KR-01 | Length metrics index Korean text difficulty | Paragraph, sentence and word length work as readability indices for Korean | 홍정하 외 2011, 『언어정보』 12 | W | Yes | Keep Korean sentences and paragraphs short; split any sentence over ~20 어절 (a default threshold, not an experimental cutoff) | korean-L2 |
| KR-02 | Sentence complexity and vocabulary difficulty co-vary | Korean readability formulas combine grammatical complexity and vocabulary grade; both correlated with difficulty in TOPIK and academic texts | 서혁 2013; Lee 2020 formula; 김장식 2012 (TOPIK) | W | Yes | Simplify words and structure together: replace a rare 한자어 *and* split the sentence, since one without the other helps less | korean-L2 |
| KR-03 | 어절 length affects fixation time in hard texts | Longer 어절 → longer single fixations when the text is difficult | Korean eye-tracking study (Korean J. Cognitive Science, 2013) | M | Partial | Break long compound 어절 chains (명사+명사+명사+조사) in technical Korean into a phrase with particles | korean-L2 |
| KR-04 | Long sentences are the top public complaint | 50.8% named "complex, long sentences" and 48.2% "difficult Sino-Korean words" as the main problems of public language | 2020 public-language survey (via 국립국어원 / ditoday report) | W | Yes | Treat long sentences and rare 한자어 as the first two things to fix in Korean answers | korean-L2 |
| KR-05 | Official guidelines give no numeric length cap | 국립국어원 『쉬운 공문서 쓰기 길잡이』 says to write briefly, but no number was found | 국립국어원 (search, 2026-11-12) | W | No | No number to adopt, so our threshold stays a labelled default | n/a |
