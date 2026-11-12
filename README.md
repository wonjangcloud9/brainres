# 🧠 brainres

**Claude answers your brain can actually read.**

English · [한국어](README.ko.md)

`caveman` makes Claude shorter. `humanizer` makes it sound human.
**brainres makes it understandable.** It reviews **801 findings** from cognitive science, psycholinguistics, decision science and human–AI trust research. Each finding is either applied as a writing rule or excluded with a stated reason.

[![Claude Code plugin](https://img.shields.io/badge/Claude_Code-plugin-d97757)](#install) [![coverage](https://img.shields.io/badge/findings_applied-659%2F659-2ea44f)](research/coverage.md) [![reviewed](https://img.shields.io/badge/findings_reviewed-801-blue)](research/) [![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE) [![Brain Score](https://img.shields.io/badge/Brain_Score-100%2F100_A-2ea44f)](https://github.com/wonjangcloud9/brainres)

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

The answer is in sentence 1. The mechanism comes as a causal chain, with one worked fix and a way to verify it, and the answer ends on a next action. Six full before/after pairs, covering debugging, a Korean decision, a concept, a comparison, risk numbers and a misconception, are in [`examples/`](examples/). Score your own text with [`brainlint`](#brainlint).

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

Only the plugin install adds the hooks. With the other routes you get the rule card or the skill, not the situation lines.

Once installed, it's always on. A session-start hook adds the rule card once per session. A per-message hook adds one short line only when your message shows a learner or emergency signal. We dropped an always-on per-message reminder after 7-turn sessions scored just as well with it turned off ([B46](evals/README.md)).

**Prefer an output style?** The plugin also ships one. Run `/output-style` and pick **brainres**. It applies the same rules and keeps Claude Code's coding instructions. If you use it, set `BRAINRES=off` so the card isn't loaded twice. That also turns off the situation lines.

**With Claude Code's built-in output styles.** The hooks work alongside any style. We ran a small test (4 prompts, 1 sample each, so treat it as directional):

| Style | Words: style alone → + brainres | Brain Score | Style features kept |
|---|---|---|---|
| Default | 202 → 147 (−27%) | 91.2 → 96.2 | n/a |
| Explanatory | 307 → 224 (−27%) | 92.8 → 98.5 | ★ Insight blocks: 4 of 4 |
| Concise | 125 → 154 (+23%) | 95 → 95 | n/a |

With Concise, brainres puts back the "why / when to switch / next step" content that Concise strips out. If you want the shortest possible answers, Concise alone, or brainres `scan` mode, is shorter. Details are in [`evals/README.md`](evals/README.md).

**Measured cost** ([`scripts/token_cost.sh`](scripts/token_cost.sh), Claude's own tokenizer, Sonnet, median of 3):

| Part | Tokens | When |
|---|---:|---|
| Rule card | 500 | once per session |
| Situation line | about 20–28 | only on learner or emergency messages |
| Full skill body | 3,391 | only when the skill is invoked |

A 20-message session costs about 500 extra input tokens before prompt caching, plus about 25 for each learner or emergency message. The card's 11 lines were picked by RICE across all findings ([ranking](research/core-card-ranking.md)). To turn it off, run `export BRAINRES=off` or `touch ~/.claude/brainres.off`.

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
| 9 | **Calibrate instead of hedging.** Say what's uncertain and how to check. Use numbers only when grounded, never an invented `~80% sure`. | Numeric uncertainty keeps trust (van der Bles 2020); first-person hedges cut overreliance (Kim 2024) |
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

**Give it the question** with `--question "Is X safe?"` to add two checks. A yes/no question must start with Yes or No, and a choice question must recommend an option in sentence 1.

**Try it in your browser** with the [Brain Score playground](playground/). Paste any answer or doc and get its score. It runs this exact `brainlint.py` through Pyodide, and nothing is uploaded. Once the owner enables Pages it lives at `https://wonjangcloud9.github.io/brainres/playground/`; until then, use a static preview such as htmlpreview.

**Score your own README** and show it off:

```bash
python3 skills/brainres/scripts/brainlint.py --badge README.md
# [![Brain Score](https://img.shields.io/badge/Brain_Score-100%2F100_A-2ea44f)](https://github.com/wonjangcloud9/brainres)
```

**Use it in CI.** A reusable GitHub Action scores your docs on every PR and fails below a threshold. It also writes a summary table:

```yaml
- uses: wonjangcloud9/brainres@main
  with:
    files: "README.md docs/**/*.md"
    min-score: "80"
```

This README scores 100. The Korean one scores 96 because its hero quotes a deliberately bad 22-어절 sentence.

## Measurement

We ran an 80-prompt suite with and without brainres on Sonnet with tools off. It covers 16 answer types, 5 prompts each, and 32 of the prompts are in Korean.

We compared 78 pairs. Two prompts were dropped because an answer was raw tool-call markup. Details are in [`evals/`](evals/).

| | baseline | brainres | per-prompt difference (95% CI) |
|---|---:|---:|---|
| Words per answer | 196 | **140** | **−29%** (−56 words; −70 to −42) |
| Visible output tokens | 670 | **480** | **−28%** (−190; −230 to −150) |
| Output tokens incl. hidden reasoning | 674 | **582** | −14% (−91; −136 to −47) |
| Within length budget | 57/78 | **71/78** | |
| Brain Score | 91.8 | **96.4** | **+4.7** (+3.0 to +6.3) |

An earlier 12-prompt × 3-sample run pointed the same way: −27% words and +5.0 Brain Score.

What this shows:

- Claude Code already avoids preambles, so brainres's measurable effect is **shorter answers with fewer readability violations**.
- **brainres was ahead in 14 of 16 answer types.** It was behind in stress (−3.2) and debugging (−2.5), mostly because of bold lead-in labels and long step lists ([weakness report](evals/results/suite-weakness.md)).
- **The real plugin matches the eval proxy** (12-prompt set): −54 words and +5.0 Brain Score per prompt. The always-on card does the work, and the full skill was auto-invoked in only 1 of 24 answers.

Caveats:

- **Shorter answers carry slightly less detail:** 94.1% of key facts covered, against 96.0% for baseline (−1.8 pp, CI −4.1 to +0.4). Secondary details were cut, but facts were rarely dropped ([V2](evals/README.md)).
- **Hidden reasoning rose by about 100 tokens per answer,** so total output tokens fell 14% while visible tokens fell 28%.
- **Some rules describe default behaviour.** Opening a code explanation with a purpose summary, and opening a decision with a recommendation plus when the other option wins, were already 100% in baseline Sonnet and Haiku. brainres doesn't cause them ([B37, B42, B45](evals/README.md)).
- Comprehension itself isn't measured yet. That needs human readers ([B10](BACKLOG.md)).

Accuracy: across 48 trap and multi-step math problems on Haiku, brainres and baseline both scored 48/48. On 6 agentic coding tasks in Claude Code, both passed 6/6 with identical diff sizes. There is no detectable accuracy cost, but this is a ceiling result ([details](research/llm-side-effects.md)).

Korean (12 prompts): answers came out 20% shorter, and answers that mixed speech levels fell from 7 of 12 to 1 of 12. A failure we found and fixed: on a savings calculation, answers stated a wrong number in sentence 1 and corrected it later. Telling the model to put the one-line calculation *in* sentence 1 fixed it, with 9/9 correct; telling it to "compute first" had not ([details](evals/README.md)).

Across models ([per-model table](evals/README.md)):

- Answers came out 35% shorter on both Haiku and Opus, with 95% CIs excluding zero.
- On Opus the Brain Score gain (+3.3) isn't significant. Opus also *thinks* more with brainres: visible output fell 36%, but hidden reasoning rose about 2.6×, so its total token bill stays flat.

What went wrong along the way ([details](evals/README.md)):

- A single-sample run first showed −33% words. The bigger sample shrank the effect, and we report the bigger sample.
- An early card made Claude invent confidence numbers (`~80% sure`) in 7 of 36 answers, against 0 of 36 for the baseline. After we rewrote the rule, the re-run had 0 of 24, with the length gains intact.

### Help measure comprehension (10 minutes)

The open question is whether people actually understand brainres answers better. The [reading benchmark](bench/) is pre-registered: 8 short answers, unlabeled, with timed questions. You submit an anonymous JSON result through an issue form, and every result will be published, good or bad.

## How it differs

| | Optimizes for | Grounded in |
|---|---|---|
| terse / caveman-style skills | fewer output tokens | token counts |
| humanizer / anti-slop skills | not sounding like AI | Wikipedia's *Signs of AI writing* |
| **brainres** | **understanding per second of reading** | **801 findings reviewed, each rated for evidence strength** |

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
| [Round 2: cross-cultural pragmatics, diagrams, argumentation, news structure, numeracy](research/catalog-round2.md) | 50 |
| [Round 3: how people read LLM answers (2025–2026)](research/catalog-round3.md) | 6 |
| [Round 4: Korean readability](research/catalog-round4.md) | 5 |
| [Round 5: how people use LLM coding help](research/catalog-round5.md) | 7 |
| [Round 6: plain language and politeness](research/catalog-round6.md) | 2 |
| [Round 7: streaming answers (a gap)](research/catalog-round7.md) | 4 |
| [Round 8: risk and numeracy](research/catalog-round8.md) | 2 |

The **[coverage ledger](research/coverage.md)** shows 659 applicable findings, all 659 cited by a rule in the skill, and 142 excluded. Exclusions fall into four groups: not applicable to text, failed replication, neuromyth, or manipulative. Cross-domain duplicates are counted once. `validate.sh` blocks any commit that lowers the applied count.

The always-on card stays small (500 tokens). Situation-specific findings live in 13 reference files that Claude reads only when the answer needs them, so applying everything doesn't mean stuffing everything into the prompt.

- **Neuromyths we refuse:** learning styles; left/right brain; the "8-second attention span"; Dale's cone; Bionic Reading; "dopamine-hit" formatting; "23 minutes to refocus"; "willpower is glucose"; "we read words by their shape". Thirty in total are listed in the catalogs.
- **Honest limits:** nobody, us included yet, has run controlled studies on formatting rules for LLM chat answers. The thresholds are engineering defaults to be tuned by evaluation. A human comprehension benchmark is on the [roadmap](BACKLOG.md).

## Contributing

Issues and PRs are welcome, especially before/after pairs where brainres made an answer *worse*. A rule only gets in if it cites a finding in `research/`.

MIT © wonjangcloud9
