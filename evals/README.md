# Evals

`python3 evals/run.py` asks the 12 questions in [`prompts.jsonl`](prompts.jsonl) twice. That takes 24 headless `claude -p` calls on Sonnet, with tools and MCP disabled, run from an empty directory.

- **baseline:** Claude Code's default behavior.
- **brainres:** the same call, with the plugin's rule card and per-message reminder appended to the system prompt. This stands in for the installed hooks.

Each answer is scored by `brainlint`. Answers, `summary.json` and `REPORT.md` go to `results/<date>/`.


## The 80-prompt suite (V1, in progress)

From 2026-11-13 the main measurement is [`suite.jsonl`](suite.jsonl): 80 prompts, 16 answer types × 5, 32 of them in Korean. The types are debug, concept, decision, yes/no, numbers, procedure, myth, stress, refusal, formal doc, novice, compare, code explanation, code writing, multi-part and advice. It runs baseline vs brainres (card proxy) on Sonnet in chunks of 15 prompts. [`combine.py --prompts suite.jsonl`](combine.py) pairs every chunk run with the current card. Answers that are raw tool-call markup, a tool-less harness artifact, are flagged (`tool_markup`) and excluded.

**After chunks V1a–V1b** (29 valid pairs, 30 prompts run; one baseline answer excluded as tool markup):

| Per prompt | brainres − baseline (95% CI) |
|---|---|
| Brain Score | +2.7 (−0.3 to +5.7) |
| Words | **−57** (−85 to −29), −27% |
| Visible output tokens | **−162** (−229 to −96), −28% |
| Within length budget | 19/29 → 26/29 |

**Which checks fire** (answers flagged out of all answers):

| Check | baseline | brainres |
|---|---:|---:|
| bold lead-in labels on list items | 7 / 29 | 6 / 30 |
| bold overuse | 7 / 29 | 2 / 30 |
| wall of text | 4 / 29 | 3 / 30 |
| long sentences | 3 / 29 | 2 / 30 |

**Early signal for the weakness report (V4):** brainres scored lower on 3 of 15 prompts in V1b and on 2 of 15 in V1a. Bold lead-ins were the most common deduction there. The card's "bold only the token that harms if misread" barely moves them (7 → 6), while it does cut bold overuse (7 → 2). We'll act on this in V4, after the full suite.

## Final result (B09b): 3 samples per prompt per condition

[`combine.py`](combine.py) merges runs made with the same core card. Each run records `card_sha`, so answers from an older card are excluded automatically. The final report is [`results/combined-final.md`](results/combined-final.md), with baseline n=36 and brainres n=36:

| | baseline | brainres | per-prompt difference (95% CI over 12 prompts) |
|---|---:|---:|---|
| Words | 201.7 | 147.3 | −54.4 (−89.1 to −19.6), −27% |
| Output tokens | 662 | 556 | −106 (−179 to −33), −16% |
| Brain Score | 91.2 | 96.2 | +5.0 (+0.8 to +9.2) |
| Within length budget | 29/36 | 32/36 | |
| No preamble / buried answer | 36/36 | 36/36 | |

The length budget is ≤100 words for yes/no and myth questions and ≤300 for everything else. The single-sample first run below overstated the length effect (−33%). This repeated measure supersedes it.

## Korean prompt set (B34)

We ran 12 Korean prompts ([`prompts-ko.jsonl`](prompts-ko.jsonl)) covering debug, concept, decision, yes/no, numbers, procedure, myth, stress, refusal, a formal email, a novice explanation and a comparison. Each was asked with and without brainres on Sonnet, 1 sample each. Results are in [`results/combined-ko12.md`](results/combined-ko12.md). `--prompts` keeps prompt sets from mixing.

| Per prompt | brainres − baseline (95% CI) |
|---|---|
| Words | −30 (−20%; −52 to −8) |
| Visible output tokens | −135 (−18%; −227 to −42) |
| Brain Score | +2.7 (−1.4 to +6.7, CI includes 0) |
| Answers mixing speech levels (해요체/합쇼체/평서체) | baseline **7 / 12** → brainres **1 / 12** |

The effect is smaller than in English (−27%). The clearest Korean gain is consistency of speech level. The one remaining mix is the formal email: 해요체 in the chat wrapper and 합쇼체 in the email body, which is correct.

