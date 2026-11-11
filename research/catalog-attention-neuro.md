# Catalog AN — attention, executive function, cognitive neuroscience, neurodiversity

Compiled 2026-11-12. IDs `AN-nn`. Ev: S strong · M moderate · W weak · C contested/failed.
Duplicates marked `No` with the original ID. New neuromyths are listed at the end.

## A. Attention networks, capture, emphasis

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| AN-01 | Phasic alerting trade-off | Warnings speed responses but raise errors | Posner 1975; Callejas 2004 | M | Partial | Urgency markers only when the action is time-critical | core |
| AN-02 | Endogenous cue validity | Invalid cues cost more than no cue | Posner 1980 | S | Yes | Every heading or lead-in predicts what follows; no teaser headings | core |
| AN-03 | Salient-singleton capture | Unique features capture attention even when irrelevant | Theeuwes 1992; Treisman & Gelade 1980; Wolfe 2021 | S | Yes | Salience only on decision-critical tokens, marked with one feature (bold), never bold+italic+emoji+caps | core |
| AN-04 | Contingent capture | Only goal-matching features capture | Folk, Remington & Johnston 1992 | S | Yes | Headings and labels reuse the key nouns from the user's question | core |
| AN-05 | Over-signaling dose | — | Lorch 1995 | M | No | Duplicate of #27 | n/a |
| AN-06 | Orienting habituation | — | Anderson 2016; Vance 2018 | M | No | Duplicate of JD-91 | n/a |

## B. Selective attention, blindness, vigilance

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| AN-07 | Inattentional blindness | Items outside the attentional set go unseen | Simons & Chabris 1999; Most 2005 | S | Yes | Each caveat in the same line as the action it governs, not a trailing "Notes" | procedure |
| AN-08 | Change blindness | Changes between versions go unnoticed | Rensink 1997; Simons & Levin 1998 | S | Yes | Re-emitting revised code/text → list every change first ("Changed: X → Y"); small edits → only changed lines | code |
| AN-09 | Load theory | High WM load increases distractor interference | Lavie et al. 2004; Lavie 2005 | S | Yes | Memory-heavy answers (math, debugging, multi-step): no asides; extras after the result | numbers |
| AN-10 | Vigilance decrement | Rare critical signals missed late | Mackworth 1948; Warm 2008 | S | Partial | A rare critical item never appears only late: state it at the top and where it applies | long-form |
| AN-11 | Attentional blink | Misses in rapid serial streams | Raymond et al. 1992 | S | No | Reading is self-paced | n/a |

## C. Task switching, interruptions, prospective memory

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| AN-12 | Task-switch cost | Switching task sets costs time; cues reduce it | Rogers & Monsell 1995; Kiesel 2010 | S | Yes | Group by mode (Why: / Do: / Check:); never alternate why and do sentence by sentence | procedure |
| AN-13 | Memory for goals / resumption lag | Suspended goals decay; resumption needs cues | Altmann & Trafton 2002 | S | Yes | Numbered steps with checkpoint states ("You should now see X") | procedure |
| AN-14 | Placekeeping disruption | 3–4 s interruptions double–triple sequence errors | Altmann, Trafton & Hambrick 2014 | S | Yes | No digressions between numbered steps; background before step 1 or after the last | procedure |
| AN-15 | Interrupted work | Compensation by speed, at the cost of stress | Mark et al. 2008 | M | Partial | Don't stop the user with an avoidable question; state the default and proceed | decide |
| AN-16 | Central bottleneck (PRP) | Two decisions can't run in parallel | Pashler 1994 | S | Partial | At most one blocking question per message; others numbered, blocking first | decide |
| AN-17 | Media-multitasker deficit | Small, unreplicated | Ophir 2009; Wiradhany & Nieuwenstein 2017 | C | No | Don't infer deficits from self-descriptions | n/a |
| AN-18 | Prospective memory | Event cues beat time cues | Einstein & McDaniel 2005; Chen 2015 meta | S | Yes | Deferred actions on a "Later:" line with an event trigger ("after deploy succeeds, delete flag X") | procedure |
| AN-19 | Goal neglect | More instruction parts → requirements dropped | Duncan et al. 1996, 2008 | M | Yes | Restate a constraint at the step where it applies; ≤3 global rules per procedure | procedure |
| AN-20 | Dual-task cost of voice | Voice interaction distracts (e.g., driving) | Strayer & Johnston 2001; Strayer 2013 | S | Yes | One item per utterance, lists ≤3, never read codes/URLs aloud | voice |

