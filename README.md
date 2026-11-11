# 🧠 brainres

**Claude answers your brain can actually read.**

English · [한국어](README.ko.md)

`caveman` makes Claude shorter. `humanizer` makes it sound human.
**brainres makes it understandable**: 90 findings from cognitive science, compressed into 10 rules that shape every answer.

[![Claude Code plugin](https://img.shields.io/badge/Claude_Code-plugin-d97757)](#install) [![evidence](https://img.shields.io/badge/rules-evidence--linked-2ea44f)](research/cognitive-principles.md) [![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE) [![built by](https://img.shields.io/badge/built_by-a_20--min_Claude_loop-8a63d2)](LOOP_LOG.md)

---

## Same question, two answers

> *"My React component keeps re-rendering forever. Why?"*

<table>
<tr><th>Default Claude-style answer · Brain Score <b>50</b> · 272 words</th><th>With brainres · Brain Score <b>100</b> · 134 words</th></tr>
<tr valign="top"><td>

Great question! Infinite re-renders are a common issue that many React developers encounter… Let me break down the most common causes.

**## Understanding the Problem**
React re-renders a component whenever its state or props change. When a component triggers a state update during rendering, or when an effect updates a value that it also depends on, it can potentially create…

**## Common Causes**
1. **Calling setState in render** – …
2. **useEffect with incorrect deps** – …
3. **Objects in dependency arrays** – …
4. … *(7 causes, all bold)*

**## Solutions**
It is important to note that the right solution depends on the specific cause…

I hope this helps! Let me know if you have any other questions.

</td><td>

Your `useEffect` is almost certainly updating a value it also depends on, so every render schedules the next one.

The loop:
1. Render → effect runs → `setItems(...)`
2. `items` changed → React re-renders
3. `items` is in the deps → effect runs again → back to 1

Fix it by depending on the input, not the output:
```js
useEffect(() => {
  fetchItems(query).then(setItems);
}, [query]); // was [items]
```

To confirm, add `console.count("render")`. A count that climbs while you touch nothing means the loop is real.

If neither pattern matches, paste the component and I'll point to the exact line.

</td></tr>
</table>

The answer is in sentence 1. The mechanism comes as a causal chain, with one worked fix and a way to verify it, and the answer ends on a next action. Full files: [`examples/`](examples/). Score your own text with [`brainlint`](#brainlint).

## Install

```bash
claude plugin install brainres --marketplace wonjangcloud9/brainres
```

Or inside Claude Code: `/plugin marketplace add wonjangcloud9/brainres` → `/plugin install brainres@brainres`.

<details><summary>Manual install / other agents</summary>

```bash
git clone https://github.com/wonjangcloud9/brainres
cp -R brainres/skills/brainres ~/.claude/skills/brainres
```

A manual install gives you the skill only. Invoke it with `/brainres`, or paste [`hooks/core-card.md`](hooks/core-card.md) into your `CLAUDE.md` or any LLM's system prompt to get the always-on behavior.
</details>

Once installed, it's always on. A session-start hook adds a ~350-token rule card once per session. A ~60-token reminder rides along with each message, because instructions fade over long sessions. To turn it off, run `export BRAINRES=off` or `touch ~/.claude/brainres.off`.

## The 10 rules

| # | Rule | The science |
|---|---|---|
| 1 | **Answer in sentence 1.** Then why, then detail. | BLUF, extraneous load (Sweller) |
| 2 | **End on the next action**, not "hope this helps". | Serial position, peak-end rule |
| 3 | **Length follows content.** ≤100 words for a fact, ≤300 for an explanation, TL;DR past 500. | Reading rate (Brysbaert 2019); longer LLM answers inflate trust (Steyvers 2025) |
| 4 | **Chunk to 4.** Sub-group anything bigger. | Working memory ≈ 4 chunks (Cowan 2001) |
| 5 | **Shape matches content.** Reasoning in prose, steps in lists, comparisons in tables. | Cognitive fit (Vessey); causal connectives (Trabasso) |
| 6 | **Signal sparingly.** Headings that carry content, ≤1 bold per paragraph. | Signaling (meta g≈.5); von Restorff; signal dilution |
| 7 | **Concrete, with your stuff.** Your files, your values, one worked example. | Concreteness, self-reference, worked-example effect (g=.48) |
| 8 | **Your words, one term per thing.** Define new terms before using them. | Lexical entrainment; curse of knowledge |
| 9 | **Calibrate instead of hedging.** "I'm ~70% sure", plus a way to check. | Numeric uncertainty keeps trust (van der Bles 2020); first-person hedges cut overreliance (Kim 2024) |
| 10 | **Plain syntax.** One idea per sentence, active voice, no nested clauses. | Center-embedding cost (Gibson 2022); negation cost |

It also **adapts to you**. Experts get terse answers, and novices get definitions first plus one analogy. This follows the [expertise reversal effect](skills/brainres/references/evidence.md), which none of the terse or humanizer skills model.

## Modes

Ask for a mode by name, e.g. *"brainres scan"* or *"learn mode"*.

| Mode | For |
|---|---|
| default | Every answer. Always on. |
| `scan` | Answer plus ≤4 bullets. For skimming or for experts. |
| `learn` | Adds a question before the explanation, a worked example, and 1–2 check questions after (retrieval practice). |
| `rewrite` | Restructures any text you paste, then checks that no claim was lost. |
| `score` | Runs brainlint on a file. |
| `off` | Pauses it. |

## brainlint

A dependency-free scorer for any answer, doc or README, in English and Korean (번역투 detection included).

```bash
python3 skills/brainres/scripts/brainlint.py answer.md
```
```
Brain Score: 50/100 (D)  ·  272 words · 18 sentences · lang=en
  -15  preamble         opens with filler: 'Great question! ...'     [Primacy effect + BLUF]
  - 8  outro            ends with generic sign-off                     [Recency effect]
  - 6  bold_lead_ins    7 list items start with bold                   [Signal dilution]
  - 5  list_overload    list of 7 items; group into chunks of <=4      [Chunking (Cowan 4±1)]
```

Each check maps to a named finding. It's a heuristic, not a comprehension test. See *Honest limits* below.

## How it differs

| | Optimizes for | Grounded in |
|---|---|---|
| terse / caveman-style skills | fewer output tokens | token counts |
| humanizer / anti-slop skills | not sounding like AI | Wikipedia's *Signs of AI writing* |
| **brainres** | **understanding per second of reading** | **90 cognitive-science findings, each rated for evidence strength** |

brainres keeps what those projects got right: no preamble, protect code and numbers, full sentences for safety warnings. It adds what they don't cover: chunking, define-before-use, reader expertise, calibrated uncertainty, and causal explanations. The survey is in [`research/trending-skills.md`](research/trending-skills.md).

## Science, not vibes

- [`research/cognitive-principles.md`](research/cognitive-principles.md) catalogs 90 concepts across working memory, Mayer's principles, eye-tracking, comprehension, fluency, memory and trust. Each has a source, an evidence grade (strong / moderate / contested) and a concrete writing rule.
- **Neuromyths we refuse:** learning styles, left/right brain, the "8-second attention span", Dale's cone, Bionic Reading, and "dopamine-hit" formatting.
- **Honest limits:** nobody, us included yet, has run controlled studies on formatting rules for LLM chat answers. The thresholds are engineering defaults to be tuned by evaluation. A human comprehension benchmark is on the [roadmap](BACKLOG.md).

## Built overnight by a loop

The repo improves itself. Every 20 minutes a Claude Code loop takes the top item from the [RICE-scored backlog](BACKLOG.md), implements it, validates it, and pushes. When the backlog runs dry, it researches again. Every iteration is logged in [`LOOP_LOG.md`](LOOP_LOG.md). The protocol is in [`LOOP.md`](LOOP.md).

## Contributing

Issues and PRs are welcome, especially before/after pairs where brainres made an answer *worse*. A rule only gets in if it cites a finding in `research/`.

MIT © wonjangcloud9
