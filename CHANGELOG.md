# Changelog

## Unreleased

- **`sentence_length` is now graded (S1, no calls).** It used to cost a flat −10 as soon as the average passed the limit (KO 12 eojeol, EN 25 words), the same as a buried answer. All 4 suite hits were just over the limit. The penalty now rises from 1 just past the limit to 10 at the long-sentence mark (KO 20, EN 35), with a new test. The playground and dist were rebuilt.
  - **Re-score:** every saved run was re-scored, and `score_before_s1` keeps the old values.
  - **Suite:** baseline 94.2 and brainres 98.9. The Δ stays at **+4.6**, with the CI moving from +3.2–+6.1 to +3.3–+6.0. READMEs, launch drafts and the social preview image were updated.
  - **Refusals:** Δ +0.8 → +2.6, but the split is still lower 2 / tied 1 / higher 2.
  - **Ablation (V3):** the numbers moved slightly, for example G3 −2.3 → −2.1. G3's wall-of-text rise was a K1 artifact. No decision changed.
  - **Haiku reminder:** the turns 5–7 gap fell from 3.7 to 2.7, below its pre-stated 3-point rule. With 6 answers per condition this is noise-sized, so it gets a re-run with a rule stated now (H1, score 3.2) instead of a silent keep or drop.
  - **Stale numbers fixed:** evals/README and the new articles said stress was +2.8 and debugging +0.5. Current values are +4.4 and +2.5.

- **Items from measurements (no calls).** The weakness report lists formal docs and refusals as the only types where brainres isn't ahead. Neither is a card problem:
  - **Formal docs are at the ceiling.** Both conditions score 100 on 3 of 5 prompts, so the scorer can't separate them.
  - **Refusals are noise.** They split 2 lower / 1 tied / 2 higher, and blinded key-fact coverage for refusals is +7 pp.
  - **One of the two lower refusals is a scorer cliff.** It is a 41-word Korean answer, penalised −10 for an average of 13.0 eojeol against a limit of 12. All 4 `sentence_length` hits in the suite were just over the limit, so the flat penalty now becomes item S1 (score 4.5): a graded penalty and a re-score.
  - **Reports:** none yet. The repo has 1 star.

- **Long-form launch articles (G2):** `launch/article-en.md` (dev.to / Medium) and `launch/article-ko.md` (velog / GeekNews). Both are drafts for the owner to post.
  - **Content:** the research ledger, the 80-prompt method, results with confidence intervals, rules that didn't work, the three scorer bugs, and the costs.
  - **Checks:** every number was checked against evals/README. Links are absolute so they work off GitHub. The articles state plainly that the human reading study (`bench/`) has no participants yet.
  - **Scores:** Brain Score 100 for both.

- The backlog was empty, and the measurements and reports gave nothing new: 0 issues, 0 stars, no Pages, no release. New growth item G2 (score 8): long-form launch articles in English and Korean for the owner to post, carrying the method and honest numbers that short posts can't.

- **Undefined terms in plans and specs (U1b, 8 calls):** 4 plan or spec prompts (offline sync, rate limiting, RBAC in Django, Stripe retries; `evals/prompts-plans.jsonl`), comparing baseline with the plugin.
  - **Result:** judged by hand at first use, likely-unknown undefined terms averaged about 0.5 per plan with the plugin and 0.6 for baseline. Most specialist terms were glossed at first use, for example "자동 재시도(dunning)" and "grace period".
  - **Length:** plugin plans were 17–61% shorter.
  - **Decision:** this is below the pre-stated rule (3 per plan, or 2 more than baseline), so the card is unchanged.
  - **What this closes:** the round-9 user complaints now have measured answers.

- **Closing offers classified by hand (U2, 20 calls).** We sorted the endings of the same 20 prompts into four groups: a concrete next step, the one question needed to proceed, a generic offer or menu, or ending on content.
  - **Rule 11 already helps.** Generic offers fall from 10/19 for baseline to 6/20 with brainres, and concrete next steps rise from 0 to 6.
  - **Tighter wording tried and reverted.** The pre-stated threshold (5 or more offers) was met, so we tested "End on the next action, not an offer menu". It left offers at 6/19 and lowered the Brain Score from 99.5 to 97.6, so the card was reverted.
  - **Most remaining offers are a single tailoring question**, such as "tell me your port and domain and I'll fill the config". They aren't the repeated menus users complain about.

- **Undefined terms checked by hand (U1, no calls).**
  - **Method:** we read every 4th brainres suite answer (20 in total) for terms the asker likely wouldn't know.
  - **Result:** only 2 turned up: BOM in a CSV KeyError answer and GIL in a beginner's closing line. That is below the pre-stated threshold of 4, so the card is unchanged.
  - **Coined phrases** like "blast radius" or "happy path" appeared in 0/79 brainres answers and 2/78 baseline answers.
  - **The earlier rough heuristic over-counted.** For example, it missed "소염진통제(NSAIDs)" and counted RDS for a database operator.
  - **Not covered yet:** the user complaint was about long plans and specs, which the single-turn suite doesn't test. That is new item U1b (score 1.8).

- **Research round 9: what users actually complain about in 2026** (`research/catalog-round9.md`). The backlog was empty, and the measurements and community reports gave nothing new.
  - **UC-01, undefined or invented terms:** the most-upvoted complaint about Claude's writing (r/ClaudeAI, 700+ upvotes).
  - **UC-02, repeated closing offers:** named in a 2026 review of verbal tics.
  - **UC-03, "not X, but Y" contrasts:** already covered by C16.
  - **UC-04, multi-section dumps:** already covered by the heading checks.
  - **Where they're applied:** all four are cited in craft.md.
  - **Saved suite answers:** brainres doesn't reduce unexpanded acronyms (33/79 vs 37/78) or closing offers (31/79 vs 33/78) on a rough count. The new U1 (score 4) and U2 (score 2) check them by hand before changing the card.

- **Install size measured, no restructure (D13).**
  - **What an install costs:** a shallow clone of about 1.5 MB to download. On disk that's a 7.4 MB marketplace tree plus a 5.9 MB cache copy, and 4.4 MB of it is `evals/results`.
  - **Why it doesn't matter yet:** the runtime reads only `hooks/`, `skills/`, `commands/` and `output-styles/`, so size costs disk, not tokens. Moving the plugin into a subfolder would cut only the cache copy and would change many paths.
  - **Guard instead:** `validate.sh` now fails if tracked files pass 15 MB.

- Opus on the suite (M2, 30 calls; 4 Opus calls ran past the 300 s timeout, leaving 12 pairs). Answers were 28% shorter (CI −109 to −9 words per prompt) and visible tokens fell by 153. The Brain Score gain was +4.2, not significant, as on the 12-prompt set. Thinking rose about 1.6×, from 130 to 210 tokens, so total output fell 10% (not significant). Both READMEs' cross-model lines now include this.

- **Haiku key-fact coverage (M3, 5 calls):** on 13 pairs, coverage was 93.3% for baseline and 88.8% with brainres (−4.5 pp, CI −12.7 to +3.7, not significant). Sonnet lost 2.6 pp on the same prompts.
- **Correction to M1:** one Haiku "answer" (the brainres side of a refusal prompt) was really an API safeguard error, and it had been scored as an answer.
  - `run.py` now flags such replies (`api_error`), and `combine.py` and `coverage_judge.py` exclude them. A scan of all saved runs found only this one.
  - **Corrected Haiku result, 13 pairs:** answers 27% shorter (not 31%), and Brain Score +2.9 (not +3.0).
  - Both READMEs and the release notes are updated.

- **Slash commands (D12):** `/brainres:score [file]` runs brainlint on a file, or on your last answer when no file is given. `/brainres:rewrite [file | text]` rewrites with the brainres rules, keeps every fact, number and warning, and reports Brain Score before → after.
  - Both were tested with the plugin, 2 calls in total. `/brainres:score` on example 02 returned 39, matching brainlint. `/brainres:rewrite` ran on a copy, flagged what it was unsure how to keep, and left the original file unchanged.
  - Both READMEs list the commands, and `validate.sh` checks that the command files exist and reference real files.