**Failure found: a premature number in sentence 1 (C17).** On the savings question (300만 원 × 40% per month toward 1억), **both** conditions opened with "약 8년 4개월", computed 6년 11개월 in the next lines, and corrected themselves. That was 1 of 1 per condition in the main run, then 3 of 3 per condition on re-run. Reasoning stays visible, so a careful reader catches it, but a skimmer keeps the wrong headline (NW-06). Models without hidden reasoning have nowhere to "compute first". We added "do any math first, never state an unchecked number" to the card. **It did not help: 3 of 3 still wrong.**

**Fixed (C17).** We changed the card wording to "For math, sentence 1 = the one-line calculation + result". Then we re-ran 3 calculation prompts × 3 samples ([`prompts-calc.jsonl`](prompts-calc.jsonl)) and judged sentence 1 by hand:

| Card wording | Sentence 1 has the right number |
|---|---:|
| original (no math clause) | 0 / 1 |
| "do any math first" | 0 / 3 |
| **"sentence 1 = calculation + result"** | **9 / 9** |

For example: "300만 원 × 40% = 월 120만 원 저축이고, 1억 ÷ 120만 원 ≈ 83.3개월이라서 약 **6년 11개월**이 걸려요."

The baseline was unstable on this prompt. It was wrong in 4/4 earlier runs, but this time it opened with the calculation and was right in all 3. We therefore claim only that brainres's sentence 1 is now reliable, not that it beats the baseline here. The card went from 488 to 498 tokens.

## Code explanations and unstated requirements (B37)

We ran 6 prompts ([`prompts-code.jsonl`](prompts-code.jsonl)) on Sonnet, with 2 samples per condition (24 calls). Four asked to explain code: Python, JS, SQL in Korean and a shell one-liner in Korean. Two asked to write code with unstated requirements. Every answer was judged by hand, and the judgments are in [`results/2026-11-12-code/judged.json`](results/2026-11-12-code/judged.json).

| | baseline | brainres |
|---|---:|---:|
| Explanations whose sentence 1 is a whole-code purpose summary (DV-01, HC-72) | 8 / 8 | 8 / 8 |
| Mean words, explanations | 171 | 140 (−18%) |
| Code answers stating assumptions *before* the code (DV-07) | 0 / 2 | 2 / 2 |

**A ceiling result on summaries.** Default Sonnet already opens code explanations with a purpose summary, and neither condition gave a line-by-line tour. The card needs no change for DV-01.

The assumptions difference is in the expected direction. For example: "This Python function uses only the standard library and skips blank price cells". But with n = 2 it is not evidence. The baseline put its assumptions in notes after the code.

**Harness limit found.** The Korean "write me a script" prompt (x06) made the model try to create a file in all 4 runs. These runs use `--tools ""`, so no file could actually be written. The baseline emitted raw tool-call markup, brainres said "만들었어요" (I made it) about a file that was never written, and one call failed outright. These are artifacts of a tool-less run of Claude Code, which still believes it can act, so x06 is excluded. `run.py` now records a failed call in `summary.json` (`failed`) instead of crashing and losing the whole run.

## Learners with broken code (B38)

We used 4 prompts ([`prompts-learn.jsonl`](prompts-learn.jsonl)) in which a self-described learner shares broken code: Python, JS, Python in Korean and C in Korean. Each ran in 3 conditions × 2 samples on Sonnet (24 calls), and every answer was judged by hand ([`results/2026-11-12-learn/judged.json`](results/2026-11-12-learn/judged.json)).

| | baseline | card (proxy) | plugin |
|---|---:|---:|---:|
| Primary fix is a change to *their* line (DV-03) | 6 / 8 | 6 / 8 | 6 / 8 |
| Ends with a specific "run / try this" check | 0 / 8 | 7 / 8 | 8 / 8 |
| Ends with a predict-first self-test question (DV-04) | 0 / 8 | 0 / 8 | 0 / 8 |
| "Makes sense?" | 0 / 8 | 0 / 8 | 0 / 8 |
| Mean words | 104 | 105 | 107 |
| **The brainres skill was invoked** | n/a | n/a | **0 / 8** |

