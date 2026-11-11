# Landscape: skills that change how LLMs write (survey 2026-11-12)

Star counts read from GitHub on 2026-11-12. "Claimed" = author's number, not independently checked.

## Terse / token-reduction family

| Repo | Stars | Core rules | Measured |
|---|---|---|---|
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | ~119k | Answer first `[thing] [action] [reason]. [next step]`; no greeting/recap/closer; ≤20-word sentences, active voice, one term per thing (from ASD-STE100); never drop `not/never/only/except`; code & numbers verbatim; full prose for security warnings, irreversible actions, confused users | Claimed −65% output tokens. Own table: only ~5% better than "Answer concisely.". JetBrains: −8.5% tokens, quality unchanged. Adobe CAVEWOMAN paper: 51.9% of compressed answers drift in meaning; **no human readers tested** |
| [drona23/claude-token-efficient](https://github.com/drona23/claude-token-efficient) | ~6.2k | Concise, no preamble/closer, "user instructions always win" | Claimed −63% words; own rerun −4–12% |
| [lowenbjer/claude-terse](https://github.com/lowenbjer/claude-terse) | 54 | Fixed shape: 1 answer sentence → list/table → ≤1 caveat → stop; UserPromptSubmit hook re-injects 576-char reminder **every turn** | −45% output tokens; style violations 11.1→1.1 per 1k words |
| [hexiecs/talk-normal](https://github.com/hexiecs/talk-normal) | ~1.9k | Bans "not X but Y", closing stamps, conditional menus; BAD/GOOD few-shot | −72% chars; regression log per rule |
| Claude Code built-in **Concise** output style | official | First sentence = result; simple Q → 1–3 sentences; full length for errors, security, destructive ops | — |

## Humanizer / anti-slop family

| Repo | Stars | Core rules | Measured |
|---|---|---|---|
| [blader/humanizer](https://github.com/blader/humanizer) | ~67.8k | 26 patterns from [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing): staging ("not X but Y"), forced triads, inflation words (delve, pivotal, tapestry), decorative bold/headings, chatbot residue; §26 "lead with the decision"; "weak alone" tells count only in clusters; voice sample outranks rules; v3 adds a lost-claim check | LLM-judge-only preference; issue #212: rewrites deleted meaning |
| [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | ~18.9k | 8 rules (cut filler, active voice, specific, "trust readers", cut quotables); self-score 5 dims ≥35/50 | none; over-broad bans (all adverbs, all passive) |
| [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | ~5.6k | rewrite/detect/edit modes; separates AI-frequency tells from genuine clarity fixes; CLI + GitHub Action + MCP | none |
| tropes.fyi | site | 49 tropes; negative parallelism = #1 tell | — |
| [obra/the-elements-of-style](https://github.com/obra/the-elements-of-style) | 624 | Strunk 1918, loaded only for prose | none |

## Adjacent

- [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) (~60.9k, HN 542 pts): 10 rules — lead with next action, number steps, end with one next step, suppress tangents, restate state, concrete time estimates, visible wins, matter-of-fact errors, **cap lists at 5**, no preamble/recap. Only big repo citing a clinical source. HN critique: rules decay over long sessions.
- fcakyon/claude-codex-settings `adhd-output-style`: shipped as a real output style.
- ELI5 skills (5 levels), plain-language-design (reports reading level), cognitive-load-reviewer (4-chunk budget — for code review, not answers).

## What works (adopt)

1. Answer first; no preamble/recap/closer. One line gets most of the gain — don't oversell compression.
2. Protect the payload: code, numbers, errors verbatim; never drop negations/limiters.
3. Exceptions: full prose for safety warnings, irreversible actions, confused readers.
4. Concrete banned-pattern lists beat "sound human"; cluster-based detection.
5. Lost-claim check after any rewrite.
6. Numbered steps + one concrete next action at the end.
7. Re-inject rules every turn (hooks) — instructions decay over long sessions.

## Gaps nobody covers (brainres's opening)

1. **No one measures human comprehension.** Every eval counts tokens or uses LLM judges.
2. **No reader model** — nothing adapts to expertise (expertise reversal effect).
3. Working memory reduced to "cap lists at 5": no chunk labels, no define-before-use, no term consistency.
4. Compression meaning-drift never checked against readers.
5. Hedges deleted, not **calibrated**.
6. **Skimming ignored**: front-loaded paragraphs, scannable first lines.
7. Anti-slop targets "not sounding like AI", not the reader.
8. No concrete-before-abstract, worked examples, analogies.
9. Little for non-native readers / non-English (e.g. Korean translationese).

## Virality patterns to copy

1. Memorable name + one-line tagline in voice.
2. Before/after demo on the first screen, with numbers.
3. Short numbered rule list that fits one screenshot.
4. Borrowed authority — cite the actual cognitive-science papers.
5. One-line install everywhere; translations; author engages on HN.
6. A benchmark others can rerun, with honest limits (hype numbers get debunked; honesty is the moat).
