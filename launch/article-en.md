# I measured whether a "readability" prompt really changes Claude's answers. Here's what held up.

*Draft for dev.to / Medium. Every number below comes from [evals/README](https://github.com/wonjangcloud9/brainres/blob/main/evals/README.md).*

**TL;DR**
- On an 80-prompt suite, brainres made Claude's answers 29% shorter and raised a readability score by 4.6 points (95% CI +3.3 to +6.0).
- The cost is real but small: a blinded key-fact check found 1.8 percentage points less detail.
- Several of my own rules didn't work, and the scorer itself was wrong three times. Both are documented.

## Why another prompt

There are popular prompts that make Claude shorter (caveman) or sound more human (humanizer). I wanted one aimed at a different target: how easily a person can read and act on the answer.

So I started with research rather than taste. I reviewed 805 findings from cognitive science, psycholinguistics, decision science and human–AI trust research. Each one is either turned into a writing rule or excluded with a written reason. All 663 applicable findings are cited by a rule, and a CI check stops that number from going down.

## What it is

- **A 500-token rule card,** added once per session in Claude Code. It has 11 rules, for example:
  - put the answer in sentence 1
  - keep at most 4 items per group
  - use prose for reasoning
  - keep numbers and warnings exact
  - end on the next action
- **Two situation lines** that are added only when your message shows the signal. A learner gets "fix their own line, end with a predict-first question". An emergency gets "next action first".
- **brainlint,** a dependency-free scorer for English and Korean. Each check cites the finding behind it.

## How I measured

- **The suite:** 80 prompts, 16 answer types × 5 (debugging, concepts, decisions, yes/no, numbers, stress, refusals, code, and so on), 32 of them in Korean.
- **The comparison:** each prompt was answered with and without the card on Sonnet with tools off, and compared per prompt with 95% confidence intervals.
- **Detail check:** a judge wrote 3–6 key facts per prompt from the question alone, before seeing any answer. It then marked both answers blind, in random order. An Opus judge re-marked a subset and agreed on 94% of marks.
- **Every change is re-measured,** with the decision rule written down before the run.

## Results

| Per prompt, 78 valid pairs | Change (95% CI) |
|---|---|
| Words | **−29%** (−70 to −42 words) |
| Visible output tokens | **−28%** |
| Total output incl. hidden reasoning | −14% |
| Brain Score | **+4.6** (+3.3 to +6.0) |
| Key-fact coverage | −1.8 points (−4.1 to +0.4) |

brainres led in 14 of 16 answer types. The length effect held on Haiku (−27%) and Opus (−28%). Their score gains pointed the same way, but they were not significant on 12–13 pairs.

## What didn't work

A rule only stays if it changes behaviour. These didn't:
- **"Do any math first":** on a savings calculation, sentence 1 was still wrong in 3 of 3 answers. Rewording it as "for math, sentence 1 is the one-line calculation and its result" fixed it, at 9 of 9.
- **An always-on per-message reminder (84 tokens):** Sonnet kept to the rules for 7 turns and about 30k tokens without it, so it's gone. Haiku did need it, so it now switches on only for Haiku.
- **A concept line, a stricter "no offer menus" rule and a "reply in the user's language" line:** I measured each one. None helped, so I reverted them.

## The scorer was wrong, three times

The most useful lesson was that **my own checker created fake weaknesses**:
1. It penalised short bold labels on list items. Research finds heavy emphasis wasted, but harmless.
2. It counted numbered step lists as walls of text.
3. It held Korean to the English bold limit.

Each looked like a brainres weakness until I read the actual answers. After fixing the checks, "stress" went from the weakest answer type (−3.2) to +4.4.

## Costs and limits

- 1.8 points less key-fact coverage, mostly trimmed elaboration. Whole facts were almost never lost: 2 appeared only in baseline answers, 3 only in brainres answers.
- The card makes Sonnet think before answering more often, so sentence 1 appears about 0.5 s later (median). The whole answer still finishes at the same time.
- **Human comprehension isn't measured yet.** A pre-registered browser reading study is in the repo (`bench/`), but nobody has taken it. The scores are a proxy.

## Try it

```bash
claude plugin install brainres --marketplace wonjangcloud9/brainres
```

For Codex, Cursor and other agents, run `npx skills add wonjangcloud9/brainres`. For claude.ai, ChatGPT or Gemini, follow [the guide](https://github.com/wonjangcloud9/brainres/blob/main/docs/use-elsewhere.md).

If an answer still reads badly, [send it in](https://github.com/wonjangcloud9/brainres/issues/new?template=hard-to-read-answer.yml). Real prompts make the next measurement better.

Repo: https://github.com/wonjangcloud9/brainres
