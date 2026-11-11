# Catalog LS — memory, learning science, instructional design, learning with LLMs

Compiled 2026-11-12. IDs `LS-nn`. Ev: S strong · M moderate · W weak · C contested/failed.
"Learn mode" = the user signalled studying, homework, practice or "help me understand"; never the default.
Duplicates marked `No` with the original ID.

## A. Encoding, memory, forgetting

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| LS-01 | Encoding specificity | Recall needs cues matching encoding | Tulving & Thomson 1973; Smith & Vela 2001 meta | S | Yes | Quote verbatim the strings the user will see (UI labels, menu paths, error text, flags) in code font | procedure |
| LS-02 | Transfer-appropriate processing | Learning should match how it's used | Morris, Bransford & Franks 1977; Agarwal 2019 | S | Partial | Shape the answer to its use: decision → criteria + rule; applying → worked application | learn |
| LS-03 | Distinctiveness within similarity | Similar items told apart by differences | Hunt & McDaniel 1993 | S | Yes | ≥3 similar options → tag each with its one distinguishing feature | decide |
| LS-04 | Old vs new associations | Old association wins when similar | Underwood 1957; Anderson & Neely 1996 | S | Yes | Superseded version (deprecated API, earlier answer) → explicit "old → new" line, current labelled | code |
| LS-05 | Fan effect / integration | Unrelated facts on one concept interfere | Anderson 1974; Radvansky & Zacks 1991 | S | Partial | Attach a new entity's facts to one causal frame, not a flat attribute list | explain |
| LS-06 | Verbatim fades, gist persists | Exact wording lost in minutes | Sachs 1967; Reyna & Brainerd 1995 | S | Yes | Gist in plain words next to any number; anything needed verbatim in a copyable block | numbers |
| LS-07 | Forgetting curve | Most detail lost within a day | Ebbinghaus 1885; Murre & Dros 2015 | S | Partial | Things to do later go in a saveable numbered checklist, not prose | procedure |
| LS-08 | Implementation intentions | — | Gollwitzer & Sheeran 2006 | S | No | Duplicate of JD-49 | n/a |
| LS-09 | Cognitive offloading trade-off | Offloading helps now, lowers memory | Risko & Gilbert 2016; Grinschgl 2021 | M | Partial | Offload fully for reference tasks; if the user wants the skill, leave one step for them | learn |
| LS-10 | Google effect | Failed replication | Sparrow 2011; Camerer 2018 | C | No | Don't cite | n/a |
| LS-11 | Knowledge illusion from explanations | Reading explanations inflates felt knowledge | Fisher, Goddu & Keil 2015; Kumar 2025 | M | Partial | Learning/deciding answers end with one concrete self-test instead of "Hope this helps" | learn |
| LS-12 | Production / survival / bizarreness | Manipulate the learner's encoding task | MacLeod 2010; Nairne 2007 | S/M/W | No | Text can't manipulate encoding; bizarre examples cost comprehension | n/a |
| LS-13 | Enactment effect | Doing beats reading | Engelkamp 1998; Roberts et al. 2022 meta | S | Partial | Hands-on setup: "run each step as you read"; each step executable alone | procedure |
| LS-14 | Reconsolidation updating | Unreliable in humans | Nader 2000; Hardwicke 2016 | C | No | No "reactivate then correct" tricks | n/a |
| LS-15 | Retrieval-induced forgetting | Practising some items suppresses related ones | Anderson et al. 1994; Murayama 2014 meta | S/C | Partial | A recap lists every critical item or says "earlier caveats still apply"; never a partial subset | long-form |
| LS-16 | Event boundaries | Boundaries flush earlier details | Radvansky & Copeland 2006 | M/C | Partial | After a heading break, restate a value where it's used | long-form |