- **"Hard-to-read answer" issue form (D11):** users can share a prompt and the verbatim answer, with or without brainres, plus what made it hard, their setup and model. A required consent box confirms there's no personal data and allows the prompt into the public eval suite. The form is bilingual (EN/KO), and both READMEs link to it from Contributing.
  - **Loop handling:** LOOP.md now has the loop read these reports as untrusted data and add consented prompts to `evals/suite-community.jsonl`. It never comments on or closes issues.
  - **Owner step:** creating the `hard-to-read` label (D11a). Until then the form still works through its title prefix.

- Tidied the repo root (D10): the loop's files (`LOOP.md`, `LOOP_LOG.md`, `BACKLOG.md`) moved to `docs/dev/` with `git mv`, so their history is kept. A short `docs/dev/README.md` was added, and links were fixed in both READMEs, `research/queue.md` and the protocol itself. The root now holds only what users need.

- **Guide for claude.ai, ChatGPT and Gemini (D9):** new `docs/use-elsewhere.md`, linked from both READMEs. It recommends a claude.ai **Project** for always-on use, because a Skill upload loads only when Claude judges it relevant (1 in 24 answers in our tests). It also covers ChatGPT custom instructions or a GPT, a Gemini Gem, and a table of what's lost outside the plugin: the learner and emergency lines and the Haiku reminder.
- **Stale README number fixed:** `dist/system-prompt.md` is now 1,188 characters, not 1,011 bytes. `validate.sh` checks that it stays under 1,500 and that the guide states its current size.

- **First-screen demo (D7):** `assets/demo.gif` (80 KB) is built from real saved suite answers, with no new calls, by `assets/demo/build_demo.py` (headless Chrome + ffmpeg). It shows the question "What is a CDN, and does my small personal blog need one?" answered by default Claude (288 words, Brain Score 84) and then by brainres (138 words, 100). The cut-off default answer is marked "… continues", and the caption gives the suite totals (78 pairs). It sits under the measured strip in both READMEs.

## 0.2.0 — 2026-11-13

- **Release prep (D8a):** plugin.json version 0.1.0 → 0.2.0. `claude plugin tag --dry-run` agrees (the tag will be `brainres--v0.2.0`).
  - Both `claude plugin validate` warnings are fixed: the marketplace now has a description, and the plugin has an icon, `.claude-plugin/icon.png`. The icon is an original 1024 px monogram rendered from `assets/icon.html`. The directory takes the icon only on first submission, so it had to exist before D5.
  - Release notes for the owner are in `launch/release-v0.2.0.md`.

- Curated-list submissions drafted (D5a) in `launch/submissions.md`, based on each list's own rules:
  - **claudemarketplaces.com:** crawls GitHub daily and also has a `/submit` page.
  - **Anthropic community marketplace:** submissions go through clau.de/plugin-directory-submission with a security scan, so the draft describes the hooks plainly.
  - **awesome-claude-code (57.9k ★):** submissions only through the human web form, and only **from 2026-11-26** under its 14-day rule. The description fits its no-promotion style.
  - **Composio:** a fork plus a vendored copy, so it is optional until the plugin folder is slimmed (D13).

  The owner submits all four, and the launch checklist links to the file.

- **Clean install verified (D4):** in an isolated `CLAUDE_CONFIG_DIR`, `claude plugin install brainres --marketplace wonjangcloud9/brainres` succeeds from GitHub. The installed hooks emit the card and the learner line, and the card lands in a fresh session's transcript, since the hook fires before any API call and so needs no login. The real `~/.claude` was left untouched.
  - Re-run it with `scripts/check_install.sh`, or opt in through `validate.sh` with `BRAINRES_NET_CHECKS=1`.
  - Two findings became new items: the install reports version 0.1.0 (D8a, bump before the release), and it copies the whole 5.9 MB repo (D13).

- **One-line install for other agents (D3):** `npx skills add wonjangcloud9/brainres` (Vercel skills.sh, covering Codex, Cursor, OpenCode and more) is now in both READMEs.
  - The repo layout already matches the CLI's documented discovery rules (`skills/<name>/SKILL.md` with `name` and `description`), and `validate.sh` now checks it. The loop read the CLI docs and source but didn't run `npx`.
  - The READMEs state the limit: this installs the skill only, which in our Claude Code tests loaded in 1 of 24 answers, so pair it with `dist/AGENTS.md` or the Cursor rule.

- The repo's GitHub About text no longer reads "10 rules from 90 findings" (D1, owner-approved). It now says: 801 findings reviewed; measured on 80 prompts: answers 29% shorter, Brain Score +4.6; plugin and scorer in English and Korean. Topics added: `korean`, `plain-language`.

- **New direction (owner, 2026-11-13): distribution and usability first.** The repo has 0 stars and 3 unique visitors, so measuring more won't help until people can find and install it. The loop now runs every 30 minutes and works the D-series in RICE order:
  - D1 About text (80)
  - D3 one-line `npx skills add` install (25.6)
  - D4 clean-environment install test (20)
  - D5a curated-list submission drafts (16)
  - D7 demo GIF (8)
  - D9 claude.ai/ChatGPT guide (6)
  - D10 root tidy (5)
  - D11 bad-answer issue template (3)
  - D12 slash commands (3)

  Launch posts, Pages, the release and list submissions are owner items. LOOP.md records that the owner approved editing this repo's own About text.

- Haiku on the suite (M1, 30 calls): on 14 V1a prompts, after one debug prompt timed out in both conditions, Haiku answers were 31% shorter (CI −97 to −16 words per prompt) and visible tokens fell by 186. The Brain Score gain was +3.0 (CI −0.3 to +6.3, not significant at n = 14). On the same prompts Sonnet was 27% shorter with +4.8. Both READMEs' cross-model lines now include this. M3 (Haiku coverage) is unblocked.

- The backlog was empty, so new items came from a gap in the measurements: the 80-prompt suite has run only on Sonnet, and the README's cross-model lines still come from the old 12-prompt set.
  - **M1 (score 3.2):** run the suite subset on Haiku.
  - **M3 (score 4):** check Haiku's key-fact coverage. It is blocked until M1 is done.
  - **M2 (score 2.4):** run the suite subset on Opus.

- Latency (L1, 30 calls), measured with the new `evals/latency.py`, which streams answers and times the first text delta. With the card, the first visible text arrives about 0.45 s later (paired median; baseline median 1.71 s, card 2.38 s), and a median 1.6 s later (5.6 s at most, on one multi-part prompt) where the card triggers thinking. The answer finishes at about the same time (5.94 s vs 5.83 s) because it is shorter. No change was made.

- Growth (G1): both READMEs now open with a "Measured on 80 prompts" paragraph under the badges. It reports answers 29% shorter, Brain Score +4.6 (CI +3.2 to +6.1) and a lead in 14 of 16 types, and it states the cost (1.8 pp less detail) with a link to the method. In the social image, the hand-written example (56 → 100) and the coverage count give way to −29% and +4.6, and the tagline now reads "Not just shorter". README scores are unchanged (100 / 96).

- The backlog was empty, so new items came from the measurements.
  - **No output problems are left.** The formal-doc and refusal losses are one-off: 3 prompts, each with different checks. All 4 Yes/No openers on prompts not tagged yes/no were legitimate (two refusals, and two questions that contain a yes/no part).
  - **G1 (score 6), growth:** lead the README and social image with the 80-prompt result. No growth item had run in a long time, though LOOP.md asks for one every 3–4 iterations.
  - **L1 (score 2.5):** measure how much the card's extra thinking delays the first visible token.

