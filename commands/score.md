---
description: Score a file (or your last answer) with brainlint, the brainres readability checker
argument-hint: "[file.md] [--question \"the question\"]"
allowed-tools: Bash(python3:*), Write
---

Score readability with brainlint, which ships with the brainres plugin.

- If `$ARGUMENTS` names a file, run:
  `python3 "${CLAUDE_PLUGIN_ROOT}/skills/brainres/scripts/brainlint.py" $ARGUMENTS`
- If `$ARGUMENTS` is empty, write your previous answer in this conversation, verbatim, to a temporary `.md` file and run the same command on that file.

Then reply with the score line, then the top 3 findings, each with the one-line fix it suggests. Don't rewrite anything unless the user asks.
