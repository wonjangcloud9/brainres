# Cognitive principles catalog (source of truth for every brainres rule)

Compiled 2026-11-12. Every rule in `skills/brainres/` must trace to a row here.

**Evidence:** S = strong (meta-analyses / many replications) · M = moderate · W = weak · C = contested / failed replication · † = shown in labs on lists or multimedia; applying it to chat is an extrapolation.

> No controlled experiments exist on formatting LLM chat answers specifically; the only direct human–AI evidence is §7 (#82–85). Numeric thresholds below are engineering defaults to A/B test, not research cutoffs.

## 1. Working memory & cognitive load

| # | Concept | Mechanism | Source | Ev | Rule | Applies | Situation |
|---|---|---|---|---|---|---|---|
| 1 | Cowan 4±1 (replaces Miller 7±2) | WM holds ~3–5 chunks | Cowan 2001, 2010 | S | ≤4 items per list; at ≥5, sub-group under labels | Yes | core |
| 2 | Chunking | Meaningful grouping raises effective capacity | Chase & Simon 1973; Gobet 2001 | S | Label each group; split long IDs/numbers into 3–4 char groups | Yes | core |
| 3 | Extraneous load | Processing not serving the goal consumes WM | Sweller 1988; Sweller et al. 2019 | S | Delete preamble, prompt restatement, meta-talk, sign-offs | Yes | core |
| 4 | Intrinsic load / element interactivity | Difficulty grows with elements held at once | Sweller 2010; Pollock et al. 2002 | S | If ≥3 parts interact: define each in one line, then explain interaction | Yes | explain |
| 5 | Germane load | "Useful effort" | Kalyuga 2011 | C | Never use it to justify added difficulty | No | n/a |
| 6 | Split-attention / spatial contiguity | Integrating separated sources costs WM | Chandler & Sweller 1991; Schroeder & Cenkci 2018 meta | S | Explanation directly after/inside the code it explains; no "see above" | Yes | code |
| 7 | Redundancy | Same content twice adds load | Kalyuga et al. 1998; Adesope & Nesbit 2012 (mixed for text) | M | Don't retell a table in prose; exception: TL;DR on >400 words | Yes | long-form |
| 8 | Expertise reversal | Novice aids slow experts down | Kalyuga et al. 2003 | S | Infer expertise from vocabulary/code; experts get no definitions/analogies | Yes | core |
| 9 | Transient information | Disappearing speech overloads WM | Leahy & Sweller 2011 | M | Voice/TTS only: ≤3 items, short sentences | Partial | voice |
| 10 | Worked example + fading | Solved examples beat unguided solving for novices | Sweller & Cooper 1985; Barbieri 2023 g=.48; Renkl & Atkinson 2003 | S | "How do I…" → one complete example with the user's real values | Yes | procedure |
| 11 | Minimalism | Task-first instruction with error recovery | Carroll 1990; van der Meij & Carroll 1995 | M | Start procedures with the first action; add "If you see X, do Y" | Yes | procedure |

## 2. Mayer's multimedia principles (text-applicable)

| # | Concept | Mechanism | Source | Ev | Rule | Applies | Situation |
|---|---|---|---|---|---|---|---|
| 12 | Coherence | Extra material competes for capacity | Mayer & Fiorella 2014 (median d≈.86); Morkes & Nielsen 1997 (+124% usability) | S | No tangents, history, trivia, hype adjectives | Yes | core |
| 13 | Seductive details | Interesting-but-irrelevant hurts learning | Sundararajan & Adesope 2020 meta | M | Delete fun facts and decorative anecdotes | Yes | core |
| 14 | Signaling | Cues expose structure | Schneider et al. 2018 (g≈.53 retention); Alpizar 2020 d=.38 | S | Headings past ~250 words; preview counts ("Three causes:") | Yes | long-form |
| 15 | Segmenting | Small self-paced units | Rey et al. 2019 meta | M | Numbered steps, one action each; sections ≤~150 words | Yes | procedure |
| 16 | Pre-training | Know the parts before the system | Mayer 2020 | M | Define 1–3 key terms in one line before use | Yes | explain |
| 17 | Multimedia | Words + pictures > words | Mayer 2009 | S† | Spatial/flow content → table or small diagram if rendered | Partial | explain |
| 18 | Personalization | Conversational style lifts retention (d = 0.30) and transfer (d = 0.54), not interest; effects small and n.s. in studies longer than 35 min | Ginns, Martin & Marsh 2013 meta (abstract checked 2026-11-12); Brom 2014 doubts | M | "you"/"I"; conversational, not chatty | Yes | core |
| 19 | Modality, voice, image, embodiment, temporal contiguity | Audio/visual channel effects | Mayer 2020 | — | Not for text | No | n/a |
| 20 | Generative activity | Learner builds meaning | Fiorella & Mayer 2016 | M | Learn mode only: one prediction or explain-back | Yes | learn |

## 3. Attention & reading behaviour

| # | Concept | Mechanism | Source | Ev | Rule | Applies | Situation |
|---|---|---|---|---|---|---|---|
| 21 | Scanning default | 79% scan; read ≤28% of words | Nielsen 1997, 2008 | M | First sentence, headings, bold, bullet openers must carry the answer alone | Yes | core |
| 22 | F-pattern | Attention decays down/right on unformatted text | Nielsen 2006; Pernice 2017 | M | Paragraph ≤4 lines/~80 words; key point first | Yes | core |
| 23 | Layer-cake scanning | Heading-scanning is most efficient | NN/g (Pernice) | M | Headings state content ("Cause: stale cache"), never "Overview" | Yes | long-form |
| 24 | Information scent / spotted pattern | Eyes jump to numbers, code, cue words | NN/g; Pirolli & Card 1999 | M | Bullet's first 2–3 words = key term; numerals | Yes | core |
| 25 | Serial position | First/last remembered best | Murdock 1962; Glanzer & Cunitz 1966 | S† | Most important first, action last; nothing critical in the middle | Yes | core |
| 26 | Isolation (von Restorff) | Distinct item stands out | Hunt 1995 | S | Emphasis only for the thing they must not miss | Yes | core |
| 27 | Signal dilution | Overused cues stop working | Lorch 1989 | M | Bold ≤1 phrase/paragraph, ≤~5% of words; no all-caps | Yes | core |
| 28 | BLUF / inverted pyramid | Conclusion first for skimmers & early stoppers | AR 25-50; Kieras 1980 | M | Sentence 1 answers (yes/no, value, recommendation) | Yes | core |
| 29 | Reading rate | ~238 wpm non-fiction | Brysbaert 2019 meta | S | Facts ≤100 words; explanations ≤300; >500 → headings + TL;DR | Yes | core |
| 30 | Skimming trade-off | Skimming loses anything unsignaled | Rayner et al. 2016 | S | Critical info goes in a signaled spot | Yes | core |
| 31 | Progressive disclosure | Show core, hold the rest | Nielsen 2006 | M | Core answer, then one-line offer of depth | Yes | core |

## 4. Comprehension

| # | Concept | Mechanism | Source | Ev | Rule | Applies | Situation |
|---|---|---|---|---|---|---|---|
| 32 | Schema activation | A frame must exist before integration | Bartlett 1932; Bransford & Johnson 1972 | S | Name the topic before details | Yes | explain |
| 33 | Advance organizer | High-level frame anchors what follows | Ausubel 1960; Luiten et al. 1980 (small) | M | Multi-part answers: one roadmap line | Yes | long-form |
| 34 | Given–new + stress position | New info attaches to known info | Haviland & Clark 1974; Gopen & Swan 1990 | S | Start sentences with the known; end on the new | Yes | core |
| 35 | Situation model | Understanding = mental model | Kintsch 1988; Zwaan & Radvansky 1998 | S | Explain mechanism (X causes Y via Z), not labels | Yes | explain |
| 36 | Causal connectives | Stated relations improve recall | Trabasso & van den Broek 1985; Sanders & Noordman 2000 | S | Keep because/so/but; bullets must not strip causal links | Yes | core |
| 37 | Reverse cohesion | Experts learn more from low-cohesion text | McNamara et al. 1996 | M | Terse for experts; explicit links for novices | Yes | core |
| 38 | Referential clarity | Ambiguous pronouns force inference | Gernsbacher 1989; Coh-Metrix | M | One term per concept; repeat the noun when "it" is ambiguous | Yes | core |
| 39 | Lexical entrainment | Partners converge on shared terms | Brennan & Clark 1996 | S | Reuse the user's words; map corrections once | Yes | core |
| 40 | Curse of knowledge | Experts can't simulate the naive view | Camerer et al. 1989; Birch & Bloom 2007 | S | Define terms the user hasn't used; expand acronyms | Yes | core |
| 41 | Concreteness | Concrete text understood/recalled better | Sadoski et al. 1993 | S | Every abstract claim gets a number, name or command | Yes | core |
| 42 | Dual coding | Verbal + imagery codes add | Paivio 1971; Clark & Paivio 1991 | S/C | Imageable wording; NOT "visual learner" tailoring | Yes | explain |
| 43 | Analogy (structure mapping) | Transfer via relational mapping | Gentner 1983; Gick & Holyoak 1983; Spiro 1989 | S | State the mapping, then where it breaks | Yes | explain |
| 44 | Contrasting cases | Side-by-side exposes key features | Alfieri et al. 2013 meta d≈.50 | S | Distinctions via a minimal pair | Yes | explain |
| 45 | Concreteness fading | Concrete → abstract | Fyfe et al. 2014; Kaminski 2008 (contested) | M | Example → rule → notation | Yes | explain |
| 46 | Narrative advantage | Narrative recalled better | Mar et al. 2021 meta | S | Mechanisms as event sequences with an actor | Yes | explain |
| 47 | Refutation text | Explicit refutation revises misconceptions | Schroeder & Kucera 2022 g=.41 | S | Myth once → false → why it seems right → correct mechanism | Yes | correction |
| 48 | Order of mention | Text order = event order is easier | Clark & Clark 1968 | M | "Do Y, then X", not "Before X, do Y" | Yes | procedure |
| 49 | Self-reference | Self-related info remembered better | Symons & Johnson 1997 meta | S | Examples use the user's project, names, values | Yes | core |
| 50 | Cognitive fit | Representation should match task | Vessey 1991 | M | Table ≥3×≥2; numbered list for sequences; prose for reasoning; code block to copy | Yes | core |

## 5. Processing fluency & language

| # | Concept | Mechanism | Source | Ev | Rule | Applies | Situation |
|---|---|---|---|---|---|---|---|
| 51 | Fluency → trust | Ease mistaken for validity | Reber & Schwarz 1999; Alter & Oppenheimer 2009 | S | Make correct content easy; polish never hides uncertainty | Yes | core |
| 52 | Illusory truth | Repetition raises perceived truth | Hasher 1977; Dechêne 2010 meta | S | Mention a myth at most once, flagged | Yes | correction |
| 53 | Needless complexity | Long words lower perceived intelligence | Oppenheimer 2006 | M | Common word when meaning is equal | Yes | core |
| 54 | Jargon penalty | Jargon lowers fluency even when defined | Bullock et al. 2019; Shulman 2020 | M | Jargon only if the user used it or it's needed for search | Yes | core |
| 55 | Perceptual disfluency | "Hard fonts aid memory" | Diemand-Yauman 2011; Meyer 2015 (16 nulls); Xie 2018 d≈.01 | C | Never make text deliberately hard | No | n/a |
| 56 | Center-embedding | Nested clauses drive difficulty | Martínez, Mollica & Gibson 2022 | S | No clause inside a clause; definitions get their own sentence | Yes | core |
| 57 | Sentence length, nominalization | Long/noun-heavy sentences are harder | Coleman 1964; Spyridakis & Isakson 1998 | W/M | Avg 15–20 words, cap ~30; verbs over nouns | Yes | core |
| 58 | Passive / good-enough parsing | Passives misread more | Ferreira 2003; Martínez 2022 (harmless) | M | Active with named agent by default | Yes | core |
| 59 | Garden paths | Misparses linger | Frazier & Rayner 1982; Christianson 2001 | S | Keep "that"; comma after introductory clause | Yes | core |
| 60 | Negation | Negations processed slower | Clark & Chase 1972; Kaup 2006; Nieuwland & Kuperberg 2008 | S | Positive phrasing; no double negatives; every "don't" has a "do" | Yes | core |
| 61 | Word frequency | Rare words read slower | Brysbaert et al. 2018 | S | High-frequency words | Yes | core |
| 62 | Surprisal | Reading time ∝ log unpredictability | Levy 2008; Smith & Levy 2013; Nieuwland 2018 | S/C | Parallel bullets, consistent formats | Yes | core |
| 63 | Natural frequencies | Counts keep base rates visible | Gigerenzer & Hoffrage 1995; McDowell & Jacobs 2017 meta (4%→24%) | S | "Of 1,000 people…" | Yes | numbers |
| 64 | Absolute vs relative risk | Relative inflates; denominator neglect | Akl 2011 Cochrane; Reyna & Brainerd 2008 | S | Give baseline; same denominator | Yes | numbers |
| 65 | Verbal probability | "Likely" read as 55–90% | Budescu & Wallsten 1985; Wintle 2019 | S | "likely (~70%)" when stakes matter | Yes | numbers |
| 66 | Cooperative principle | Readers assume every word matters | Grice 1975; Sperber & Wilson 1986 | theory | Every caveat implies importance — cut irrelevant ones | Yes | core |

## 6. Memory

| # | Concept | Mechanism | Source | Ev | Rule | Applies | Situation |
|---|---|---|---|---|---|---|---|
| 67 | Elaboration | "Why" links facts | Craik & Lockhart 1972; Dunlosky 2013; Bisra 2018 g≈.55 | S | Attach a "because" to each key fact | Yes | explain |
| 68 | Generation | Self-produced info remembered | Slamecka & Graf 1978; Bertsch 2007 d≈.40 | S | Learn mode: user predicts a step first | Yes | learn |
| 69 | Retrieval practice | Recall strengthens memory | Roediger & Karpicke 2006; Rowland 2014 g≈.50 | S | Learn mode: 1–2 check questions; never in task mode | Yes | learn |
| 70 | Prequestions | Prior question boosts targeted info | St. Hilaire 2024 g=.54; Pan & Carpenter 2023 | M | Learn mode: one key question before explaining | Yes | learn |
| 71 | Supplied summaries | Summaries ≥ full text for main points | Reder & Anderson 1980 | M | >400 words → 2–4 bullet TL;DR on top | Yes | long-form |
| 72 | Hypercorrection | Confident errors corrected best | Butterfield & Metcalfe 2001 | S | Correct confident user errors directly | Yes | correction |
| 73 | Curiosity / prediction error | Info gaps aid encoding | Loewenstein 1994; Gruber et al. 2014 | M | One real puzzle, then resolution; no clickbait | Yes | explain |
| 74 | Metacomprehension illusion | Fluent text inflates felt understanding | Glenberg 1982; Rhodes & Castel 2008 | S | "Reads clearly" ≠ "understood"; offer a check in learn mode | Yes | learn |
| 75 | Zeigarnik | Unfinished tasks recalled better | Zeigarnik 1927; Ghibellini & Meier 2025 meta (no memory effect) | C | No cliffhangers; state remaining next step | Partial | core |
| 76 | Peak-end | Evaluation tracks peak & end | Kahneman 1993; Alaybek 2022 r≈.58 | S† | End on the takeaway or next action, not caveats | Yes | core |

## 7. Decision, motivation & trust

| # | Concept | Mechanism | Source | Ev | Rule | Applies | Situation |
|---|---|---|---|---|---|---|---|
| 77 | Choice overload | Many options can paralyze | Iyengar & Lepper 2000; Scheibehenne 2010 (≈0); Chernev 2015 (moderated) | C | Unclear preferences → ≤3–4 options | Yes | decide |
| 78 | Defaults / recommendation | Recommended option adopted | Jachimowicz 2019 d=.68 | S | Recommend one, say when to deviate | Yes | decide |
| 79 | Framing | Gain/loss shifts choice | Tversky & Kahneman 1981; Many Labs | S | Risks: both frames or neutral counts | Yes | numbers |
| 80 | Anchoring | First number biases | Tversky & Kahneman 1974 | S | Lead with best estimate + range | Yes | numbers |
| 81 | Two-sided refutational | Answering objections persuades | Allen 1991; O'Keefe 1999 | M | Name the strongest objection and answer it | Yes | decide |
| 82 | Numeric uncertainty | Ranges cost little trust; verbal caveats cost more | van der Bles 2020 (n=5,780) | S | Quantify uncertainty instead of stacking caveats | Yes | core |
| 83 | LLM calibration gap | Longer explanations raise confidence regardless of accuracy | Steyvers et al. 2025 *Nat Mach Intell* | M | Length follows content, never certainty | Yes | core |
| 84 | First-person hedging | "I'm not sure, but…" reduces overreliance | Kim et al. 2024 FAccT (N=404, prereg) | M | Hedge locally, first person, at the uncertain claim | Yes | core |
| 85 | Explanation-induced overreliance | Explanations raise acceptance regardless of correctness | Bansal 2021; Lee & See 2004 | M | When unsure, give a way to verify (command, test, source) | Yes | core |
| 86 | Illusion of explanatory depth | People overestimate mechanism grasp | Rozenblit & Keil 2002 | S | "How does X work" → step-by-step causal chain | Yes | explain |
| 87 | Seductive allure | Irrelevant technical detail satisfies | Weisberg 2008; Hopkins 2016 | M | No decorative technical detail | Yes | core |

## 8. Neuroscience (what holds up)

| # | Concept | Mechanism | Source | Ev | Rule | Applies | Situation |
|---|---|---|---|---|---|---|---|
| 88 | Predictive processing | Brain predicts input; errors cost effort | Friston 2010; Clark 2013 | M | Give a roadmap, then deliver on it | Yes | long-form |
| 89 | Reading network (VWFA) | Reading repurposes visual object system | Dehaene & Cohen 2011; Snell 2024 (Bionic Reading null) | S | No "brain-hack" formatting | Yes | core |
| 90 | Mind-wandering / DMN | Off-task episodes rise with difficulty & length; r≈−.21 with comprehension | Smallwood & Schooler 2015; Bonifacci 2023 meta | S | Short, concrete segments tied to the user's goal | Yes | core |

## Neuromyths — never cite or design around

Learning styles/meshing (Pashler 2008) · left/right-brain people (Nielsen 2013) · 8-second goldfish attention · 10-minute attention limit (Bradbury 2016) · Dale's cone percentages · "images 60,000× faster" · "dopamine hits" from formatting · 10% of brain · Miller 7±2 as hard limit · Sans Forgetica, Bionic Reading · backfire effect as reason to avoid corrections (Swire-Thompson 2023).

## Conflict resolution

1. **Brevity vs novice support** (#8,#12 vs #40,#10) → decide by inferred expertise; novices get definitions + one example; nobody gets repetition.
2. **Answer-first vs organizer-first** (#28 vs #32–33) → answer first, then roadmap; frame first only when the answer is unintelligible without it (one line).
3. **Answer-first vs given–new** (#34) → different scales: conclusion first in the answer; known→new inside each sentence.
4. **Bullets vs causal coherence** (#1,#14 vs #36) → bullets for parallel items; prose for reasoning; keep connectives inside bullets.
5. **Fluency vs desirable difficulty** (#51 vs #68–70) → surface always fluent; difficulty only via task structure in learn mode.
6. **Fluency/length vs calibration** (#51,#83) → local numeric/first-person uncertainty; length tied to content.
7. **Uncertainty vs trust** (#82,#84) → specific local hedges, never blanket caveats.
8. **Refutation vs illusory truth** (#47,#52) → myth once, flagged, surrounded by fact.
9. **Completeness vs choice overload** (#77–78) → one default + ≤3 alternatives.
10. **Concreteness vs transfer** (#41,#45) → end the example with the general rule.
11. **Personalization vs coherence** (#18,#12) → conversational, no filler/flattery.
12. **Headings vs short answers** → structure only past ~250 words.

## Primary verification sources

[Ghibellini & Meier 2025](https://ideas.repec.org/a/pal/palcom/v12y2025i1d10.1057_s41599-025-05000-w.html) · [Steyvers et al. 2025](https://arxiv.org/abs/2401.13835) · [Kim et al. 2024](https://www.arxiv.org/abs/2405.00623) · [van der Bles 2020](https://core.ac.uk/download/305110478.pdf) · [Mar et al. 2021](https://pubmed.ncbi.nlm.nih.gov/33410100/) · [Scheibehenne 2010](https://abcwest.cogs.indiana.edu/pmwiki/pdf/scheibehenne.options.2010.pdf) · [Brysbaert 2019](https://www.Gwern.net/doc/psychology/linguistics/2019-brysbaert.pdf) · [Nieuwland 2018](https://www.mpi.nl/publications/item2564015/large-scale-replication-study-reveals-limit-probabilistic-prediction) · [Bonifacci 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9971160/) · [Bullock 2019](https://comm.osu.edu/sites/comm.osu.edu/files/PUS%202019-%20Bullock%20et%20al..pdf) · [Barbieri 2023](https://link.springer.com/content/pdf/10.1007/s10648-023-09745-1.pdf) · [Schroeder & Kucera 2022](https://link.springer.com/content/pdf/10.1007/s10648-021-09656-z.pdf) · [St. Hilaire 2024](https://link.springer.com/10.1007/s10648-023-09814-5) · [Jachimowicz 2019](https://ideas.repec.org/a/cup/bpubpo/v3y2019i02p159-186_00.html) · [Martínez et al. 2022](https://news.mit.edu/2022/legal-writing-understanding-0307) · [Snell 2024](https://pubmed.ncbi.nlm.nih.gov/38723450/) · [Prike et al. 2023](https://www.networkscienceinstitute.org/publications/examining-the-replicability-of-backfire-effects-after-standalone-corrections) · [Alpizar 2020](https://rex.libraries.wsu.edu/esploro/outputs/journalArticle/A-meta-analysis-of-signaling-principle-in/99900601052901842)