- **Their own code:** every condition fixed the user's own line for 3 of 4 prompts. The exception was removing items while looping, where all 6 answers led with a list-comprehension rewrite instead of the one-character fix, `for n in nums[:]:`.
- **Endings:** brainres answers end with a concrete check ("change `var` to `let` and run it"), which the baseline never did. No condition asked a real self-test question.
- **The skill never loaded,** so the learner rules in `learn.md` (DV-03, DV-04) never reached the model. Earlier, the skill auto-invoked in 1 of 24 answers. Rules that live only in references apply only when someone asks for the skill. B39 tests adding learner triggers to the skill description.
- **One failure (C18):** a brainres answer opened with the wrong program output (`[1, 5, 2, 4]`), traced the loop, and corrected itself (`[3, 2, 4]`). This is the same premature-value pattern as C17, now for *traced output* rather than arithmetic. It happened in 1 of 8 card answers, 0 of 8 baseline answers and 0 of 8 plugin answers.

### Learner triggers in the skill description (B39): tried and reverted

We added learner triggers to the SKILL.md description ("I'm learning", "beginner", "homework", 공부 중, 배우는 중, 과제; 910 of 1,024 chars) and re-ran with the real plugin:

| | before | after |
|---|---:|---:|
| Skill invoked on the 4 learner prompts × 2 | 0 / 8 | 1 / 8 |
| Skill invoked on the 12 general prompts (false triggers) | 1 / 24 earlier | 0 / 12 |

Even the one invoked answer still led with a rewrite instead of fixing the user's own line, and it asked no self-test question. A description trigger barely changes whether Sonnet loads a skill for a one-shot answer, and loading it did not change the behaviour. **We reverted it,** because it cost about 40 always-loaded tokens for no measured gain. The lever left is the per-turn reminder hook, which sees the prompt and can add one targeted line only when a learner, stress or calculation signal appears (B40).

## Situation-aware reminder (B40)

Rules that live only in skill references reach the model only when the skill loads, which happened in 1 of 24 general prompts and 1 of 8 learner prompts (B38, B39). The per-turn hook does see the prompt, so it now appends **one targeted line only when the prompt shows that situation's signal**. It reads only the `prompt` field, never `cwd` or paths.

We measured each candidate line with the real plugin on Sonnet, with the line off (`BRAINRES_SITUATIONS=off`) and on, 2 samples per prompt (28 calls), judged by hand:

| Line | Behaviour | off | on | Kept? |
|---|---|---:|---:|---|
| **Learner:** "fix their own line first (not a rewrite); end with one predict-first question" | Ends with a predict-first question (DV-04) | 0 / 8 | **8 / 8** | **yes** |
| | Primary fix on the user's own line (DV-03) | 6 / 8 | **8 / 8** | |
| | Mean words | 89 | 109 (+22%) | |
| Math / program output: "sentence 1 = the one-line calculation or trace + result" | Sentence 1 states the right output (3 trace prompts) | 6 / 6 | 6 / 6 | no, no effect |

With the learner line, the loop-removal answers led with the one-character fix to the user's own loop (`for n in nums[:]:`) and ended with questions like "what does `sum_even([1, 3, 5])` return, and why?". The 22% extra words are the question and the trace, and we judged them worth it for a learner. The math line changed nothing, because the plugin was already right on all 3 trace prompts, so it was dropped. C18 (wrong traced output in sentence 1, seen once in the card proxy) did not recur in 12 plugin answers.

**Trigger precision:** the learner regex fires on all 4 learner prompts and on none of the 52 prompts in the other eval sets. `validate.sh` checks the routing, including a `cwd` named `homework/beginner`. The line costs about 20 tokens, an estimate from its 88 characters, and only on turns that match.

### Emergency line (B41)

We tested a third line on 4 stress prompts ([`prompts-stress.jsonl`](prompts-stress.jsonl)): DROP TABLE on production, a site down with a 502, `git reset --hard` with uncommitted work, and a project folder deleted from the terminal. The line reads "Emergency: the single next action first; if the habitual move is harmful, say so up top; ≤5 steps, then why" (from support.md, AN-35/36). We ran it with the real plugin, line off vs on, 2 samples each (16 calls), judged by hand:

