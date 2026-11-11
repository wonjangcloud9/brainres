# Rewrite mode: restructure without losing meaning

Rewrites that optimize style can quietly delete claims. Two cases from our survey:

- humanizer turned "the single most important" into "the important", and later added a lost-claim check.
- Compressed LLM output changed meaning in 51.9% of answers (CAVEWOMAN).

Readers don't notice: a near-miss version reads as correct (PL-24), and missing qualifiers go unseen (PL-04). So every rewrite follows these four steps.

## 1. Inventory first

Before changing anything, list the original's payload as numbered lines:

- **Claims:** one line each, including conditions ("only if…", "unless…").
- **Numbers, units, versions, dates.**
- **Code, commands, paths, flags, URLs, error text.**
- **Negations and limiters:** not, never, only, except, without, 않, 없.
- **Warnings and their order relative to steps.**

## 2. Rewrite

Apply the 10 rules and [craft.md](craft.md), along with the situation file that fits (procedure, decide, numbers…).

- Restructure: answer first, chunk to 4, prose for reasoning, warnings before their step. (#28, #1, #36, HC-50)
- Shorten by cutting repetition and filler, not qualifiers or logic. Mechanical shortening doesn't improve comprehension. (HC-90)
- If you merge or recap points, keep every critical one. A partial recap suppresses the rest. (LS-15)

## 3. Lost-claim check

Mark every inventory line in the rewrite:

| Mark | Meaning | What to do |
|---|---|---|
| ✓ | kept, same meaning | nothing |
| ⚠ | kept, but meaning shifted (scope, certainty, order) | fix it, or tell the user |
| ✗ | dropped | allowed only for exact duplicates or content the user asked to cut. Say so |

Negations, numbers, conditions and warnings are never dropped silently. (PL-04, PL-25)

If the files are available, run the mechanical check as well:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/brainlint.py --compare original.md rewritten.md
```

It lists numbers, code spans, URLs and negations that disappeared, and exits 1 when anything did.

## 4. Report

Give the rewritten text first, then one line of changes:

> Kept 12/12 claims; cut 2 duplicate sentences; moved the backup warning before step 3; ⚠ "usually" became "always" in step 5. Fixed.

Report any ✗ or ⚠ explicitly. Never claim "nothing was lost" without doing step 3.
