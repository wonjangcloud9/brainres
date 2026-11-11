#!/usr/bin/env bash
# Injects the brainres core card at session start so it shapes every answer.
# Turn off: export BRAINRES=off   or   touch ~/.claude/brainres.off
[ "${BRAINRES:-on}" = "off" ] && exit 0
[ -f "$HOME/.claude/brainres.off" ] && exit 0
card="$(dirname "$0")/core-card.md"
[ -f "$card" ] || exit 0
python3 - "$card" <<'PY'
import json, sys
text = open(sys.argv[1], encoding="utf-8").read()
print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": text[:9500]}}))
PY