## D. Working-memory updating, interference, cognitive control

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| AN-21 | Proactive interference & release | Old items intrude; category change releases | Keppel & Underwood 1962; Wickens 1970; Jonides & Nee 2006 | S | Yes | Retract explicitly ("Replace the v1 command with:"); never show old and new unlabeled side by side | correction |
| AN-22 | Similarity-based interference | Similar items compete at retrieval | Van Dyke & McElree 2006; Oberauer 2012 | S | Yes | Distinct names for distinct things (no `data1`/`data2`); one name per thing | code |
| AN-23 | WM span vs comprehension | Low-span readers integrate poorly over distance | Daneman & Merikle 1996 (r≈.4) | S | Yes | Use the noun, not "it/this", when the antecedent is >1 sentence back or ambiguous | core |
| AN-24 | Dependency locality & pupillary effort | Long subject–verb gaps raise WM cost | Gibson 1998; Futrell 2015; Just & Carpenter 1993 | S | Yes | Subject and verb within ~8 words (extends #56) | core |
| AN-25 | Stroop-type format conflict | Incongruent dimensions cause errors | MacLeod 1991; Botvinick 2001 | S/W | Partial | ✓ and green only for do/success, ✗ and red only for don't/fail; never "✓ Don't…" | core |
| AN-26 | Consistent mapping → automaticity | Only consistent mappings become automatic | Schneider & Shiffrin 1977 | S | Yes | Fixed conventions: `code` = literal, **bold** = must-not-miss; stable section order | core |
| AN-27 | Stimulus–response compatibility | Display order should match response order | Fitts & Seeger 1953; Proctor & Vu 2006 | S/W | Partial | Same option order and labels across summary, table and recommendation | decide |
| AN-28 | Unity/diversity of EF | Updating, shifting, inhibition separable | Miyake et al. 2000 | S | Partial | Audit: count values to track, mode switches, defaults to override; minimize each | core |

## E. Effort, fatigue, stress, anxiety

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| AN-29 | Effort cost / demand avoidance | Effort spent by expected value | Kool 2010; Shenhav 2013; Westbrook 2013 | S | Yes | First line states payoff and cost ("3 steps, ~5 min, fixes X"); recommended path = least-effort path | core |
| AN-30 | Ego depletion | — | Hagger 2016 | C | No | Duplicate of JD-116 | n/a |
| AN-31 | Mental fatigue | Sustained effort raises felt cost | Boksem & Tops 2008; Wiehler 2022 | M/W | Partial | Long sessions or fatigue signals → re-summarize current state in ≤3 lines first | long-form |
| AN-32 | Decision fatigue | — | Glöckner 2016 | C | No | Duplicate of JD-116 | n/a |
| AN-33 | Choice overload | — | Chernev 2015 | C | No | Duplicate of #77 | n/a |
| AN-34 | Yerkes–Dodson | Original data don't support a general inverted-U | Teigen 1994; Corbett 2015 | C | No | Never add pressure to "optimize arousal" | n/a |
| AN-35 | Acute stress → prefrontal impairment | Catecholamines impair PFC, WM, flexibility | Arnsten 2009; Shields 2016; Lim & Dinges 2010 | S | Yes | Stress/emergency/exhaustion → single next action first, then ≤5 short imperative steps, no branching, explanation after | emotion-support |
| AN-36 | Stress → habit shift | Stress biases toward habitual action | Schwabe & Wolf 2009 | M | Partial | If the habitual move is harmful, say so up top ("Don't restart the DB yet") | emotion-support |
| AN-37 | Controllability | Perceived control buffers stress | Maier & Seligman 2016 | M | Yes | Bad news: what the user can do, within the first 2 sentences | emotion-support |
| AN-38 | Uncertainty worse than known bad | Stress tracks outcome uncertainty | de Berker et al. 2016 | M | Yes | Verdict first, even if bad; if unknown, say what's unknown and when it will be known | correction |
| AN-39 | Attentional control theory | — | Eysenck 2007 | S | No | Duplicate of EM-08 | n/a |
| AN-40 | Threat attentional bias | Anxious people attend to threat | Bar-Haim 2007 (d≈.45) | S | Yes | Severity words only when calibrated, always with magnitude + action | emotion-support |
| AN-41 | Math anxiety | — | Ashcraft & Kirk 2001 | S | No | Duplicate of EM-09 | n/a |
| AN-42 | Validation | — | Shenk & Fruzzetti 2011 | M | No | Duplicate of EM-74 | n/a |
| AN-43 | Affect labeling | — | Lieberman 2007 | M | No | Duplicate of EM-75 | n/a |
| AN-44 | Scarcity "bandwidth tax" | Low evidentiary value on audit | Mani 2013; O'Donnell 2021 | C | No | Excluded | n/a |

## F. Emotion, reward, novelty, information-seeking

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| AN-45 | Emotional memory trade-off | Arousal strengthens center, weakens periphery | Kensinger 2007; McGaugh 2004 | S | Yes | Put the action inside the warning sentence ("Back up X before running Y") | procedure |
| AN-46 | Negativity bias | — | Baumeister 2001 | S | No | Duplicate of EM-07 | n/a |
| AN-47 | Emotion-word speed | Conflicting findings | Kousta 2009; Estes & Adelman 2008 | C | No | Excluded | n/a |
| AN-48 | Reward prediction error, done right | Dopamine = prediction error, not pleasure | Schultz 1997; Berridge & Robinson 1998 | S | Partial | Surprise only when the surprising fact is the thing to learn; no manufactured suspense | learn |
| AN-49 | Preference for advance information | Early resolution valued; dopamine signals it | Bromberg-Martin & Hikosaka 2009; Bennett 2016 | S | Yes | Outcome before method; never make the reader wait for the verdict (neural support for BLUF) | core |
| AN-50 | Ostrich effect | Bad news avoided when coping seems low | Sweeny 2010; Charpentier 2018; Karlsson 2009 | M | Yes | Pair bad news with an actionable next step in the same paragraph | correction |
| AN-51 | Curiosity inverted-U | Peaks at intermediate confidence | Kang et al. 2009; Kidd & Hayden 2015 | M | Partial | "Why?" first only in learn mode with partial knowledge; novices get the answer directly | learn |
| AN-52 | Ambiguity aversion | — | Hsu 2005 | S/M | No | Duplicate of JD-25 | n/a |
| AN-53 | Novelty → encoding boost | Novelty tags nearby information | Lisman & Grace 2005; Ballarini 2009 | M/W | Partial | At most one genuinely novel concrete example next to the key idea; no gimmicks | learn |
| AN-54 | Seductive allure of neuroscience | — | Weisberg 2008 | M | No | Duplicate of #87 (never back claims with "your brain…" talk) | n/a |

## G. Cognitive aging & time of day

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| AN-55 | Processing-speed decline | Slower processing limits WM | Salthouse 1996 | S | Yes | Older reader signals: one idea per sentence, ≤5 steps per block, no time-pressure wording | accessibility |
| AN-56 | Inhibitory deficit | Interleaved irrelevant text slows older readers | Hasher & Zacks 1988; Connelly et al. 1991 | M | Yes | No mid-sentence asides; side information after the point | core |
| AN-57 | Environmental support | Recognition cues shrink age deficits | Craik 1986 | S | Yes | Repeat the value instead of "use the value from step 2" | procedure |
| AN-58 | Reliance on predictability | Older readers lean on context | Rayner et al. 2006 | M | Partial | Familiar phrasing, normal word order | accessibility |
| AN-59 | Crystallized knowledge preserved | Vocabulary holds or grows with age | Salthouse 2010; Ramscar 2014 | S | Yes | Reduce load, not vocabulary; no condescension | accessibility |
| AN-60 | Positivity effect | Older adults favor positive information | Reed, Chan & Mikels 2014 meta | M | Partial | For older users, risk information first and explicit | accessibility |
| AN-61 | Circadian synchrony | Chronotype peaks | May et al. 1993 | M/W | No | Chronotype unknown; effects modest | n/a |

## H. Embodiment, grounding, neuro-hype

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| AN-62 | Action-sentence compatibility | Null in 18 labs | Glenberg & Kaschak 2002 → Morey 2022 | C | No | No "motor-priming verb" rules | n/a |
| AN-63 | Object-orientation match | Null in ~4,000 participants | Stanfield & Zwaan 2001 → Chen 2025 | C | No | Concreteness stands on behavioral evidence alone | n/a |
| AN-64 | Somatotopic action words | Causal role disputed | Hauk 2004; Mahon & Caramazza 2008 | M/C | No | Excluded | n/a |
| AN-65 | Facial feedback, power posing, behavior priming | Registered replications null | Wagenmakers 2016; Ranehill 2015; Doyen 2012 | C | No | Word choice doesn't "prime behavior" | n/a |
| AN-66 | Mirror-neuron accounts | Weakly supported | Hickok 2009; Hamilton 2013 | C | No | Excluded | n/a |
| AN-67 | SNARC / mental number line | Small left, large right | Dehaene 1993; Wood 2008 meta | S | Partial | Numeric options ascending top to bottom; otherwise say "sorted by X" | numbers |
| AN-68 | Space–time mapping | Past left, future right | Santiago et al. 2007 | M | Partial | Chronologies oldest → newest by default; label reverse order | explain |
| AN-69 | Neural efficiency | Experts show less activation | Neubauer & Fink 2009 | M | No | Covered by #8 | n/a |

## I. Reading & the brain / dyslexia

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| AN-70 | Word-frequency effect | — | Rayner 1998 | S | No | Duplicate of #61 | n/a |
| AN-71 | Jumbled-letter cost | Transposed letters slow reading 11–36% | Rayner et al. 2006 | S | Yes | No deliberate misspellings, leetspeak or stylized spellings | core |
| AN-72 | Speed reading / RSVP | Speed bought with comprehension | Rayner et al. 2016 | S | Partial | Never emit one-word-per-line "fast read" layouts | core |
| AN-73 | Phonological core of dyslexia | Deficit is phonological, not visual | Ramus 2003; Peterson & Pennington 2012; Rello 2013 | S/M | Yes | Short frequent words, acronyms expanded at first use; lexical simplification over layout tricks | accessibility |
| AN-74 | Italics / caps cost | Italics hurt dyslexic readers; caps slower | Rello & Baeza-Yates 2013; Tinker 1963 | M | Yes | Emphasis with bold only; no italic/underline emphasis, no caps runs over 2 words | accessibility |
| AN-75 | Font size, spacing, dyslexia fonts, overlays | No letterform/overlay effect | Rello 2016; Kuster 2018; Wery & Diliberto 2017; Griffiths 2016 | M/S | No | Rendering is the UI's job; never claim a font fixes dyslexia | n/a |

## J. ADHD

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| AN-76 | ADHD working-memory deficit | Large verbal and visuospatial deficits | Martinussen 2005; Kasper 2012 | S | Yes | One action per step; restate values instead of carrying them across steps | procedure |
| AN-77 | ADHD time perception | Timing deficits (g≈.69) | Marx 2021; Metcalfe 2024 | S | Yes | Duration estimates: total, plus any step over 10 min | procedure |
| AN-78 | Delay aversion | Steeper delay discounting | Sonuga-Barke 2002; Jackson & MacKillop 2016 | M | Yes | An action doable in under 2 minutes at the top | procedure |
| AN-79 | Reinforcement sensitivity | Immediate feedback and near subgoals sustain effort | Luman 2005 | M | Yes | "Step n of N"; tasks over 7 steps split into phases with done-criteria | procedure |
| AN-80 | Implementation intentions (ADHD) | — | Gawrilow & Gollwitzer 2008 | S | No | Duplicate of JD-49 | n/a |
| AN-81 | Elevated mind-wandering in ADHD | Spontaneous mind-wandering elevated | Bozhilova et al. 2018 | M | Yes | Long answers: a heading or step number every 3–5 paragraphs as a re-entry point | long-form |
| AN-82 | Hyperfocus | Poorly defined construct | Ashinoff & Abu-Akel 2021 | W | No | Excluded | n/a |

## K. Autism

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| AN-83 | Figurative-language gap tracks language ability | Gap vanishes when matched on language | Kalandadze 2018; Norbury 2005 | M | Yes | Instructions stated literally; pair any idiom with its literal meaning | accessibility |
| AN-84 | Intolerance of uncertainty in autism | Elevated, mediates anxiety | Boulter 2014; Jenkinson 2020 | S | Yes | Preview the structure, mark required vs optional, say what happens next | accessibility |
| AN-85 | Double empathy | 2025 registered report: info transfer equal, rapport lower in mixed pairs | Milton 2012; Crompton 2020, 2025 | M/C | Partial | Match the user's directness; no rapport padding | accessibility |
| AN-86 | Weak central coherence | Meta: no local bias, slower global processing | Van der Hallen 2015 | C | Partial | Gist before details (applies to everyone) | explain |
| AN-87 | Scalar implicature intact | Autistic adults compute "some → not all" | Pijnacker 2009; Chevallier 2010 | M | Partial | Make modality explicit ("must" / "optional"); avoid "you might want to" when you mean "do" | core |

## L. Aphasia, Easy Read, COGA

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| AN-88 | Aphasia-friendly text | Simplified syntax/vocabulary aid comprehension; clip art distracts | Rose 2003; Brennan 2005; Rose 2011 | M/W | Yes | Sentences ≤12 words, one idea each, bold the key word, no decorative images or emoji | accessibility |
| AN-89 | Easy Read | — | Buell 2020 | W | No | Duplicate of HC-95 | n/a |
| AN-90 | W3C COGA patterns | Literal language, no double negatives, summaries, no reliance on memory | W3C "Making Content Usable" 2021 | W | Yes | One instruction per line; no double negatives; >400 words → summary first; restate earlier-turn info | accessibility |
| AN-91 | Curb-cut effect | Accessibility changes help everyone | Galliussi 2020 | M | Yes | Apply accessibility defaults universally; never require disclosure first | core |

## M. Screen readers & markdown

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| AN-92 | Heading navigation | — | WebAIM 2024 | M | No | Duplicate of HC-111 | n/a |
| AN-93 | Emoji verbosity | — | Unicode CLDR | W | No | Duplicate of HC-110 | n/a |
| AN-94 | ASCII / box diagrams | Read aloud as punctuation noise | WCAG 2.2 SC 1.1.1, 1.3.1 | M | Yes | Follow every ASCII diagram with a prose or list equivalent | accessibility |
| AN-95 | Tables & screen readers | Header rows give context; wide tables laborious | WCAG 1.3.1 | M | Yes | Always a header row; ≤5 columns; no meaning in blank cells | accessibility |
| AN-96 | Link text | — | WCAG 2.4.4 | M | No | Duplicate of HC-61 | n/a |

## New neuromyths (never cite; correct if the user does)

1. "23 minutes to refocus after an interruption" — Mark et al. 2005 measured ~25 min to resume a work sphere with other tasks in between (SD ≈ 55 min); not refocusing time.
2. "Email drops IQ 10 points, more than marijuana" — unpublished HP study, n=8, disowned (Wilson 2005).
3. "Digital natives can multitask" — Kirschner & De Bruyckere 2017.
4. "Willpower is glucose-fueled" — Hagger 2016; Vohs 2021; Vadillo et al. 2016.
5. "Hungry judges / decision fatigue" — Weinshall-Margel & Shapard 2011; Glöckner 2016.
6. "Yerkes–Dodson law" as a general rule — Teigen 1994; Corbett 2015.
7. "Mirror neurons explain empathy; broken mirrors cause autism" — Hickok 2009; Hamilton 2013.
8. "Autistic people lack empathy / can't handle non-literal language" — Fletcher-Watson & Bird 2020; Kalandadze 2018; Crompton 2025.
9. "Dyslexia is visual; special fonts or overlays fix it" — AAP/AAO 2011; Kuster 2018; Griffiths 2016.
10. "We read words by their shape" — Larson 2004; Pelli et al. 2003.
11. "Cambridge study: letter order doesn't matter" — no such study; Rayner et al. 2006 found 11–36% slowdown.
12. "Speed reading keeps comprehension at 1000+ wpm" — Rayner et al. 2016.
13. "Brain training expands working memory / IQ" — Melby-Lervåg et al. 2016; Simons et al. 2016.
14. "Amygdala hijack / amygdala = fear center" — LeDoux & Pine 2016.
15. "Sugar causes hyperactivity" — Wolraich et al. 1995 meta.
16. "Oxytocin is the trust hormone" — Nave et al. 2015; Declerck et al. 2020.
17. "Brain images make claims persuasive" — Farah & Hook 2013 (verbal neuro-allure is the real effect).
18. "Power posing changes hormones" — Ranehill 2015.
19. "Hyperfocus is an ADHD superpower" — construct poorly defined (Ashinoff & Abu-Akel 2021).