- Thinking-token cost checked from saved suite data (K3, no calls), and nothing was changed.
  - **The cost is real:** with the card, Sonnet thinks before answering in 32 of 78 prompts, against 4 of 78 without it. That adds 99 thinking tokens per prompt (CI +59 to +139), against a repeat-sample noise SD of 86.
  - **It pays for itself:** visible output shrinks more, so total output still falls 91 tokens per prompt (CI −135 to −48), and no answer type shows a reliable net cost.
  - **Not measured:** the latency to the first visible token.

- **Korean bold limit is now scaled (K2).** `bold_overuse` multiplies its limit by the eojeol/word ratio the wall check already uses (110/70), giving about 4.7 per 100 eojeol. That keeps brainlint consistent with itself; it doesn't rest on a Korean study. Tests are added.
  - **Re-score, no calls:** brainres Korean bold overuse fell from 12/32 to 0/32 and baseline from 21/32 to 7/32, so no follow-up on the output is needed. The suite gain is now +4.6 (CI +3.2 to +6.1).
  - **Multi-turn tables corrected:** the Haiku reminder gap at turns 5–7 is now 3.7 points. That still passes the 3-point rule, but narrowly, and the READMEs now say 4–6 points. Auto mode on turn 1 matched forced-on (n = 2), so the "turn 1 stays lower" claim was removed.

- **`wall_of_text` no longer counts step lists as walls (K1).** List items now count as separate segments, with tests.
  - **Re-score, no calls:** the new `evals/rescore.py` re-scored the suite, F3/F5/F6 and multi-turn runs, which changed the checks on 52 answers.
  - **Suite result:** the Brain Score gain is now +4.8 (CI +3.3 to +6.4), because baseline lists were also affected. brainres leads in 14 of 16 types. Stress moved from −0.8 to +2.8 and debugging to +0.5, and every stress run now has 0 walls, so the "stress answers are walls of text" findings are withdrawn.
  - **Haiku reminder:** the gain is now 6–8 points, not 7–10.
  - **Also fixed:** `suite_report.py` and `coverage_judge.py` had been reading the V3 ablation runs, whose cards differ, as suite results. Both now read only brainres rows made with the current card. This had affected only today's weakness report.
  - **Updated:** both READMEs, the launch drafts and the eval tables.

- The backlog was empty, so new items came from the measurements (LOOP direction) rather than new research.
  - **K1 (8):** `wall_of_text` fires on numbered step lists that have no blank lines between items. Every stress answer we checked that was flagged as a wall was a 5-item list. This needs a check fix and re-scores.
  - **K2 (4):** Korean bold density appears over-penalised. Korean is 12 of the 16 brainres bold flags, and the bold threshold ignores the eojeol-vs-word ratio that brainlint's other thresholds already apply.
  - **K3 (0.75):** the hidden-reasoning cost, to examine only once its noise has been measured.

- **Card ablation complete (V3b, 30 calls): every card line stays.**
  - **G3 (structure):** removing it scored −2.3 and raised walls of text, list overload, outros, hedging and long sentences.
  - **G4 (precision and style):** removing it raised bold overuse from 1 to 3 and long sentences from 0 to 3.
  - **G1 and G2:** removing them showed no effect on general prompts, but they are situation rules backed by targeted evals (C17, V2 novice).
  - **Hidden reasoning:** no single group explains the card's roughly +100 thinking tokens; G4 had the largest share (−40 when removed).
  - The full write-up is in `evals/ablation/RESULTS.md`.

- Card ablation, part 1 (V3a, 30 calls): `run.py --card` swaps in an ablated card, and `evals/ablation/` holds four cards, each with one group of lines removed. The new `evals/ablation_report.py` compares each against the full card on the 15-prompt V1a subset.
  - **Noise, measured from 36 repeat-sample pairs:** the standard error of a 15-prompt difference is about 1.2 points and 7 words.
  - **Results:** removing G1 (sentence-1 answer, agree only with evidence) changed the score by +0.9 and words by −7. Removing G2 (fit expertise, be concrete) changed them by +1.3 and +1. Both are inside the noise on general prompts.
  - **Pending:** G3 and G4 run next. The pruning decision will also weigh the targeted evals these rules were built from, such as C17 math and C14 invented confidence.

- **The emergency line stays (F6, 25 calls):** on 10 new stress prompts (`evals/prompts-stress2.jsonl`), sentence 1 was the next action in 10/10 answers with the plugin, against 8/10 with the card alone. Key-fact coverage was 73.8% against 75.7% (−1.9 pp). That passes the pre-stated rule (≥ 20 pp gain, ≤ 5 pp loss). Pooled over B41, F3 and F6, action-first rises from 65% to 89% at a cost of about 4 pp of coverage.
- `coverage_judge.py` gained the `--prompts`/`--keys` options for new prompt sets and a `pair` phase that compares any two conditions.

- Haiku auto-reminder end to end (B50, 15 calls): the transcripts show the line injected on turns 2–7. Turns 5–7 scored 98.7 in auto mode, against 100.0 forced on and 92.7 off. Turn 1 scored 92.0, because the SessionStart hook input has no model field, so the READMEs point Haiku users who want turn 1 covered to `BRAINRES_REMINDER=on`. `multiturn.py` gained the `--conditions` (`auto`, `off`, `reminder`) and `--tag` options.

- **The reminder returns automatically for Haiku (B48, 28 calls).** In 7-turn sessions Haiku scored 100.0 at turns 5–7 with the always-on line and 92.7 without it. The gap was present from turn 1, so the card alone is weaker on Haiku rather than drifting.
  - The hook now reads the last model from the session transcript and adds the 84-token line only for Haiku sessions, from turn 2 onward.
  - `BRAINRES_REMINDER=on` forces the line for any model, and `off` disables it.
  - `multiturn.py` uses the opt-in for its reminder condition.
  - `validate.sh` checks the routing, and both READMEs and the cost tables are updated.
  - Next: B50 (4.8), an end-to-end check of auto mode.

- Emergency-line rewrite (F5, 14 calls): the new wording, which kept every remaining step on one short line each, left stress key-fact coverage at 77%, the same as the old line. Walls of text got worse (9/10), so it was reverted per the pre-stated rule. The trade-off is documented: the line raises action-first (pooled 54% → 83%) but costs 6 pp of coverage against the card alone. F6 (2) decides keep or remove on a larger sample with a rule set in advance.

- Targeted fixes for concept and stress answers (F3, 27 calls, using the real plugin and the frozen key facts with blind marking):
  - **Dropped:** a candidate concept line did nothing (coverage 90% → 89%).
  - **Found a cost of the B41 emergency line:** stress answers covered 77% of key facts with it, against 92% for baseline. It cuts the steps after the first action, such as telling stakeholders, the post-mortem and "avoid risky repairs". F5 (3) rewrites the line.
  - `coverage_judge.py` can now mark any results folder against the suite baseline (`--treatment-dir`). F2 is superseded.

- **The bold lead-in check is narrowed (F1).** Lorch, Lorch & Klusewitz 1995 found heavy cueing no better than none, not worse, and NN/g advises front-loading bullets with scan words. brainlint now flags only sentence-length bold leads (more than 5 words on average), and the penalty drops from 6 to 4. Short bold labels are no longer penalised, and #27 is updated.
  - **Re-score, no calls:** the checks changed on 29 suite answers. The suite Brain Score gain went from +4.7 to +5.1 (CI +3.4 to +6.8). Stress went from −3.2 to −0.8, and what remains there is walls of text.
  - **Example scores moved:** 01 from 50 to 56, 02 from 41 to 39 (the bold-overuse penalty the old check had masked now applies), and 03 from 50 to 48.
  - **Updated to match:** tests, both READMEs, examples, launch drafts and the social image.

- Cross-judge check of the coverage result (F4, 9 calls): we re-marked 26 prompts with Opus using the same frozen key facts and answer order. The two judges agreed on 94% of fact marks (r = 0.82 on coverage). The direction held, but Opus measured a smaller gap: −0.6 pp, against −1.3 pp from Sonnet on the same prompts. `coverage_judge.py` gained the `--judge`, `--marks`, `--subset` and `--phase agree` options, and both READMEs mention the check.