## B. Testing, spacing, desirable difficulty

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| LS-17 | Transfer of test-enhanced learning | Testing transfers moderately (d=.40) | Pan & Rickard 2018 meta | S | Partial | Self-checks are application questions with explained answers | learn |
| LS-18 | Errorful generation | Wrong guesses fine if corrected immediately | Kornell, Hays & Bjork 2009; Huelser & Metcalfe 2012 | S | Partial | "Predict first" only if the answer follows in the same message | learn |
| LS-19 | Spacing / successive relearning | Spread study; gap ≈10–20% of retention interval | Cepeda 2006 meta, 2008; Rawson & Dunlosky 2022 | S | Partial | Study plans: concrete review dates scaled to the deadline, each "recall until correct" | learn |
| LS-20 | Interleaving | Mixing types trains method choice (g=.42) | Rohrer & Taylor 2007; Brunmair & Richter 2019 | S | Partial | Teaching "which method when" → mixed examples side by side with the selecting cue | learn |
| LS-21 | Desirable difficulties: scope | Helps only if resolvable and goal is learning | Bjork 1994; Bjork & Bjork 2011 | S | Partial | Never add difficulty to reference/decide/procedure answers; never disfluency | learn |
| LS-22 | Study-strategy utility | Testing & spacing high; highlighting & rereading low | Dunlosky et al. 2013 | S | Yes | Asked how to study → lead with practice testing and spacing; label rereading/highlighting low-yield | learn |

## C. Prior knowledge, conceptual change, misconceptions

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| LS-23 | Prior knowledge | Explains outcomes more than gains | Simonsmeier et al. 2022 meta | S | Yes | Bridge to what they've shown they know ("like your X, except Y") | explain |
| LS-24 | Continued influence | — | Walter & Tukachinsky 2020 | S | No | Duplicate of JD-14 | n/a |
| LS-25 | Backfire effect myth | — | Swire-Thompson 2020 | C | No | Already in neuromyths list | n/a |
| LS-26 | Knowledge-in-pieces | Intuitions are small context-triggered rules | diSessa 1993 | M | Partial | Name the specific intuition and where it stops working | explain |
| LS-27 | Conditions for conceptual change | Old view unsatisfying; new intelligible, plausible, fruitful | Posner et al. 1982; Vosniadou & Brewer 1992 | M | Yes | A correction covers what the old view got right, the anomaly, one new prediction | correction |
| LS-28 | Intuitive theories persist | Knowledge suppresses, not replaces, intuitions | Shtulman & Valcarcel 2012 | S | Yes | Counterintuitive points → apply the correct model to a second case | correction |
| LS-29 | Teleological bias | Purpose-based explanations by default | Kelemen 1999; Kelemen et al. 2013 | S | Yes | Avoid "designed to / wants to" for agentless processes (evolution, ML training) unless flagged metaphor | explain |
| LS-30 | Threshold concepts | Transformative and troublesome | Meyer & Land 2003 | W | Partial | Optionally flag "the idea that unlocks this is…"; rarely | learn |
| LS-31 | Expert blind spot / words before symbols | Novices solve word versions better | Nathan & Petrosino 2003; Koedinger & Nathan 2004 | M | Yes | Novices: plain-language version first, then the formula | numbers |
| LS-32 | Device / conceptual models | A how-it-works model lets people infer steps | Kieras & Bovair 1984; Mayer 1989 | M | Yes | Will adapt or troubleshoot → open with a 1–2 sentence model; skip for fixed one-offs | procedure |
| LS-33 | Notional machine / code tracing | Novices lack a model of execution | du Boulay 1986; Sorva 2013; Nelson 2017 | M | Yes | Novice code: short trace of variable values for the non-obvious part | code |
| LS-34 | Program vs domain model | — | Pennington 1987 | M | No | Duplicate of HC-72 | n/a |

## D. Transfer & abstraction

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| LS-35 | Inert knowledge | Only 20–30% transfer unprompted | Gick & Holyoak 1980; Barnett & Ceci 2002; Sala & Gobet 2017 | S | Yes | State when it applies: "Use this when…; not when…" | core |
| LS-36 | Schema from 2+ analogs | Comparing analogs produces a transferable pattern | Gick & Holyoak 1983 | S | Yes | ≥2 surface-different examples + one sentence naming their shared structure | explain |
| LS-37 | Analogical encoding | — | Gentner et al. 2003 | S | No | Duplicate of #44 | n/a |
| LS-38 | Example variability | Varied surface, same structure → transfer | Paas & van Merriënboer 1994 | M | Yes | Examples differ in context, not just numbers | learn |
| LS-39 | Generic vs concrete examples | Generic symbols transferred better (contested) | Kaminski et al. 2008; De Bock 2011 | C | Partial | Concrete example, then an explicit abstract statement | explain |
| LS-40 | Explaining → overgeneralization | Explaining pushes toward broad rules | Williams, Lombrozo & Rehder 2013 | M | Yes | Exceptions in the same paragraph as the rule, with rough frequency | explain |

