# Explaining a concept or mechanism

Use this when the answer's main job is "help me understand X".

**Order:** frame → parts → causal chain → one concrete example → the general rule.

## Frame

1. **Name the topic first,** gist before details. (#32, AN-86)
2. **Explain only the gap the question reveals,** and offer depth. Find the implied alternative and explain the difference ("X rather than the usual Y, because…"). (JD-110, JD-107)
3. **Bridge from what they have shown they know:** "like your X, except Y". Build examples from their own domain or data. (LS-23, EM-23)
4. **Check each term against their vocabulary.** A term whose technical sense isn't the everyday one (branch, kernel, token, "significant") needs the domain set up first, or a gloss. (EM-108, PL-13)
5. **Lay readers:** everyday words, sentences of about 20 words or fewer on average, and nothing accuracy-critical dropped. Unprompted LLM answers sit at grade 10–12+. (PL-64)
6. **New domain → headings.** Familiar question → no headings. (HC-56)

## Mechanism

- **Parts before the system.** If 3 or more parts interact, define each in one line, then explain how they interact. (#4, #16)
- **Write a causal chain in event order:** actor → action → effect, with *because / so*. Use prose, not bullets, because bullets hide the causal links. (#35, #46, #48, #86, HC-16)
- **Never give a label as the explanation** ("it's entropy"). Give A → via B → C. (LS-43)
- **Tie a new entity's facts into one causal frame,** not a flat attribute list. (LS-05)
- **State critical relations in active order,** and flag counterintuitive directions: "A depends on B, not the reverse". When plain words still leave a counterintuitive concept, state the counterintuitive point explicitly. (PL-23, HC-89)
- **API misuse → name the underlying model in one line.** (HC-69)
- **Introduce implied entities before "the …":** "This creates a lock file. The lock file…". After "because" or "so", name the referent when two of the same type came before. (PL-28, PL-42)
- **Mark adjacent sentences that aren't cause and effect** ("Separately,"), because readers assume they are. (PL-30)
- **No purpose talk for processes without an agent** (evolution, ML training) unless it is flagged as metaphor. (LS-29)
- **Name the specific intuition and where it stops working:** "closer = hotter works for stoves, not seasons". (LS-26)
- **Chronologies run oldest → newest** unless labelled otherwise. (AN-68)
- **Attach a "because" to each key fact.** (#67)

## Causes and evidence

- **Give the top 1–3 causes with rough weights.** Never drop a large-share cause to look simpler ("also contributes: …"). Unpack every side to the same granularity and add an "other" bucket. (JD-108, JD-04)
- **"If X were different, the answer would be Y."** (JD-109)
- **Raise regression to the mean** when someone credits recovery after an extreme low to an intervention. In post-mortems, separate "knowable then" from "known now". (JD-08, JD-15)
- **When studies conflict,** say why (population, dose, design) and give the current bottom line. (JD-57)
- **State real consensus and how strong it is.** When presenting two sides, give their relative evidential weight. (JD-66, JD-67)
- **Show verifiable steps and flag the weakest one.** Point to the exact line, number or source the reader can check in seconds. Long reasoning is not a persuasion device. (JD-97, JD-99)

## Examples and abstraction

- **Concrete first, then the rule it shows, then notation if needed.** End by stating the rule explicitly. (#45, #41, LS-39)
- **Give 2 or more surface-different examples,** plus one sentence naming their shared structure. (LS-36)
- **Put exceptions in the same paragraph as the rule,** with a rough frequency. Explaining invites overgeneralization. (LS-40)
- **Use imageable wording:** "a shelf next to the desk" beats "a proximal storage layer". Learning-style tailoring is a myth. (#42)
- **Analogy:** map the structure, then say where it breaks. **Distinction:** a minimal pair, then name the difference. (#43, #44)
- **Spatial or flow content → a small table or diagram.** 4 or more entities with typed relations → "A —causes→ B" lines. (#17, LS-81)
- **One genuine puzzle is allowed** if you resolve it right away. (#73)
- **Anchor on the user's real problem and show it before generalizing.** No attention hooks. (LS-59)
- **High-stakes terms:** plain text first, then offer to check understanding. (HC-93)

## Repair

- **On "what?", rephrase with new words.** On a targeted question, fix only that part. (EM-106)

Fit the reader: experts skip the parts and analogy steps; novices get all of it. (#8)
For a misconception in the question, see [correction.md](correction.md).

## Structure and diagrams (round 2)

- **Lookups get the inverted pyramid. "Help me understand" gets the answer line, then a cause → effect story.** Narrative structure helps novices most. Experts get facts ranked by importance, and nobody gets a scene-setting opener. (NW-01, NW-02, NW-04)
- **"What happened with X?" → add one line on why it matters.** (NW-08)
- **Keep each entity's attributes together,** in one table row or one block. (DG-01)
- **Add a diagram only when its shape answers the question:** a flow for "what happens when", a tree for "what contains what". An ill-fitting diagram is worse than text. (DG-04)
- **Diagrams stay simple:** about 7 nodes or fewer, only causally relevant parts. Give each arrow style one meaning and a label ("A —writes→ B"). (DG-05, DG-06)
- **Use the same labels in the text and the diagram or table,** and state the mapping once. (DG-09)
