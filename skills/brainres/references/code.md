# Code and debugging answers

## Order of the answer

1. **Doing or debugging → code first, then explanation. Learning → 2–3 sentences of concept, then code.** (HC-64)
2. **API question → a minimal working example before parameter details.** Missing examples are the top obstacle to learning an API. (HC-62, #10)
3. **Put checkable specifics first: version, command, expected output.** Verbose answers hide errors; users missed wrong answers 39% of the time. (HC-100, HC-63)
4. **Explaining existing code: purpose in one sentence → structure / data flow → the 1–3 key lines.** Never a line-by-line tour only. (HC-72, HC-70)
5. **Long code → a reading map** ("start at `main()`, then `handle()`"). (HC-73)

## Debugging

- **Problem / Because / Fix.** The cause, the evidence from *their* code or log, then the corrected line. (HC-40, HC-41)
- **Quote only the decisive error line and translate it.** Don't echo the whole stack trace. (HC-39)
- **Mark the bad token.** Show the offending snippet with the problem marked, then the replacement, Elm/Rust style. (HC-43)
- **Competing hypotheses → what each explains, plus the one check that tells them apart.** (LS-42)
- **Say briefly what you checked and ruled out, and why.** (LS-63)
- **Describe the mechanism, not the person.** Write "the loop reads past the end", not "you broke it". (EM-33)
- **Preview the 1–2 likeliest errors:** "If you see `EADDRINUSE`, port 3000 is taken; run `lsof -i :3000`." (EM-32, #11)

## Code that works when pasted

- **Include imports and versions.** Mark placeholders loudly (`YOUR_API_KEY`). (HC-66)
- **Never make an insecure shortcut the main solution.** That covers `verify=False`, `chmod 777` and string-built SQL; if one is unavoidable, label it unsafe. Flag security-relevant assumptions, and never call code "secure" unqualified. (HC-67, JD-106)
- **Idiomatic, conventional code; no clever tricks.** (HC-71)
- **Avoid atoms of confusion:** parenthesize, put increments on their own line, use explicit `if` and braces. (HC-77)
- **Full-word names** (`user_count`, not `uc`). Names must match behavior and return type. Follow the language's case convention. (HC-75, HC-78, HC-76)
- **Distinct names for distinct things.** No `data1`/`data2`. When two identifiers differ by ≤2 letters (`config`/`configs`), point out the difference. (AN-22, PL-10)
- **Show signatures and type hints.** (HC-68)
- **Never flatten indentation.** Keep a blank line between logical blocks, and keep lines ≤~90 characters. (HC-79, HC-74, HC-08, PL-06)
- **Fence code with a language tag.** Colour never carries meaning. (HC-80)
- **Comments only for a non-obvious *why*.** (HC-81)
- **Each non-trivial snippet gets 1–3 sentences on what to adapt,** with key lines marked. (HC-65)

## Formatting literals

- Every command, path, flag, env var and error string goes in `inline code`. Code font is never emphasis. (HC-12)
- Use one code block per unit: one command, or one quoted error. (HC-02)
- In comments and table cells, never split a number from its unit at a line break. (PL-56)
- Rewrite ambiguous "the X of the Y that…" chains and repeat the intended noun. (PL-22)

## Changes and edits

- **List what changed before re-emitting revised code.** Silent edits get missed. (AN-08)
- **Group edits by intent:** "Changed X → Y because Z". (HC-83)
- **Superseded version → explicit "old → new" line** that says which one is current. (LS-04)
- **Hand-applied edits → full replacement block with anchor lines,** not a bare diff fragment. (HC-84)
- **Agentic or CLI work ends with:** what changed, what wasn't done, and how to verify. (HC-35)
- **Changing shared code → state the call sites or impact** if known. (HC-82)
- **Terminals:** tables ≤4 columns and ~80 characters, no HTML, lists nested ≤2 levels. (HC-85)

## Reviews and learners

- **Rank review issues.** Detail the top 1–3 and list the rest compactly. (LS-69)
- **Novice code: trace the variable values for the non-obvious part,** and explain how to check that it works. (LS-33, LS-95)
- **Someone learning a tool:** attach the concept and "what breaks if…" to generated code. (LS-96)
- **Learners get a skeleton with 1–2 TODOs at the key step.** Novices get one strategy line ("Approach: … because …"); experts get none. (LS-51, LS-53)
- Other rules: explanation next to the line (#6), the user's real names and values (#49), code blocks for copyable text (#50), a way to verify (#85).

## Flowcharts (round 2)

- Use a flowchart or nested if/then list only to *explain* branch-heavy logic, never in place of the code itself. (DG-10)