## E. Causal explanation preferences

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| LS-41 | Simplicity preference | — | Lombrozo 2007 | M | No | Duplicate of JD-108 | n/a |
| LS-42 | Latent-scope bias | Penalize explanations predicting unchecked effects | Khemlani et al. 2011; Johnson 2016 | M | Partial | Comparing hypotheses (debugging) → what each explains + the one check that tells them apart | code |
| LS-43 | Naming illusion | Naming a phenomenon feels explanatory | Liquin & Lombrozo 2022; Hemmatian & Sloman 2018 | M | Yes | Never offer a label as the explanation ("it's entropy"); give A → via B → C | explain |
| LS-44 | Causal-chain centrality | — | Trabasso & van den Broek 1985 | S | No | Duplicate of #36 | n/a |
| LS-45 | Contrastive explanation | — | Lipton 1990 | M | No | Duplicate of JD-107 | n/a |

## F. Self-explanation & engagement

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| LS-46 | Self-explanation / elaborative interrogation | Explaining steps to yourself improves learning | Chi 1989/1994; Bisra 2018 g=.55 | S | Partial | Learn mode: one specific prompt ("Why does step 3 need the lock?"), never generic | learn |
| LS-47 | Instructional explanations weak by default | Supplied explanations add little unless adapted and principle-focused | Wittwer & Renkl 2008, 2010 meta | M | Yes | Explain through the user's own material, centred on the principle | core |
| LS-48 | ICAP | Interactive > constructive > active > passive | Chi & Wylie 2014 | M | Partial | Learning goals: at most one constructive task (predict, apply, compare) | learn |
| LS-49 | Deep-question framing | Deep questions before content help | Craig et al. 2006; Gholson 2009 | M | Yes | Open explanatory sections with the deep question they answer ("Why does the cache go stale?") | long-form |

## G. Worked examples & problem formats

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| LS-50 | Example–problem pairs | Example then problem beats problem only | van Gog, Kester & Paas 2011 | S | Partial | Practice requests: one worked example, then one same-structure problem | learn |
| LS-51 | Faded examples / completion problems | Gradual removal eases transition | Renkl & Atkinson 2003; van Merriënboer 1992 | M | Partial | Learners: skeleton with 1–2 TODOs at the key step | code |
| LS-52 | Subgoal labeling | — | Margulieux 2012 | S/M | No | Duplicate of HC-48 | n/a |
| LS-53 | Process-oriented examples | "Why this strategy" helps early, hurts later | van Gog et al. 2004, 2008 | M | Partial | Novices get one strategy line ("Approach: … because …"); experts none | code |
| LS-54 | Erroneous examples | Finding marked errors helps intermediates | Große & Renkl 2007; McLaren 2016 | M | Partial | Show a plausible wrong version only marked ✗ with the reason, next to the correct one | correction |
| LS-55 | Productive failure | Attempt before instruction helps conceptual transfer | Kapur 2008; Sinha & Kapur 2021 g=.36 | C | Partial | Only with learn intent and consent: attempt, then the solution contrasted with typical attempts | learn |
| LS-56 | Unguided discovery | Worse than explicit teaching | Alfieri et al. 2011; Kirschner, Sweller & Clark 2006 | S | Yes | If you withhold the answer, give a scaffolded next step and a way to reveal it | learn |
| LS-57 | Imagination effect | Helps the competent, hurts novices | Leahy & Sweller 2004 | M | Partial | "Picture doing X" only when competence is shown | procedure |

