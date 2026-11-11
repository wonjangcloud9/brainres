# 🧠 brainres

**Claude answers your brain can actually read.**

English · [한국어](README.ko.md)

`caveman` makes Claude shorter. `humanizer` makes it sound human.
**brainres makes it understandable.** It reviews **725 findings** from cognitive science, psycholinguistics, decision science and human–AI trust research. Each finding is either applied as a writing rule or excluded with a stated reason.

[![Claude Code plugin](https://img.shields.io/badge/Claude_Code-plugin-d97757)](#install) [![coverage](https://img.shields.io/badge/findings_applied-596%2F596-2ea44f)](research/coverage.md) [![reviewed](https://img.shields.io/badge/findings_reviewed-725-blue)](research/) [![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE) [![built by](https://img.shields.io/badge/built_by-a_20--min_Claude_loop-8a63d2)](LOOP_LOG.md) [![Brain Score](https://img.shields.io/badge/Brain_Score-100%2F100_A-2ea44f)](https://github.com/wonjangcloud9/brainres)

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

**Use it anywhere** (built by [`scripts/build_dist.py`](scripts/build_dist.py) from the same sources):

| Where | File | How |
|---|---|---|
| claude.ai / Claude desktop | [`dist/brainres-skill.zip`](dist/brainres-skill.zip) | Customize → Skills → upload |
| ChatGPT, Gemini, any LLM | [`dist/system-prompt.md`](dist/system-prompt.md) | Paste into custom instructions (1,011 bytes, fits ChatGPT's 1,500-character field) |
| Codex and other AGENTS.md readers | [`dist/AGENTS.md`](dist/AGENTS.md) | Copy to your repo root, or append to an existing AGENTS.md |
| Cursor | [`dist/cursor/brainres.mdc`](dist/cursor/brainres.mdc) | Copy to `.cursor/rules/brainres.mdc` |
| Claude Code, without the plugin | `skills/brainres/` | `cp -R skills/brainres ~/.claude/skills/brainres`, then `/brainres` |

Only the plugin install adds the hooks. With the other routes you get the rule card or the skill, not the per-message reminder.

Once installed, it's always on. A session-start hook adds the rule card once per session, and a short reminder rides along with each message, because instructions fade over long sessions.

**Prefer an output style?** The plugin also ships one. Run `/output-style` and pick **brainres**. It applies the same rules and keeps Claude Code's coding instructions. If you use it, set `BRAINRES=off` so the card isn't loaded twice. That also turns off the per-message reminder.

**Measured cost** ([`scripts/token_cost.sh`](scripts/token_cost.sh), Claude's own tokenizer, Sonnet, median of 3):

| Part | Tokens | When |
|---|---:|---|
| Rule card | 418 | once per session |
| Reminder | 79 | each message |
| Full skill body | 3,309 | only when the skill is invoked |

A 20-message session costs about 2,000 extra input tokens before prompt caching. The card's 11 lines were picked by RICE across all findings ([ranking](research/core-card-ranking.md)). To turn it off, run `export BRAINRES=off` or `touch ~/.claude/brainres.off`.

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

It is also **honest, not agreeable**. It checks the premise of your question, agrees only when the evidence supports it, and never flatters. Sycophantic AI raises trust while it harms judgment ([Cheng 2026](research/catalog-judgment-trust.md)).

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

**Score your own README** and show it off:

```bash
python3 skills/brainres/scripts/brainlint.py --badge README.md
# [![Brain Score](https://img.shields.io/badge/Brain_Score-100%2F100_A-2ea44f)](https://github.com/wonjangcloud9/brainres)
```

This README scores 100. The Korean one scores 96 because its hero quotes a deliberately bad 22-어절 sentence.

## How it differs

| | Optimizes for | Grounded in |
|---|---|---|
| terse / caveman-style skills | fewer output tokens | token counts |
| humanizer / anti-slop skills | not sounding like AI | Wikipedia's *Signs of AI writing* |
| **brainres** | **understanding per second of reading** | **725 findings reviewed, each rated for evidence strength** |

brainres keeps what those projects got right: no preamble, protect code and numbers, full sentences for safety warnings. It adds what they don't cover: chunking, define-before-use, reader expertise, calibrated uncertainty, causal explanations, anti-sycophancy, stress-aware procedures, and Korean and L2 reading research. The survey is in [`research/trending-skills.md`](research/trending-skills.md).

## Science, not vibes

Every finding in [`research/`](research/) has a source, an evidence grade (strong / moderate / weak / contested) and either a concrete writing rule or a stated reason for exclusion:

| Catalog | Findings |
|---|---|
| [Core cognitive principles](research/cognitive-principles.md) | 90 |
| [Psycholinguistics & reading (incl. L2 and Korean)](research/catalog-psycholinguistics.md) | 95 |
| [Learning science & learning with LLMs](research/catalog-learning-science.md) | 99 |
| [Attention, neuroscience & neurodiversity](research/catalog-attention-neuro.md) | 96 |
| [Judgment, decision & human–AI trust](research/catalog-judgment-trust.md) | 118 |
| [HCI, information design & program comprehension](research/catalog-hci-infodesign.md) | 115 |
| [Emotion, motivation & conversational pragmatics](research/catalog-emotion-pragmatics.md) | 112 |

The **[coverage ledger](research/coverage.md)** shows 596 applicable findings, all 596 cited by a rule in the skill, and 129 excluded. Exclusions fall into four groups: not applicable to text, failed replication, neuromyth, or manipulative. Cross-domain duplicates are counted once. `validate.sh` blocks any commit that lowers the applied count.

The always-on card stays small (418 tokens). Situation-specific findings live in 13 reference files that Claude reads only when the answer needs them, so applying everything doesn't mean stuffing everything into the prompt.

- **Neuromyths we refuse:** learning styles; left/right brain; the "8-second attention span"; Dale's cone; Bionic Reading; "dopamine-hit" formatting; "23 minutes to refocus"; "willpower is glucose"; "we read words by their shape". Thirty in total are listed in the catalogs.
- **Honest limits:** nobody, us included yet, has run controlled studies on formatting rules for LLM chat answers. The thresholds are engineering defaults to be tuned by evaluation. A human comprehension benchmark is on the [roadmap](BACKLOG.md).

## Built overnight by a loop

The repo improves itself. Every 20 minutes a Claude Code loop takes the top item from the [RICE-scored backlog](BACKLOG.md), implements it, validates it, and pushes. When the backlog runs dry, it researches again. Every iteration is logged in [`LOOP_LOG.md`](LOOP_LOG.md). The protocol is in [`LOOP.md`](LOOP.md).

## Contributing

Issues and PRs are welcome, especially before/after pairs where brainres made an answer *worse*. A rule only gets in if it cites a finding in `research/`.

MIT © wonjangcloud9