| | off | on |
|---|---:|---:|
| Sentence 1 is the next action, not an explanation | 3 / 8 | **6 / 8** |
| A harmful habitual move is flagged before the steps | 4 / 8 | **6 / 8** |
| Mean words | 203 | 197 |

**Kept.** With the line on, the 502 answers opened with "Restarting nginx won't fix a 502…", and the `git reset` answers led with "`git gc`, `git prune`은 실행하지 마세요".

**One loss.** On DROP TABLE, the line-off answers warned up top that new writes make recovery harder (2/2). The line-on answers led with `ROLLBACK;` and moved the "don't recreate the table" warning into step 1 (0/2 up top). n = 8 per condition, so this is a direction, not a proof.

**Trigger precision:** the line fires on the 4 test prompts and on the 2 stress prompts in the other sets. Among the other 52 prompts it also fired on 1 mild case ("깃에서 실수로 main에 커밋했어", via "실수로"). The line is harmless there. It costs about 28 tokens, an estimate from its length, and only on matching turns.

## Decision answers without the skill (B42, no new calls)

decide.md's core shape has two parts: recommend one option in sentence 1, and say when the other option wins (#78, JD-44). It reaches the model only when the skill loads. We re-read 16 saved Sonnet answers to the 4 decision prompts: REST vs GraphQL, list vs tuple in Korean, Vercel vs AWS in Korean, and MacBook Air vs Pro in Korean. Judgments are in [`results/2026-11-12-b42/judged.json`](results/2026-11-12-b42/judged.json).

| | baseline | card | plugin |
|---|---:|---:|---:|
| Sentence 1 recommends one option, or gives the deciding rule | 4 / 4 | 8 / 8 | 4 / 4 |
| Says when the other option is the better choice | 4 / 4 | 8 / 8 | 4 / 4 |

**Another ceiling.** Default Sonnet already opens with "Use REST" or "Vercel을 추천해요" and adds a "when GraphQL would be worth it" section. brainres changes the length and formatting (measured above), not this shape, so no decision line was added. Together with B37 (code explanations) and B43 (agentic final messages), this means several reference rules describe what Sonnet already does. B45 checks whether that holds on Haiku before anything is pruned.

### The same ceilings on Haiku (B45)

We re-ran the explain set (4 prompts × 2) and the decision set (4 prompts × 1) on Haiku, under baseline and card (24 calls). Judgments are in [`judged-b45.json`](results/2026-11-12-b45-decision-haiku/judged-b45.json).

| | baseline | card |
|---|---:|---:|
| Code explanation, sentence 1 is a purpose summary | 8 / 8 | 8 / 8 |
| Decision, sentence 1 recommends or gives the deciding rule | 4 / 4 | 4 / 4 |
| Decision, says when the other option wins | 4 / 4 | 4 / 4 |
| Mean words, explanations | 166 | 133 (−20%) |
| Mean words, decisions | 165 | 102 (−38%) |

Haiku is at ceiling too, so **summary-first code explanations and the recommend-plus-alternative decision shape are default Claude behaviour**. brainres doesn't cause them. The rules stay in the references for other models and contexts. What brainres changes here is length.

**Two card side effects on Haiku.** One of 4 Korean answers with the card came back in English: "This query lists users who…" for "이 쿼리 뭐 하는 거야?". Across every saved run, that is 1 of 16 Haiku card answers to Korean prompts, against 0 of 16 Haiku baseline, 0 of 99 Sonnet card or plugin, and 0 of 8 Opus card answers. One answer to "What does this code do?" opened with "Yes," (1 of 8): card rule 1's yes/no clause was over-applied. Both are tracked as C19.

### Card side effects on Haiku (C19)

We used 6 prompts built to provoke the two side effects ([`prompts-c19.jsonl`](prompts-c19.jsonl)): what/why questions, short Korean questions over code, and a Korean refusal request. Each ran on Haiku with the card, 2 samples, before and after a change (24 calls).

| | before | after |
|---|---:|---:|
| Korean prompt answered in English | 0 / 8 | 1 / 8 |
| Yes/No opener on a non-yes/no question | 1 / 12 | 0 / 12 |
| Mean words | 118 | 116 |