- **Information coverage (V2, 30 calls), new `evals/coverage_judge.py`.**
  - **Method:** a Sonnet judge wrote key facts from each question alone (397 facts), which were then frozen. It marked both answers blinded and in random order.
  - **Result:** brainres covered 94.1% of key facts against 96.0% for baseline (−1.8 pp, CI −4.1 to +0.4). It covered less on 31 prompts and more on 13 (sign test p = .01).
  - **What changed is detail, not facts.** 37 facts went from full to partial coverage, against 17 the other way. Only 2 facts were dropped outright, against 3 the other way.
  - Concept and stress answers lost the most detail (−10 pp each).
  - Both READMEs now state this trade-off.
  - New items: F4 (8), an Opus cross-check, and F3 (2.5), detail loss in concept and stress.

- **Suite complete (V1f, 10 calls): 78 valid pairs across 80 prompts.** Per prompt, Brain Score rose 4.7 (CI +3.0 to +6.3), words fell 56 (−29%), visible output tokens fell 28%, and total output tokens including hidden reasoning fell 14%. This replaces the 12-prompt result as the headline in both READMEs and the Show HN, Reddit and GeekNews drafts.
- **Weakness report (V4, no calls)** from the new `evals/suite_report.py`, written to `results/suite-weakness.md`:
  - brainres was ahead in 14 of 16 types and behind in stress (−3.2) and debugging (−2.5).
  - No check fired more often with brainres.
  - Hidden reasoning rose about 100 tokens per answer.
  - New items: F1 (2.5) checks whether the bold-lead-in penalty that drives the stress losses is evidence-based, and F2 (2) tests stress prompts with the plugin's emergency line. V3 now also tracks thinking tokens.

- Suite chunk V1e (30 calls), now 73 valid pairs over 75 of 80 prompts. Per prompt, Brain Score rose 4.6 (CI +2.8 to +6.3), words fell 55 (−28%) and visible tokens fell 187 (−28%). Long sentences went from 10 to 2 and fragmented reasoning from 7 to 0. Stress prompts remain the weak category: brainres was lower on 2 of 5 and tied on 3.

- Suite chunk V1d (30 calls), now 58 valid pairs over 60 of 80 prompts. Per prompt, Brain Score rose 4.9 (CI +2.9 to +7.0), words fell 56 (−30%) and visible tokens fell 192 (−29%). One more answer was excluded as tool markup. Stress prompts emerge as the weak category: brainres was lower on 2 of 4 and tied on 2, with bold lead-ins and walls of text in step lists.

- Suite chunk V1c (30 calls), now 44 valid pairs over 45 of 80 prompts. Brain Score rose 4.2 per prompt (CI +1.8 to +6.6), the first significant result on the suite. Words fell 54 (−28%) and visible tokens fell 178 (−29%). Bold lead-ins fell from 13/44 to 8/45 and bold overuse from 12 to 4. New `evals/suite_next.py` picks the next unrun prompts and prints a running report.

- Suite chunk V1b (30 calls), now 29 valid pairs over 30 of 80 prompts. Per prompt, words fell 57 (−27%, CI −85 to −29) and visible tokens fell 162 (−28%). Brain Score rose 2.7 (CI −0.3 to +5.7). Bold lead-ins are about as common with brainres as without (6/30 vs 7/29), but bold overuse fell from 7 to 2. That is the first candidate for V4.

- **New direction (owner, 2026-11-13): measure outputs, verify and prune.** `LOOP.md` now ranks suite runs, an information-coverage check, a per-category weakness report and pruning ahead of new research. Research rounds run only when the measurements give nothing new.
- **New 80-prompt suite** (`evals/suite.jsonl`): 16 answer types × 5, 32 of them in Korean. `validate.sh` checks its shape.
- **Chunk V1a** (30 calls): across 14 valid pairs, words fell 54 per prompt (95% CI −105 to −3), visible tokens fell 146, and Brain Score rose 4.2 (CI includes 0).
- **Tool-markup answers are now excluded.** `run.py` flags answers that are raw tool-call markup (`tool_markup`), and `combine.py` drops them.
- **Backlog:** V1 (16) adds 5 more chunks, V4 (10) is the weakness report, V2 (6.7) is the information-coverage judge, and V3 (1.7) is card ablation. B49 is superseded by V1.

- Research round 8, a deeper pass on risk and numeracy (`research/catalog-round8.md`). It was nearly all covered already. From Zipkin 2014 (a 91-study review) numbers.md gains two rules: never give an effect only as a number needed to treat (RN-01, mixed evidence), and keep one format and one denominator because frequencies and percentages tested about equal (RN-02). Coverage is 659/659 (801 reviewed).
- New backlog: B49 (score 8) refreshes the README headline numbers, which were measured before the C19 card change and the reminder cut. B48 (score 2) checks the reminder cut on Haiku.

- Long-context drift check (B47, 26 calls): `evals/multiturn.py --long` pasted about 3k tokens of logs or code per turn, building sessions of about 30k tokens. Late-turn answers scored 100.0, against 98.0 for the same questions in fresh sessions, so there was no drift and no periodic reminder was added.
- **brainlint false positives fixed:** the question-aware recommendation check now accepts a premise-correcting "Neither…, because…" and Korean "더 나은 선택이에요" / "낫습니다", with tests.

- **Cut the always-on per-turn reminder (B46), saving 84 tokens on every message.**
  - **Test:** `evals/multiturn.py` ran 7-turn sessions with the real plugin (EN and KO conversations, 28 calls). Turns 5–7 scored 98.7 without the reminder and 97.0 with it, so there was no drift. The transcripts confirm the card loads once per session.
  - **Hook:** it now emits nothing unless a learner or emergency signal appears, and both of those lines were measured to work.
  - **Eval proxy:** `run.py`'s card proxy is now the card alone.
  - **Docs:** the READMEs, Reddit draft and validation checks are updated. A 20-message session costs about 500 extra tokens instead of about 2,200.
  - **Untested:** long sessions with large tool outputs; B47 (score 3) covers them.

- At the owner's request, removed the "built by a 20-min Claude loop" badge and the loop section from both READMEs, and the loop lines from the Show HN, X and GeekNews drafts. LOOP.md and LOOP_LOG.md stay in the repo.

- Research round 7 (`research/catalog-round7.md`): we found no controlled study of how streaming changes comprehension or trust in LLM answers, and recorded that as the main finding. ST-01, a practitioner report that readers act on partly streamed text, now backs the C17 rule in numbers.md. Three system-level studies (pacing, response delay, multiple answers) are catalogued and excluded.
- `llm-side-effects.md`: added two LLM-side studies, Li 2024 (instructions drift within about 8 rounds) and Laban 2025 (multi-turn performance −39%).
- The COGA and dyslexia queue item was already covered.
- Coverage is 657/657 (799 reviewed).
- New B46 (score 5) tests whether the 84-token per-turn reminder actually prevents drift on Claude. It has never been measured.

- Haiku language flip (C20, 20 calls): the Korean SQL prompt that had come back in English stayed Korean in 10/10 runs with the current card, so there was nothing to fix. A "Reply in the user's language" first line on the card also scored 0/10, so the card change was reverted per the pre-stated rule. The residual risk is about 1 in 12 runs on that prompt.

- Agentic re-run with the test runner allowed (B44, 12 runs): `evals/agentic.py --allow-tests` auto-approves only `python -m unittest`. Both conditions passed 6/6, and every final message opened with the test result it actually saw. Notes on what the tests don't cover appeared in 3/6 baseline vs 2/6 plugin messages, so the 0/6 vs 2/6 gap seen in B43 was noise. On final messages the plugin is at parity with default Claude Code.

