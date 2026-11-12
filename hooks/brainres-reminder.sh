#!/usr/bin/env bash
# Per-turn micro-reminder. Instructions decay over long sessions; a short
# re-injection each turn keeps the rules active (~60 tokens per turn).
# Turn off: export BRAINRES=off   or   touch ~/.claude/brainres.off
[ "${BRAINRES:-on}" = "off" ] && exit 0
[ -f "$HOME/.claude/brainres.off" ] && exit 0
cat <<'JSON'
{"hookSpecificOutput":{"hookEventName":"UserPromptSubmit","additionalContext":"brainres (skip if the user turned it off): answer in sentence 1 · ≤4 items per group · prose for reasoning · concrete, their values · uncertainty once, numbers only if grounded · agree only with evidence · fit their expertise · end on the next action."}}
JSON