- **"Reply in the user's language" in the per-turn reminder: no effect, reverted.** The same SQL prompt ("이 쿼리 뭐 하는 거야?" over a SQL block) flipped to English again. Across saved runs it has now flipped in 2 of 6 Haiku card answers, and every other Korean prompt has stayed in Korean. This looks like a Haiku-specific pull from an English system prompt plus code-heavy input. It remains open as C20.
- **Card rule 1 now says "*Only* a yes/no question starts with "Yes"/"No"."** Across every saved run, Yes/No openers on non-yes/no questions appeared in 3 of 173 card answers, against 0 of 145 baseline and 0 of 90 plugin answers. After the change they appeared in 0 of 12, against 1 of 12 before. That is too few to show an effect, so it is kept as a zero-cost precision fix, not a measured win. The card stays at 1,349 bytes and is now **500 tokens**, measured; it was 498.

### Haiku answering a Korean SQL prompt in English (C20): not reproducible, nothing changed

We ran the one prompt that had flipped ("이 쿼리 뭐 하는 거야?" over a SQL block) 10 times on Haiku with the current card, and 10 times with "Reply in the user's language." added to the card's first line. To fit the line, other bytes were trimmed, keeping 1,348 bytes. We decided in advance to keep the line only if English answers dropped.

| | current card | card + language line |
|---|---:|---:|
| Answered in English | **0 / 10** | 0 / 10 |
| Mean words | 115 | 95 |

The current card produced no English answers, so there was nothing to fix. With the card, this prompt has now flipped in 1 of 12 runs; an earlier card version flipped 2 of 6. **The card change was reverted.** The word drop was not the outcome we tested, so it is not a reason to keep the change. A residual risk of about 1 in 12 on code-heavy Korean prompts with Haiku is noted here and not acted on.

## Does the per-turn reminder prevent drift? (B46): no, so it was cut

The plugin used to append an 84-token reminder to every message, because instructions are known to drift in long dialogs (Li et al. 2024). We had never measured that on Claude. [`evals/multiturn.py`](multiturn.py) runs scripted 7-turn sessions with the real plugin, resuming one session per conversation, with the reminder on vs off (`BRAINRES_REMINDER=off`; the card stays on). There were 2 conversations (EN and KO), 28 calls on Sonnet. We checked the transcripts: the card was injected once at session start and not again on resume, so this matches a real session.

| Mean per answer | reminder on | reminder off |
|---|---:|---:|
| Brain Score, turns 1–2 | 94.5 | 96.8 |
| Brain Score, turns 3–4 | 100.0 | 98.0 |
| Brain Score, turns 5–7 | 97.0 | **98.7** |
| Words, turns 5–7 | 134 | 123 |

There was no drift without the reminder, so per the pre-stated rule the always-on line was cut. That saves 84 tokens on every message. The hook now emits nothing unless a learner or emergency signal appears; those lines were measured to change behaviour (B40, B41).

**Limit:** 7 short turns is a small context. Long Claude Code sessions full of tool output are not covered. B47 tests that case.

**Long context (B47).** `python3 evals/multiturn.py --long` pastes about 3k tokens of logs or code in each of turns 1–4. The session reaches about 30k context tokens. Turns 5–7 are plain database questions, also asked in fresh sessions as the control (2 samples each). Card only, no per-turn reminder, Sonnet, EN + KO, 26 calls:

| Mean per answer | long session | fresh session |
|---|---:|---:|
| Brain Score, turns 5–7 | **100.0** | 98.0 |
| Words, turns 5–7 | 178 | 159 |

There was no drift at about 30k tokens either, so no periodic reminder was added. Two late-turn answers were first flagged `no_recommendation`, and both were brainlint false positives:
- One answered the PgBouncer-vs-`max_connections` question with "Neither is the first fix, because the error you logged most likely comes from your app's own pool". That uses the pasted log to correct the premise, which is better than the fresh answers.
- The other recommended with "PgBouncer가 대체로 더 나은 선택이에요".

brainlint now accepts both forms, with tests, and the run was re-scored. Before the fix, the long-session mean was 97.3. The long-context answers ran 12% longer, plausibly because they used the pasted context.

## Agentic coding: does the plugin change outcomes? (B32)