- Card side effects on Haiku (C19, 30 calls):
  - **Reverted:** a "reply in the user's language" line in the per-turn reminder had no effect. The same code-heavy Korean SQL prompt still came back in English (0/8 before, 1/8 after), so that case moves to C20 (1.8).
  - **Kept:** card rule 1 now reads "*Only* a yes/no question starts with "Yes"/"No"". Yes/No openers on non-yes/no questions were 3 of 173 card answers across saved runs, and 1/12 before vs 0/12 after this change. That is too few to prove an effect, so it is recorded as a zero-cost precision fix.
  - The card stays at 1,349 bytes and is now 500 tokens (measured, was 498). The READMEs, launch drafts and social image are updated.

- Haiku ceiling audit (B45, 24 calls): summary-first code explanations (8/8 vs 8/8) and the recommend-plus-alternative decision shape (4/4 vs 4/4) are at ceiling on Haiku too. Both READMEs now say these are default Claude behaviour, not brainres effects. On these prompts brainres made answers 20% (explanations) to 38% (decisions) shorter.
- **Found C19 (score 9):** with the card, Haiku answered 1 of 16 Korean prompts in English, against 0 of 99 on Sonnet. It also opened one non-yes/no answer with "Yes,".

- Decision answers without the skill (B42, no new calls): we re-read 16 saved Sonnet answers to the 4 decision prompts. A recommendation in sentence 1 and "when the other option wins" both appear in every answer under baseline, card and plugin, a ceiling result, so no decision line was added. New B45 (2.5) checks on Haiku whether the rules that hit a ceiling on Sonnet (B37, B42, B43) describe default behaviour.

- Agentic final-message check (B43, no new calls): we re-read the 12 B32 final messages. All 12 already state what changed, what wasn't done and how to verify, in both conditions. That is a ceiling result, and it is confounded: the harness disallows Bash, so every run had to say it couldn't run the tests. Plugin messages more often named a limit the tests don't cover (2/6 vs 0/6, n too small to count). No end-of-task line was added. New B44 (2.4) re-runs with only test commands allowed. The first commit, 76a3401, held only the judgments; the docs followed in the next commit.

- Research round 6, a deeper pass on plain language (`research/catalog-round6.md`). Most of it was already covered, by #18 (personalization), HC-88 (plain language for experts) and #57 (nominalizations). #18 now carries verified effect sizes: retention d = 0.30, transfer d = 0.54, no reliable effect beyond 35 minutes. Two findings are new: PN-01, the politeness effect in tutoring (mixed evidence, added to learn.md as "correct collaboratively but plainly"), and PN-02, Trudeau 2012 (supports HC-88). Coverage is 656/656 (795 reviewed). New backlog: B43 (agentic final-message check, 4) and B42 (decision answers without the skill, 2.5). Both re-read existing outputs, so they cost no new calls.

- Emergency situation line (B41): the reminder hook now also adds "Emergency: the single next action first; if the habitual move is harmful, say so up top; ≤5 steps, then why" when a prompt shows a stress or emergency signal (urgent, outage, "by accident", DROP TABLE, 급해, 망했, 날아갔, 실수로…).
  - Measured with the real plugin, off vs on, 16 calls: answers whose sentence 1 is the next action rose from 3/8 to 6/8, and answers flagging a harmful habitual move before the steps rose from 4/8 to 6/8.
  - One loss: on DROP TABLE, the up-top write warning fell from 2/2 to 0/2.
  - The line fired on 1 mild case among 52 other prompts. `validate.sh` checks the routing.

- Situation-aware reminder (B40): `hooks/brainres-reminder.sh` now reads the prompt and adds one targeted line, about 20 tokens, only when it sees a learner signal ("I'm learning", "beginner", "homework", 공부 중, 배우는 중, 과제…). It ignores `cwd`, and `BRAINRES_SITUATIONS=off` disables it.
  - **Learner line kept.** With the real plugin, answers ending in a predict-first question went from 0/8 to 8/8, and fixes made on the user's own line went from 6/8 to 8/8. Answers got 22% longer.
  - **Math/trace line dropped.** It made no difference, with sentence 1 correct in 6/6 answers with and without it. C18 is closed because it did not recur.
  - The regex fired on none of the 52 other eval prompts, and `validate.sh` checks the routing.
  - The hook no longer blocks when run from a terminal, and `run.py` passes `/dev/null` to it.
  - 29 calls.

- Tried and reverted (B39): learner triggers in the skill description raised skill invocation on learner prompts only from 0/8 to 1/8, with 0/12 false triggers on general prompts. Even when the skill was loaded, the answer still rewrote the user's code and asked no self-test question, so the change bought nothing for about 40 always-loaded tokens. 20 calls. Next is B40 (score 6), a situation-aware reminder hook that adds one targeted line only when the prompt shows a learner, stress or calculation signal.

- Learner eval (B38): 4 broken-code prompts from self-described learners, run under baseline, card and plugin with 2 samples each, 24 calls, judged by hand.
  - All three conditions fixed the user's own line in 6 of 8 answers.
  - brainres answers ended with a concrete run-it check in 7/8 (card) and 8/8 (plugin), against 0/8 for the baseline.
  - No condition asked a real self-test question.
  - **The skill was invoked in 0 of 8 plugin runs,** so the learner rules in `learn.md` never apply in practice. B39 adds learner triggers to the skill description.
  - **New failure (C18):** a card answer stated the wrong program output in sentence 1 and corrected it later.

- Code-explanation eval (B37): 6 prompts × 2 samples × 2 conditions on Sonnet, 24 calls, judged by hand.
  - Sentence 1 was a purpose summary in 8/8 answers in both conditions, a ceiling result, so the card needs no change. brainres explanations were 18% shorter.
  - Assumptions stated before the code: brainres 2/2, baseline 0/2. That is too small to count as evidence.
  - Found a harness limit: in tool-less runs, a "write me a script" prompt makes the model act as if it created a file. That prompt is excluded.
  - Also found a harness bug: one failed call crashed the whole run. `evals/run.py` now records failed calls in `summary.json` and keeps going.

- Research round 5, on how people use LLM coding help (`research/catalog-round5.md`): 7 studies, 6 applied. MacNeil 2023 found students preferred summary explanations and rated line-by-line least useful; Kazemitabaar 2024 (CodeAid, 700 students); Prather 2024 (the widening gap); Nam 2024 (in-IDE explanations); Vaithilingam 2022; Liang 2024. New code rules: state unstated assumptions in one line above the code, and after non-trivial generated code name the 1–2 lines most likely to need changing. New learn rule: mark the fix on the learner's own code instead of rewriting it. Coverage is 654/654 (793 reviewed). New backlog: B37 (code-explanation eval, 9.6) and B38 (learner check, 1.5).

- Study 2, part 2 of 2 (B36b, launch prep):
  - **Page:** `bench/study2/index.html` reuses the study-1 engine, now generalized to take versions, content groups and an optional preference step. It balances 2 trials per content × format cell for each participant, and a headless autotest in validate.sh checks that.
  - **Analysis:** `analyze.py` gained a study-2 analysis (H1 interaction, H2 search time plus accuracy non-inferiority) and a report section. Study 1 analysis now ignores study-2 submissions.
  - **Independent item review (amendment v1.2, before any data):** a reviewer agent flagged 4 of 8 items. Two bullet versions were missing facts, and some questions leaked wording or had giveaway answers. All were fixed and the manifest re-hashed. Q1 time is now measured to the final option pick (`pick_ms`) rather than to the button, and parallel prose was trimmed toward bullet length so H2 tests format more than word count.
  - **Sample size (protocol amendment v1.1, before any data):** a power simulation raised the target from n = 80 to n = 150. At n = 80 the power was 0.61 for a 15 pp effect; at n = 150 it is 0.89. A 10 pp effect is still underpowered (0.57), and the protocol says so.

- Study 2, part 1 of 2 (B36a): `bench/study2/PROTOCOL.md` pre-registers a 2×2 within-subject test of rule 5, crossing content (causal vs parallel) with format (prose vs bullets). Hypotheses: H1, prose helps understanding for causal content only; H2, bullets speed up finding in parallel content. The protocol includes a decision rule and an analysis plan. Eight topics are written in both formats with identical claims, plus find and understand quizzes, frozen in `items/MANIFEST.sha256`. B36b covers the independent review, the power simulation, the page and the analysis.

