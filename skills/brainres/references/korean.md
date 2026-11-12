# 한국어 답변 (Korean output) and non-native readers

Korean evidence is mostly small studies (M/W). Treat these rules as strong defaults, not laws. The 어절 thresholds (an average of ≤12, flagged above 20) are engineering defaults: no Korean experiment manipulating sentence length was found (KR-01, KR-05).

## Speech level

- **Default to 해요체.** Use 합쇼체 for formal documents. Switch to 반말 only when the user asks, then keep it consistent. Conversational does not mean 반말. (EM-112, HC-112)
- **Use one speech level per answer.** Attach -시- only to human subjects. Never honor objects: no "함수가 반환하십니다". (PL-87)

## Sentence shape

- **Use canonical SOV with explicit case particles.** Don't front the object. (PL-86)
- **Put long arguments and adverbials before short ones.** Don't import English end-weight order. (PL-84)
- **Limit each noun to one short 관형절 (about 10 syllables or fewer).** Anything longer gets its own sentence. (PL-85)
- **Cut 번역투.** Use active voice instead of "~에 의해 ~되다". Don't chain 그/그녀/그것. Drop "~하는 것이 중요합니다" boilerplate, and avoid ~를 가지다 and ~에 있어서. (PL-88)
- **End action bullets with a verb (~하세요),** not stacked nouns (개조식 noun endings). (HC-114)

## Words

- **Prefer common words to rare 한자어 or English loanwords with the same meaning** (쉬운 공공언어). (HC-113)
- **Established loanword terms (서버, 캐시) act as cognates; use them.** (PL-78)
- **Gloss an ambiguous Sino-Korean technical term once:** "정합성(consistency)". (PL-89)
- **Spell a technical compound the same way throughout the answer.** Leaving it unspaced is allowed (맞춤법 §50). (PL-83)
- **Keep identifiers and product names in Latin script.** Don't switch language mid-clause for ordinary words: write "배포하면", not "deploy하면", unless "deploy" is the user's own term. (PL-81)
- **Put the key term in the first 1–2 eojeol of each bullet or heading.** (PL-82)

## Non-native readers (any language)

- **Apply the word-frequency rules more strictly,** roughly the top 3,000 words, and shorten sentences. (PL-75)
- **At most 1 unfamiliar word per ~50 words,** and gloss domain terms inline. (PL-76)
- **Replace idioms ("under the hood") and phrasal verbs ("figure out")** with literal single-word verbs. (PL-77)
- **No ellipsis, reduced relatives or long-distance pronouns.** (PL-79)
- **Offer mnemonics for arbitrary vocabulary only on request,** spelling out each letter of an acronym. (LS-80)

## Directness and politeness (round 2 research)

- **Keep the content direct and the ending polite.** Korean politeness lives in the speech level, not in vaguer content, and hints are read as *less* polite because they are unclear. (CC-05, CC-04)
- **Don't rely on implicature.** Korean readers read more into what is left unsaid. If the user's worry turns out to be fine, say so outright ("X는 문제없어요"), and state priorities explicitly ("가장 중요한 것: …"). (CC-03, CC-07)
- **Refusals:** put one regret word inside sentence 1 ("아쉽지만 그 방식은 안 돼요"), then the reason and an alternative. Don't pad. (CC-06)
- **Uncertainty gets its own clause:** "미확인: 3.2 이후 동작". L2 readers miss hedges carried only by a modal ending. Never put '-것 같습니다' on a verified fact; use it only for real uncertainty, and say what is uncertain. (CC-08, CC-10)
- **Probability words:** don't rely on 가능성 높음 alone. Give a grounded number or name what is unverified. Never invent a percentage. (CC-09)
- **Use 두괄식, not 기승전결.** The conclusion comes first, then the background. (CC-11)

## Readability research (round 4)

- **Fix words and structure together.** Replace a rare 한자어 *and* split the long sentence; Korean difficulty measures weigh both. Long sentences and hard Sino-Korean words are also the two most common public complaints. (KR-02, KR-04)
- **Break long compound-noun chains in technical Korean.** Write "사용자 권한 설정 변경 요청 처리" as a phrase with particles ("사용자 권한 설정을 바꾸는 요청을 처리"), because long 어절 slow reading in hard texts. (KR-03)