[`agentic.py`](agentic.py) copies each of 6 small tasks ([`agentic/`](agentic/): pagination off-by-one, slugify, input validation, half-up rounding, LRU cache, Korean word count) into a temp dir. Claude Code, on Sonnet, gets "Make the tests pass. Do not change the test files", with tools Read/Edit/Write/Glob/Grep (no Bash) and `acceptEdits`. It runs with and without `--plugin-dir`, and the harness runs the tests itself. Results are in `results/2026-11-12-agentic-sonnet/`.

| | Tests pass | Test files modified | Median lines changed | Median words in final message |
|---|---:|---:|---:|---:|
| baseline | 6 / 6 | 0 | 7 | 93 |
| plugin | 6 / 6 | 0 | 7 | 88 |

- **No change in coding outcomes:** same pass rate, same diff size, and the tests were left alone in both conditions.
- **The final report wasn't shorter.** That contrasts with the 27% cut on chat answers. Claude Code's own agentic reporting conventions seem to dominate there. The sample is small (1 run per task).


### Final-message structure (B43, no new calls)

We re-read the 12 final messages from the run above. code.md asks that agentic work end with what changed, what wasn't done and how to verify (HC-35). Judgments are in [`judged-final-message.json`](results/2026-11-12-agentic-sonnet/judged-final-message.json).

| | baseline | plugin |
|---|---:|---:|
| Says what changed | 6 / 6 | 6 / 6 |
| Says what wasn't done, or its limits | 6 / 6 | 6 / 6 |
| Says how to verify | 6 / 6 | 6 / 6 |
| Names a behaviour or limit the tests don't cover | 0 / 6 | 2 / 6 |

**A ceiling result, with a confound.** This harness disallows Bash, so every run *had* to say "I couldn't run the tests" and "run `python -m unittest` to confirm". The first two rows may just reflect that.

The one difference points in the expected direction. Two plugin messages flagged something outside the tests: "`\w+` splits on apostrophes, so *don't* becomes *don* and *t*", and "I also reject `page_size < 1`, which the tests don't require". With n = 6, that is not evidence. No end-of-task line was added. B44 would re-run with test commands allowed, to see the case where tests *can* run.

**Re-run with the test runner allowed (B44).** `python3 evals/agentic.py --allow-tests` auto-approves only `python -m unittest`, and any other shell command is denied in `-p` mode. Results are in [`2026-11-12-agentic-sonnet-tests`](results/2026-11-12-agentic-sonnet-tests/judged-final-message.json).

| | baseline | plugin |
|---|---:|---:|
| Tests pass (checked by the harness) | 6 / 6 | 6 / 6 |
| Sentence 1 reports the test result it actually saw | 6 / 6 | 6 / 6 |
| Names a behaviour or limit the tests don't cover | 3 / 6 | 2 / 6 |
| Median words in final message | 71 | 68 |

Once the tests can run, both conditions open with the observed result ("All 4 tests now pass") and claim nothing the harness contradicts. The beyond-the-tests difference seen without Bash (0/6 vs 2/6) disappears (3/6 vs 2/6), so it was noise. For agentic final messages, the plugin is at parity with default Claude Code.

## Does brainres hide reasoning on error-prone prompts? (B31, inconclusive)

The LR-01 risk is that cutting length removes the reasoning a reader needs to catch a wrong answer (Friedman 2026). [`tricky.py`](tricky.py) asks 8 classic trap questions ([`tricky.jsonl`](tricky.jsonl)) on Haiku, with and without brainres. Results are in `results/2026-11-12-tricky-haiku/`.

| | Correct | Reason within the first 2 sentences | Median words |
|---|---:|---:|---:|
| baseline | 8 / 8 | 2 / 8 | 56 |
| brainres | 8 / 8 | **4 / 8** | 80 |

- **Inconclusive on the real question.** Haiku got every trap right in both conditions, so the "wrong answer" case never occurred.
- **No sign of hidden reasoning.** On these prompts brainres attached a reason to the verdict twice as often ("9.9 is bigger. 9.9 = 9.90, and…").
- **Two lessons about our own tooling:**
  - A whole-text regex first marked several correct answers wrong because the explanations mentioned the tempting wrong answer. Correctness is now judged from sentence 1 and was checked by hand.
  - Prompt t8 was internally contradictory; both conditions correctly pointed this out.