- Premature-number fix (C17): card rule 1 now reads "For math, sentence 1 = the one-line calculation + result", and SKILL.md and numbers.md match. Across 3 calculation prompts × 3 samples, sentence 1 was right in 9 of 9 answers, against 0 of 3 with "do any math first" and 0 of 1 with the original card. The baseline was unstable on the same prompt (wrong in 4/4 earlier, right in 3/3 now), so we don't claim it beats the baseline. The card grew from 488 to 498 tokens (measured), and the READMEs, launch drafts and social image are updated.

- Korean eval set (B34): 12 Korean prompts via `evals/run.py --prompts prompts-ko.jsonl` (24 calls). Per prompt, words fell 30 (−20%, 95% CI −52 to −8) and visible output tokens fell 18%. Answers mixing speech levels dropped from 7/12 to 1/12. The Brain Score gain, +2.7, has a CI that includes 0.
- **Failure found (C17):** on a savings calculation, both conditions stated a wrong number in sentence 1 ("8년 4개월") and corrected it later, in 9 of 9 answers. A card change ("do any math first, never state an unchecked number", which keeps the card at 1,348 bytes) did not help, with 3 of 3 still wrong. SKILL.md and numbers.md now carry the guidance. C17 tests the alternative, putting the calculation inside sentence 1.

- Research round 4, on Korean readability (`research/catalog-round4.md`): 5 findings, 4 of them applied in korean.md. The key gap: no Korean experiment manipulates sentence length in 어절, so our thresholds (an average of ≤12, flagged above 20) are now labelled engineering defaults. New Korean rules: fix rare 한자어 and long sentences together, and break long compound-noun chains. Coverage is 648/648 (786 reviewed). New backlog: B34 (Korean eval set), B36 (benchmark study 2: bullets vs prose), B35 (scheduled re-scan).

- Agentic coding check (B32): `evals/agentic.py` runs 6 small failing-test tasks through Claude Code on Sonnet (Read/Edit/Write/Glob/Grep, no Bash), with and without the plugin. The harness runs the tests itself. Both conditions passed 6/6, modified 0 test files, and changed a median of 7 lines. The final report was about the same length (93 vs 88 words), unlike the 27% cut on chat answers. Coding outcomes are unchanged.

- Accuracy-cost eval, part 2 (B33b): 15 harder problems on Haiku (`evals/hard15.jsonl`, 30 calls) scored 15/15 in both conditions, with hard items checked by hand. Across all 48 trap and multi-step problems the score is 48/48 with and without brainres, so no accuracy cost is detectable (a ceiling result). The "brevity applies to the final answer" card line was not added, since there is no evidence it's needed. Both READMEs gain an accuracy line.

- Accuracy-cost eval, part 1 (B33a): 15 multi-step word problems on Haiku, with answers computed in Python, 30 calls. Both conditions scored 15/15, so no accuracy cost was observed, but that is a ceiling result. One brainres explanation contained a slip ("Seoul is 9 hours ahead of UTC-8") alongside a correct final answer. `tricky.py` gains a first-sentence-or-last-lines check for multi-step sets. B33b is rescoped to harder problems.

- Research round on LLM-side risk (`research/llm-side-effects.md`). Strict format restrictions degrade LLM reasoning (Tam 2024), and "be concise" prompts trade accuracy for length (Lee 2025). Our evals have shown no accuracy loss on 18 single-step traps, and on Opus brainres moved effort into hidden reasoning. Multi-step problems are untested. New backlog: B33a/B33b (accuracy cost on 30 multi-step problems) and B32 (agentic coding check).