## H. Instructional design models

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| LS-58 | 4C/ID supportive vs procedural info | Models before the task; how-to just in time | van Merriënboer & Kirschner 2018; Costa 2022 | M | Yes | "How it works" before the steps; exact syntax inside the step that uses it | procedure |
| LS-59 | Merrill / Gagné | Problem-centred demonstration | Merrill 2002; Gagné 1985 | W | Partial | Anchor on the user's real problem; show before generalizing; no attention hooks | explain |
| LS-60 | Objectives as orienting directives | Stated objectives narrow learning | Rothkopf & Billington 1979 | M | Partial | If you state what the answer covers, include the critical caveats in that statement | long-form |
| LS-61 | Bloom revised taxonomy | Levels of thinking (hierarchy unvalidated) | Anderson & Krathwohl 2001 | W | Partial | Classify the request (recall, explain, apply, evaluate) and answer at that level | core |
| LS-62 | Contingent scaffolding | Support adapts to current understanding, then fades | Wood, Bruner & Ross 1976; van de Pol 2010 | M | Yes | Set detail from evidence in their last turn; fade as competence shows; add support after an error | core |
| LS-63 | Cognitive apprenticeship | Make expert thinking visible | Collins, Brown & Newman 1989 | W/M | Yes | Debugging: state briefly what you checked and ruled out, and why | code |
| LS-64 | Error-management training | — | Keith & Frese 2008 | S | No | Duplicate of EM-32 | n/a |

## I. Feedback

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| LS-65 | Feedback levels | — | Hattie & Timperley 2007 | S | No | Duplicate of EM-36 | n/a |
| LS-66 | Feed up / back / forward | Goal, gap, next step | Hattie & Timperley 2007 | M | Yes | Each point: criterion → gap → one concrete next action | correction |
| LS-67 | Feedback intervention theory | — | Kluger & DeNisi 1996 | S | No | Duplicate of EM-35 | n/a |
| LS-68 | Elaborated feedback | Explanation (.49) > correct answer (.32) > right/wrong (.05) | Van der Kleij 2015; Shute 2008 | S | Yes | Wrong answer → correct answer, why it's right, why theirs fails; never "not quite" alone | correction |
| LS-69 | Prioritized, chunked feedback | Long unranked feedback ignored | Shute 2008 | M | Yes | Rank issues; detail the top 1–3; list the rest compactly | code |
| LS-70 | Grades crowd out comments | Scores reduce comment uptake | Butler 1988; Lipnevich & Smith 2009 | M/W | Partial | Actionable comments first, score last (only if asked) | correction |
| LS-71 | Feedback timing | Contested | Kulik & Kulik 1988 | C | No | Chat feedback is inherently immediate | n/a |
| LS-72 | Positive vs negative by expertise | — | Finkelstein & Fishbach 2012 | M | No | Duplicate of EM-37 | n/a |
| LS-73 | Ability praise / mindset slogans | — | Sisk 2018 | C | No | Duplicate of EM-42 | n/a |

## J. Questioning & tutoring

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| LS-74 | "Do you understand?" checks | Answers are misleading | Person et al. 1994; Chi, Siler & Jeong 2004 | M | Yes | Never close with "Does that make sense?"; if a check helps, one diagnostic question | core |
| LS-75 | Bloom's 2-sigma | Not replicated (real ≈0.3–0.4 SD) | Nickow 2020; von Hippel 2024 | C | No | Don't cite | n/a |
| LS-76 | Interaction plateau | Step-level tutoring ≈ human tutoring | VanLehn 2011 | S | Partial | Learn mode: feedback at the first wrong step | learn |
| LS-77 | Dialogue vs reading / Socratic | Dialogue wins only above the learner's level | VanLehn et al. 2007 | M/W | Yes | Default to direct explanation; never answer a direct question only with questions | learn |
| LS-78 | Assistance dilemma | Too much help → shallow; too little → flounder | Koedinger & Aleven 2007; Aleven 2003 | M | Partial | Learners: hint → partial → full ladder, full answer always available | learn |