- **B31b followed up** with 10 harder prompts ([`tricky2.jsonl`](tricky2.jsonl)): weekday and date arithmetic, letter counting, 3-digit multiplication, Python aliasing, `[[0]*2]*2`, JS `.sort()`, a pens-pricing problem and leap-year day counts. Results are in `results/2026-11-12-tricky2-haiku/`. Checked by hand, Haiku was **10/10 correct in both conditions** again. Reason within the first 2 sentences was 5/10 for both, and median words were 42 (baseline) and 32 (brainres).
- **Conclusion after 18 prompts:** current models made no natural errors on these traps, so the LR-01 risk can't be observed this way. Testing it needs answers that are wrong by construction, as in Friedman 2026. Where it could be measured, reasoning visibility was equal (5/10) or better (4/8 vs 2/8) with brainres.
- **A small brainres artifact:** one answer opened with "[[0, 0], [0, 0]] is wrong.", refuting an answer nobody had proposed. Repeating a myth the user never held can make it stick (#52). Logged as C16.

## Real plugin vs the card-append proxy (B29)

All earlier runs appended the card and reminder to the system prompt. This run installs the real plugin (`--plugin-dir`, so hooks fire and the skill can be invoked with the `Skill` and `Read` tools) and asks the 12 prompts × 2 samples. Results are in [`results/combined-plugin.md`](results/combined-plugin.md).

| Per-prompt vs baseline (Sonnet) | Real plugin | Card-append proxy |
|---|---|---|
| Words | −54 (95% CI −82 to −27) | −54 (−88 to −20) |
| Brain Score | +5.0 (+0.0 to +10.0) | +5.3 (+0.4 to +10.2) |
| Invented confidence % | 0 / 24 | 0 / 24 |

- **The proxy is valid.** The installed plugin produces the same effect.
- **The hooks do the work.** The skill was auto-invoked in only 1 of 24 answers, the emergency prompt (11). This matches the cost table: the 3,391-token skill body loads rarely, while the 488-token card and 84-token reminder are always present.

## Other models (B28)

The same 12 prompts were run with and without brainres on the current card, 1 sample each. Per-prompt differences are given with 95% CIs ([`results/combined-haiku.md`](results/combined-haiku.md)).

| Model | Words | Brain Score | Output tokens | Invented confidence % |
|---|---|---|---|---|
| Sonnet (3 samples) | −27% (−54; −89 to −20) | +5.0 (+0.8 to +9.2) | −16% (CI excludes 0) | 0 / 24 after C14 |
| **Haiku** (1 sample) | **−35%** (−71; −114 to −28) | **+3.9** (+0.1 to +7.7) | −14% (CI includes 0) | 0 / 12 |
| **Opus** (2 samples) | **−35%** (−80; −113 to −48) | +3.3 (−0.5 to +7.2, CI includes 0) | visible **−36%** (−308; −472 to −144); hidden reasoning +253 (CI −15 to +521) | 0 / 24 |

**Output tokens on Opus (resolved in B28c).** `output_tokens` includes hidden reasoning (`modelUsage.thinkingTokens`). A re-run that recorded the split shows Opus with brainres **thinks more and writes less**:

- Visible output tokens fell by 308 per prompt (−36%, 95% CI −472 to −144).
- Thinking tokens rose by 253 (about 2.6×; CI −15 to +521, borderline).

Total output tokens therefore stay roughly flat on Opus (985 → 1,050, CI includes 0). The reader sees a third less, but the bill doesn't shrink on Opus.

The question-aware check (`--question`) caught one real Haiku slip. In 12, the brainres answer opened with "다음 기준으로 고르면 됩니다." and put the recommendation in sentence 2 (`no_recommendation`).

## Stress prompt with the real plugin (C13)

Card-only evals can't reach `support.md` because skill references load only when the skill is invoked. We ran the emergency prompt (11, "I deleted a production table") through the real plugin (`--plugin-dir`, tools `Skill Read`), 3 times before and 3 times after adding stress triggers to the skill description:

| | Old description | Description with stress triggers |
|---|---|---|
| Skill invoked | 0 / 3 | 1 / 3 |
| ≤5 numbered steps (support.md rule) | 2 / 3 | 3 / 3 |
| Mean Brain Score (rescored with the fixed brainlint) | 87.7 | 87.3 |

This is a partial effect on a tiny sample. The description change costs nothing always-on, so we kept it. The stress rule stays off the always-on card because its RICE score (3) is below the card's cut line ([ranking](../research/core-card-ranking.md)).

While doing this, brainlint got two fixes. `fragmented_reasoning` now ignores numbered steps, because steps are the right shape for procedures (#15). Nested list items no longer count toward the parent list. Scores in older `summary.json` files were computed with the scorer as it stood at run time.

## Interplay with built-in output styles (B24)

The style is passed with `--style` (`--settings {"outputStyle": ...}`). We used 4 prompts (01, 03, 08, 10), 1 sample each, comparing each style alone with the same style plus brainres. Results are in `results/2026-11-12-style-*`.

| Style | Mean words: alone → + brainres | Mean Brain Score | Notes |
|---|---|---|---|
| Explanatory | 307 → 224 (−27%) | 92.8 → 98.5 | ★ Insight blocks kept in 4 of 4 answers |
| Concise | 125 → 154 (+23%) | 95 → 95 | brainres adds decision support (when to switch, next step) |

There were no invented confidence numbers in any condition. The Learning style was not tested. The sample is tiny, so this documents the direction only.

## Regression found while building the benchmark (C14)

While writing quiz questions, we noticed brainres answers stating confidence numbers with no basis, such as "~80% likely on Homebrew Python", "Roughly 80% of small internal tools…" and "(~90% 확신)". A count across all answers:

| | Answers with an ungrounded confidence % |
|---|---:|
| baseline | 0 / 36 |
| brainres | **6 / 36** |

The cause is card rule 8, "uncertainty … as a number". Our own catalog warns against exactly this: spurious precision signals false confidence (JD-33, Jerez-Fernandez 2014). We count it as a real harm introduced by brainres.

**Fixed (C14).** Rule 8 now reads: "say what is unsure and how to check it. Use a number only if grounded (a measured rate, a calculation, a source); never invent a confidence %". `brainlint` gained an `invented_confidence` check.

| Card | Answers flagged by `invented_confidence` |
|---|---:|
| baseline | 0 / 36 |
| v2.1 (old rule 8) | 7 / 36 |
| **v2.2 (fixed)** | **0 / 24** |

On card v2.2 the length gain held: per prompt, words −54 (95% CI −88 to −20) and Brain Score +5.3 (CI +0.4 to +10.2) ([`results/combined-c14.md`](results/combined-c14.md)). The card cost rose from 461 to 488 tokens.

## First run (2026-11-12)

| Metric | baseline | brainres |
|---|---:|---:|
| Mean Brain Score | 91.6 | 93.5 |
| Median words | 210 | 140 (−33%) |
| Mean output tokens | 710 | 537 (−24%) |
| No preamble / buried answer | 12/12 | 12/12 |

Per-prompt results are in [`results/2026-11-12/REPORT.md`](results/2026-11-12/REPORT.md).

What this does and doesn't show:

- **Claude Code already answers first.** The baseline had no preambles in any of the 12 answers, so brainres's measurable effect here is **shorter answers with fewer formatting violations**, not answer-first.
- **Two prompts regressed.**
  - 09 (Korean concept, 88 → 82): two sentences run over 20 어절. The always-on card has no Korean line; the Korean rules live only in the skill's references (follow-up C12).
  - 08 (HTTPS, 94 → 84): the brainres answer was 291 words against 456, but it drew wall-of-text and bold-lead-in penalties. brainlint barely penalizes raw length, so the longer baseline scored higher.
- **Follow-up C12 is done.** After the Korean line was added to the card, a re-run of the 4 Korean prompts × 2 samples gave 0 of 8 answers with sentences over 20 어절 (before: 2 of 4). The mean Korean score went from 89.2 to 93.9 ([results](results/)). The stress prompt (11) still overuses bullets (82), and that is next to check.
- **The sample is small.** It is 12 prompts with one sample each, and LLM output varies between runs. Treat the gaps as directional (follow-up B09b repeats each prompt).
- **brainlint is a proxy.** It measures rule violations, not comprehension. Measuring comprehension needs people (B10).