- C16: the refutation rules (SKILL.md, correction.md) now apply only to misconceptions the user stated or implied, and never to opening by knocking down an answer nobody proposed (#52). A new `brainlint --question` check, `preemptive_refutation`, flags sentence-1 openings like "X is wrong." / "X는 틀렸어요" when X isn't in the question. It catches the real Haiku answer from B31b and produces no false positives on the 12 example files. 1 new test.

- B31b: 10 harder prompts on Haiku, covering dates, letter counts, multiplication, Python aliasing, JS sort, pricing and leap years (20 calls). Checked by hand, Haiku answered all 10 correctly in both conditions. After 18 trap prompts, natural errors don't occur often enough to test the LR-01 risk, which would need answers that are wrong by construction. Reasoning visibility with brainres was equal or better. One artifact surfaced: an answer pre-emptively refuted a wrong answer nobody had proposed. This is logged as C16. `tricky.py --set` selects the prompt file.

- LR-01 risk check (B31; `evals/tricky.py`, 8 trap questions on Haiku, 16 calls). The result is inconclusive because both conditions answered all 8 correctly, so the "wrong answer" case never occurred. No hidden reasoning was observed: brainres attached a reason within the first 2 sentences in 4 of 8 answers, against 2 of 8 for the baseline. Tooling lessons: a whole-text regex misjudged correct answers, so correctness is now judged from sentence 1 and was verified by hand. Prompt t8 was contradictory. B31b follows with harder prompts.

- **Process fix.** Commit `a139844` was pushed while `validate.sh` failed on a stale README badge. Validation had been piped into `grep`, which hid its exit status. The English README measurement list was split, bringing its score from 94 back to 100. LOOP.md now says to judge validation by exit status. `scripts/install-hooks.sh` offers an optional pre-commit hook for the owner; the loop doesn't install it.

- Opus token puzzle resolved (B28c; 24 calls, with the thinking/visible split). With brainres, Opus writes less and thinks more. Visible output tokens fell by 308 per prompt (−36%, 95% CI −472 to −144). Hidden reasoning rose by 253 (about 2.6×, borderline CI), so total output is about flat. Pooled over both Opus runs: words −80 (−35%) and Brain Score +3.3 (not significant). The READMEs now say plainly that the bill doesn't shrink on Opus.

- Real-plugin eval (B29): `evals/run.py --conditions plugin` installs the plugin via `--plugin-dir`, with the Skill and Read tools available, and records turns. We ran 12 prompts × 2 against baseline: words −54 per prompt (95% CI −82 to −27) and Brain Score +5.0 (CI +0.0 to +10.0). Both match the card-append proxy (−54, +5.3), so the proxy is validated. The skill was auto-invoked in only 1 of 24 answers (the emergency prompt), so the effect comes from the always-on hooks. `combine.py --treatment` compares any condition.

- Generalization to Opus (B28b; 24 calls): per prompt, words −79 (−34%, 95% CI −117 to −41) and Brain Score +2.9 (CI −1.5 to +7.3, not significant). `output_tokens` rose 19% (CI includes 0) because they include hidden reasoning; one probe showed `thinkingTokens` in `modelUsage`. `run.py` now records `thinking_tokens` and `visible_output_tokens`, and `combine.py` reports visible tokens when available. B28c re-runs Opus with the split.

- Generalization to Haiku (B28a; 24 calls, 12 prompts × 2 conditions): per prompt, words −71 (−35%, 95% CI −114 to −28), Brain Score +3.9 (CI +0.1 to +7.7), output tokens −14% (CI includes 0), and 0 invented confidence numbers. `--question` caught one real slip, an answer that framed before recommending. Opus follows in B28b.

- `brainlint --question` (B27) adds question-aware checks. `yesno_not_first` fires when a yes/no question, including tag questions like "…, right?", doesn't get Yes or No as the first word. `no_recommendation` fires when sentence 1 of a choice question neither names an option nor recommends one. This closes the blind spot documented in `examples/README.md`: 04 "before" now scores 70 and 02 "before" 33, while every "after" stays at 100. Scores without `--question` are unchanged, and the goldens hold. Evals record `score_q` separately, and the playground has an optional question field. 9 new tests bring the total to 43.

- Research round 3 (the backlog was empty). `research/catalog-round3.md` adds 6 findings on how people read LLM answers. One applies as a new rule: when an answer might be wrong, keep the key reasoning visible, because medium-length explanations helped people catch LLM errors (Friedman 2026, LR-01). Another sets an outline-first approach for long deliverables (LR-05). Four are excluded with reasons, including one search-summary claim that the abstract didn't support. The gap is confirmed: no study yet compares bullets and prose for comprehension of chatbot answers. Coverage is 644/644 applicable findings (781 reviewed). New backlog items: B27–B31.

- Reusable GitHub Action (`action.yml`, B20): `uses: wonjangcloud9/brainres@main` scores markdown on every PR, fails below `min-score`, and writes a Brain Score table to the job summary. This repo's CI (`.github/workflows/ci.yml`) runs `validate.sh` and dogfoods the action on both READMEs (min 90). The `build_dist --check` now compares zip entries rather than bytes, so CI on Linux doesn't fail on zlib differences.
- Backlog: B23 (voice rules) is marked superseded, because `references/voice.md` already covers it.

- Research round 2 (C09, `research/catalog-round2.md`): 50 new findings on cross-cultural pragmatics, diagrams, argumentation, news structure and numeracy. Hall's high/low-context framework is excluded for weak validation. The catalog now has 775 findings reviewed, and all 642 applicable ones are applied. New rules:
  - Sentence 1 must be correct on its own (Ecker 2014, Gabielkov 2016).
  - Directness follows the user's own signals, not their nationality.
  - Korean answers keep the content direct and the ending polite, put a regret word inside the refusal sentence, state uncertainty as its own clause, and use 두괄식.
  - Numbers get a verdict and a benchmark, with at most 3 per recommendation. Use "N in 100", never "1 in X".
  - Diagrams must fit the question, have about 7 nodes or fewer, and give each arrow one meaning.
  - Every "not found" says where you looked.
- Two conflicts are resolved. CC-09 ("always add a number to Korean probability words") is reconciled with C14: the number must be grounded, or the answer says what is unverified. The "1 in 4" example in numbers.md becomes "25 in 100".

- Brain Score playground (`playground/index.html`, B21): paste text and get the score and findings in the browser. Instead of a port, it runs the real `brainlint.py` through Pyodide, so the scores can't diverge. Parity is verified: the browser and Python both give 50 with identical findings. The page is generated by `build_dist.py`. `scripts/check_playground.sh` runs as an opt-in network check, and both READMEs link the playground.

- Stress handling (C13, partial). The skill description now names emergencies and distress as triggers, so `support.md` can load. Real-plugin runs, 3 per condition: skill invoked 0/3 → 1/3, answers with ≤5 steps 2/3 → 3/3, Brain Score unchanged within noise. brainlint fixes: numbered steps no longer count as `fragmented_reasoning`, and nested items no longer inflate list length (+2 tests, 34 total). Golden scores are unchanged.

- Interplay with Claude Code's built-in output styles is now measured and documented (B24). `evals/run.py --style` sets the style, using 4 prompts with 1 sample each. With Explanatory, brainres cut words 27%, raised the Brain Score from 92.8 to 98.5, and kept all ★ Insight blocks. With Concise, brainres added 23% words (decision support) at an equal score. Both READMEs recommend Concise alone or `scan` for the shortest answers. Style runs are kept out of `combine.py`.

- Benchmark analysis (B10-4): `bench/analyze.py` is stdlib only. It reads local JSON files or `--from-issues` via `gh`, applies the pre-registered exclusions, and runs paired Wilcoxon and t-interval analyses for H1–H3, a sign test for E1, and the decision rule. 5 tests on simulated participants cover a planted effect, null data, an accuracy drop, exclusions, and an exact Wilcoxon value.
- **Protocol amendment v1.1, before any data:** the same simulation showed the 5 pp non-inferiority margin had only 28–68% power at n = 60, so it is widened to 10 pp (84–99% power). The reason and the simulation table are in PROTOCOL.md.

- Re-measured costs after C14 (`scripts/token_cost.sh`, median of 3): rule card 488 tokens, reminder 84 (was 79), skill body 3,391 (was 3,309). The README tables lose their "re-measure pending" asterisk, and a 20-message session is about 2,200 extra input tokens.

- Benchmark, step 3 of 3 (B10-3): `bench/index.html` is the participant page. It offers English or Korean, puts each participant on counterbalanced list A or B (50/50 versions, unlabeled), randomizes item and option order, and records timed find and understand questions with confidence, an attention check and 2 preference pairs. Results export as JSON. `build_dist.py` generates the page from the frozen items. `validate.sh` runs a headless-Chrome autotest through the whole study. Results are submitted through a GitHub issue form. Next: B10-4 (analysis) and B10-5 (the owner enables Pages and recruits).

- **Fixed the regression (C14):** card rule 8, SKILL rule 9 and numbers.md now forbid invented confidence percentages; numbers are allowed only when grounded (JD-33). A new `brainlint` check, `invented_confidence`, flags self-rated "~80% sure" and "(~90% 확신)" but not confidence intervals or calculations, with tests. Inline code is now treated as a quoted literal, so a README that *mentions* an anti-pattern isn't penalized for it (32 tests in total). The Korean README measurement section is split again after this change pushed it over the paragraph limit. Eval re-run: 7 of 36 answers flagged before the fix, 0 of 24 after, with length gains intact (words −54, CI −88 to −20). The card grew from 461 to 488 tokens. README, launch drafts and the social image are updated.

- Benchmark, step 2 of 3 (B10-2): 24 quiz questions, a "find" question and an "understand" question for each item, each answerable from **both** versions. An independent LLM review passed 22 and flagged 2 for fixes; both are fixed. Its finding that 9 stems or options leaned on brainres wording led to neutral rewrites. Quiz hashes are added to the pre-registration manifest.
- **Regression found (C14):** brainres answers invented confidence numbers in 6 of 36 cases ("~80% likely", "~90% 확신"), against 0 of 36 for the baseline. It is documented in `evals/README.md` and is the top backlog item.

- Human comprehension benchmark, step 1 of 3. `bench/PROTOCOL.md` pre-registers 3 hypotheses (find faster; comprehension non-inferior at a 5 pp margin; better calibration), a counterbalanced within-subject design, n=60, an analysis plan, exclusions and a decision rule. 12 answer pairs are frozen in `bench/items/`, with SHA-256 hashes in `MANIFEST.sha256`.

- `rewrite` mode gets its own procedure in `references/rewrite.md`: inventory the claims and payload, rewrite, mark each item ✓/⚠/✗, then report. This answers the meaning-loss failures of other rewrite skills (humanizer #212, CAVEWOMAN's 51.9% drift).
- `brainlint --compare original rewritten` checks mechanically for numbers, code spans, URLs and negations that a rewrite dropped, and exits 1 when anything is missing. List numbering and trailing URL punctuation are ignored. 4 new tests bring the total to 30.

- Evals final, part 3 of 3 (B09b), with 3 samples per prompt per condition (72 answers): words −27% (per prompt −54, 95% CI −89 to −20), output tokens −16% (CI −179 to −33), Brain Score 91.2 → 96.2 (+5.0, CI +0.8 to +9.2), and 29/36 → 32/36 answers within the length budget. The earlier single-sample claim (−33% words, −24% tokens) is superseded in the READMEs and launch drafts.

- Evals, part 2 of 3 (B09b): baseline now has 3 samples per prompt (n=36). Interim per-prompt result: Brain Score +4.6 (95% CI +0.4 to +8.8), words −54 (CI −89 to −20), output tokens −117 (CI −213 to −22).

- Evals, part 1 of 3 (B09b): runs now record the card hash so card versions never mix, plus a length-budget metric. `evals/combine.py` merges runs and reports SD and a paired 95% CI. Interim result per prompt: Brain Score +4.2 (CI +0.2 to +8.2), words −63 (CI −99 to −27), output tokens −165 (CI −263 to −67).

- Core card v2.1 adds a Korean line to rule 10: 해요체, ≤12 어절, no 번역투. In the eval re-run (4 Korean prompts × 2), answers with long sentences went from 2 of 4 to 0 of 8, and the mean Korean Brain Score went from 89.2 to 93.9. The card cost rose from 418 to 461 tokens (measured), and the READMEs, launch drafts and social image are updated. `evals/run.py` gains `--ids`, `--conditions`, `--samples` and `--tag`.

- First eval harness (`evals/run.py`, 12 prompts × baseline and brainres on Sonnet, tools and MCP off). Median answer length fell from 210 to 140 words (−33%), output tokens fell 24%, and the mean Brain Score rose from 91.6 to 93.5. Claude Code's baseline already had no preambles. Two regressions are documented: Korean sentence length, and brainlint's blind spot on raw length. Results are in `evals/results/`, a summary is in both READMEs, and the launch drafts now carry the measured numbers.
- brainlint ignores HTML comments, which readers never see; a test covers it. Follow-ups: C12 (a Korean line in the card) and B09b (repeated samples).

- Verification round 1 (`research/verification-2026-11.md`) checked 11 citations against primary records.
  - **Verified:** the 5 studies the README leans on most (Cheng 2026 *Science*, Ding 2025 AAAI, Ibrahim 2026 *Nature*, Kim 2024 FAccT, Steyvers 2025), plus Gopstein 2017 and Langhout & Aniche 2021.
  - **Upgraded:** Ashktorab 2019 (EM-110), read in full text, goes from W to M.
  - **Downgraded:** Hales 2017 (PL-14) is an opinion piece, not an experiment. It goes from W–M to W, and the unsupported "n=98" is removed.
  - **Flagged:** Wright & Reid 1973 and Dixon 1982 exist, but their specific results were not located.
  No rule had to be removed.

- brainlint adds 7 line-level checks from craft.md and SKILL.md: `scope_ambiguity` ("all … not"), `bare_this`, `former_latter`, `minimizer` ("simply", "just run", 간단히), `understanding_check` ("does that make sense?"), `emoji` (✓/✗ excluded because they carry meaning), and `boilerplate_warning`. There are now 25 checks in total. No example or README score changed. Trigger and non-trigger tests bring the total to 25.

- 4 new before/after pairs, for 6 in total: concept (DB index), comparison table (SQLite/Postgres/MongoDB), risk numbers (flaky-test cumulative probability, computed), and misconception (incognito). `examples/README.md` indexes them with scores, and all 12 files are pinned as golden cases (23 tests in total).
- brainlint gaps found by the new examples are fixed. "That's an interesting question" now counts as a preamble, and "…is a crucial decision that depends on many factors" now counts as a buried answer. The blind spot that remains is answers with no recommendation, which needs the question; it is documented.

- brainlint v0.2 adds 3 checks:
  - `buried_answer`: the first sentence frames instead of answering ("There are several factors…", "It depends…", "여러 가지…"). It is skipped when a preamble was already penalized.
  - `fragmented_reasoning`: more than 60% of lines are bullets and there are no causal links, in answers of at least 120 words.
  - `term_swap`: curated synonym pairs such as folder/directory and 앱/애플리케이션 appear in the same answer.
  Golden scores are unchanged. 5 new tests bring the total to 23.

- The SKILL.md body drops from 3,893 to 3,309 tokens (−15%, measured). The 35 inline evidence-ID groups moved to `references/rule-sources.md`, which maps each rule to its findings. Coverage stays at 596/596.

- `brainlint --badge <file>` prints a shields.io "Brain Score" badge, so anyone can score their README. Both READMEs carry their own scores, and `validate.sh` fails if a badge goes stale. The English README scores 100 and the Korean one 96; the 96 comes from the deliberately bad hero sentence.
- brainlint fix found while dogfooding: markdown table rows were counted as one giant paragraph. Tables are now excluded from prose checks, and a test covers it (20 tests in total).
- Korean README: the install and evidence sections are restructured into tables and short groups. They had broken our own chunking rule, at 79 → 96.
- `assets/social-preview.png` (1280×640) and its HTML source, for the GitHub social preview and launch posts.

- Opt-in output style `output-styles/brainres.md`, picked with `/output-style`. `keep-coding-instructions` is on. It is generated from the core card by `build_dist.py`, so it can't drift; the stale check covers it.

- brainlint: Korean is now measured as korean.md specifies, with an average of ≤12 어절 and a long-sentence flag above 20. Headings no longer count as sentences, and 2-word labels no longer dilute the average. The Korean "before" example now scores 41 (was 45), because its 22-어절 sentence is flagged. Scores are updated in the READMEs, examples and launch draft. 3 new tests bring the total to 18.
- Backlog tidy: B17 and B18 are marked superseded by the coverage work, and B06 is re-scoped to the scorer.

- `tests/test_brainlint.py`: 15 stdlib tests. Golden scores for the shipped examples (50 / 100 / 45 / 100), every check's trigger and non-trigger, code-block exclusion, and the JSON schema. They run from `validate.sh`. A mutation check (list threshold 5 → 6) confirmed the tests catch regressions.

- Portable builds in `dist/` from one source (`scripts/build_dist.py`, deterministic): `system-prompt.md` for any LLM (fits ChatGPT custom instructions), `AGENTS.md`, Cursor rule `cursor/brainres.mdc`, and `brainres-skill.zip` for claude.ai. `validate.sh` fails if `dist/` is stale.

- Core card v2: 11 lines chosen by RICE across all 725 findings (`research/core-card-ranking.md`); 631 → 418 tokens (−34%, measured). Situation-only rules (clarifying questions, headings, stress mode, Korean) stay in the skill. `validate.sh` caps the card at 1,350 chars.

- Measured prompt cost with Claude's tokenizer (`scripts/token_cost.sh`): rule card 631 tokens per session, reminder 79 per message, full skill 3,893 when invoked. Earlier README estimates (~450 / ~60) are corrected.

- `launch/`: drafts for Show HN, an X thread, GeekNews (Korean) and r/ClaudeAI, plus a pre-posting checklist. These are for the owner to post; the loop never posts.

- **Full-coverage program:** 6 new domain catalogs bring the total to 725 reviewed findings. All 596 applicable findings are cited by a rule (100%); 129 are excluded with a reason (not text-applicable, failed replication, neuromyth, manipulative, or duplicate).
- New rule set "Honest, not agreeable" (anti-sycophancy, premise checks, no flattery, "I'd do X because Y") in SKILL.md and the always-on card.
- 4 new reference files: `support.md` (distress, worry, emergencies), `accessibility.md` (dyslexia, ADHD, autism, aphasia, older readers, screen readers), `korean.md` (Korean output and L2 readers), `craft.md` (line-level psycholinguistics). All 9 existing references expanded.
- 19 new neuromyths documented (e.g. "23 minutes to refocus", glucose willpower, word-shape reading).

- `README.ko.md`: Korean README with a Korean before/after hero (45 → 100), linked from the English README.

- Coverage ledger (`scripts/coverage.py`, `research/coverage.md`): every catalogued finding is applied in a skill file or excluded with a reason; validate.sh ratchets the count.
- Situation router + 9 reference files (explain, decide, numbers, code, procedure, learn, correction, long-form, voice). The original catalog is at 87/87 applicable findings applied.

- Per-turn reminder hook (UserPromptSubmit, 238 chars ≈ 60 tokens) so the rules hold across long sessions. Same opt-out as the session hook.

## 0.1.0 — 2026-11-12

- Core skill `brainres`: 10 evidence-linked rules, reader-expertise adaptation, explanation patterns, payload protection, modes (scan, learn, rewrite, score, off).
- Always-on: SessionStart hook injects a ~350-token core card (opt out with `BRAINRES=off` or `~/.claude/brainres.off`).
- `brainlint` v0.1: dependency-free readability scorer for English and Korean, each check mapped to a cognitive-science finding.
- Research: 90-concept cognitive-principles catalog with evidence grades; survey of trending output-style skills.
- Two before/after examples (EN debugging, KO decision).