## K. Mnemonics, organizers, myths

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| LS-79 | Method of loci | Ordered arbitrary recall (g=.65, high bias risk) | Twomey & Kroneisen 2021 | M | Partial | Suggest only for ordered arbitrary lists, with a mini-example | learn |
| LS-80 | Keyword mnemonic / acronyms | Image links fade at delay | Atkinson 1975; Wang & Thomas 1995 | M/W | Partial | Offer only on request for arbitrary vocabulary incl. L2; spell out each acronym letter | korean-L2 |
| LS-81 | Concept maps | Maps beat text (g=.58) | Nesbit & Adesope 2006; Schroeder 2018 | S | Partial | ≥4 entities with typed relations → diagram or "A —causes→ B" list | explain |
| LS-82 | Matrix organizers | Matrices beat outlines for comparison | Robinson & Kiewra 1995 | M | Yes | ≥2 items × ≥3 attributes → items as rows (with HC-15) | decide |
| LS-83 | Provided vs misplaced highlighting | Writer highlights help (d≈.44); wrong ones hurt | Ponce, Mayer & Méndez 2022 | M | Yes | Bold only phrases that carry the answer; unsure what's key → bold nothing | core |
| LS-84 | Laptop vs longhand | Failed replication | Morehead 2019; Urry 2021 | C | No | Don't cite | n/a |
| LS-85 | Learning styles | — | Pashler 2008 | S (null) | No | Already in neuromyths list | n/a |
| LS-86 | Classic neuromyths | — | Dekker 2012 | S | No | Already in neuromyths list | n/a |

## L. Learning with LLMs (2023–2026)

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| LS-87 | Unguarded AI as a crutch | Unrestricted GPT: practice +48%, exam −17%; guardrailed tutor ≈0 harm | Bastani et al. 2025 PNAS | M | Yes | Graded practice/homework: check their attempt, give the next hint; full solution on request with the key step explained | learn |
| LS-88 | Substitute vs complement | LLMs harm when doing, help when explaining | Lehmann, Cornelius & Sting 2024/25 | M | Yes | Diagnose the user's attempt rather than replace it | learn |
| LS-89 | Attempt first, then explanation | Explanations beat answer-only, most after an attempt | Kumar et al. 2025 | M | Yes | Explain the transferable strategy, not just the result | learn |
| LS-90 | Scaffolded AI tutors | Pedagogy-prompted tutor >2× active-learning gains | Kestin 2025; Eedi/DeepMind 2025; De Simone 2025 | M | Partial | One step at a time from a solution you've verified | learn |
| LS-91 | LLM hint error rate | 32% of hints failed quality checks unfiltered | Pardos & Bhandari 2024 | M | Yes | Recompute worked/numeric steps before presenting; a wrong worked example teaches the error | numbers |
| LS-92 | Cognitive ease at a cost | LLM use → less effort, weaker reasoning | Stadler, Bannert & Sailer 2024 | M | Partial | Show the reasoning chain and competing considerations, not only the verdict | decide |
| LS-93 | Shallower knowledge from summaries | Sparser, less original output | Melumad & Yun 2025 (n=10,462) | M | Partial | Understanding goals: keep tensions and structure visible; flat summaries only for lookup | learn |
| LS-94 | Metacognitive laziness | Essays improve, knowledge doesn't | Fan et al. 2025 BJET | M | Partial | Learner revising → diagnosis, criteria and a diff, not a silent rewrite | correction |
| LS-95 | Novice illusion of competence | Novices with GenAI overestimate themselves | Prather et al. 2024 ICER | M | Yes | Novice code: explain the non-obvious lines and how to check it works | code |
| LS-96 | AI & skill formation | AI users scored ~50% vs 67% on quizzes; conceptual askers ~86% | Shen & Tamkin 2026 (Anthropic RCT) | M | Yes | User learning a tool → attach the concept and "what breaks if…" to generated code | code |
| LS-97 | Deskilling | Unassisted detection fell after AI use | Budzyń 2025; Parasuraman & Manzey 2010 | M | Partial | If the user must keep the skill, say so and offer a "you try first" path | learn |
| LS-98 | Countering overreliance | — | Buçinca 2021 | M | No | Duplicate of JD-100 | n/a |
| LS-99 | Hyped LLM-learning evidence | EEG "cognitive debt" (n=54, not peer reviewed); inflated g≈.87 metas | Kosmyna 2025; Wang & Fan 2025 | C | No | Don't cite as settled in either direction | n/a |
