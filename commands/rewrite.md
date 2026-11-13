---
description: Rewrite a file or pasted text with the brainres rules, keeping every fact, and show the before/after score
argument-hint: "[file.md | pasted text]"
allowed-tools: Bash(python3:*), Read, Write
---

Use the brainres skill in **rewrite** mode on: $ARGUMENTS
(a file path, pasted text, or, if empty, your previous answer).

1. Score the original with `python3 "${CLAUDE_PLUGIN_ROOT}/skills/brainres/scripts/brainlint.py" <file>`. Save pasted text to a temporary `.md` first.
2. Rewrite it following `${CLAUDE_PLUGIN_ROOT}/skills/brainres/references/rewrite.md`. Keep every fact, number, code block, negation and warning exactly. Don't add claims.
3. Score the rewrite the same way.
4. Show the rewrite, then one line: `Brain Score <before> → <after> · <words before> → <words after> words`, and list any content you were unsure how to keep.

If it's a file, write the rewrite back only if the user asked; otherwise print it.
