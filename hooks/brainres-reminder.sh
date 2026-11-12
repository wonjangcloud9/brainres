#!/usr/bin/env bash
# Per-turn situation hook. Adds one targeted line only when the prompt shows a learner or
# emergency signal; otherwise it emits nothing.
# Situation lines (B40): rules that live only in skill references reach the model only
# when the skill loads (measured 1/24 general, 1/8 learner prompts), so one targeted line
# is appended only when the prompt shows that situation's signal. Learner line (B40): predict-first
# question 0/8 → 8/8, fix on their own line 6/8 → 8/8. Emergency line (B41): sentence 1 = the next
# action 3/8 → 6/8, harmful habitual move flagged before the steps 4/8 → 6/8 (plugin, Sonnet). Its cost (F3): stress
# key-fact coverage 77% vs 83% card-only. A rewrite that kept all remaining steps (F5) didn't help (77%, walls 9/10).
# Turn off: export BRAINRES=off   or   touch ~/.claude/brainres.off
# Situation lines only: export BRAINRES_SITUATIONS=off
[ "${BRAINRES:-on}" = "off" ] && exit 0
[ -f "$HOME/.claude/brainres.off" ] && exit 0
[ "${BRAINRES_REMINDER:-on}" = "off" ] && exit 0  # evals only (B46): card on, per-turn reminder off
input=""; [ -t 0 ] || input=$(cat 2>/dev/null)  # never block when run by hand from a terminal
# Match against the prompt only (not cwd or transcript paths); fall back to raw input without python3.
prompt=$(printf '%s' "$input" | python3 -c 'import sys,json; print(json.load(sys.stdin).get("prompt",""))' 2>/dev/null) || prompt=$input
# B46: the always-on base line (84 tokens/turn) was cut: 7-turn sessions showed no drift without it.
# Only situation lines remain, and nothing is emitted on turns without a signal.
extra=""
if [ "${BRAINRES_SITUATIONS:-on}" != "off" ]; then
  if printf '%s' "$prompt" | grep -qiE "i'?m (learning|new to|a beginner)|i am (learning|new to|a beginner)|beginner|newbie|homework|assignment|공부 ?중|배우는 ?중|배우고 있|초보|과제|숙제"; then
    extra="$extra Learner: fix their own line first (not a rewrite); end with one predict-first question."
  fi
  if printf '%s' "$prompt" | grep -qiE "urgent|asap|emergency|panick?ing|outage|(site|server|prod|production|app|db|database) (is|went|has been) down|by accident|accidentally|drop table|lost (all|everything|my work)|급해|급합니다|망했|큰일|날아갔|실수로|다운됐|장애"; then
    extra="$extra Emergency: the single next action first; if the habitual move is harmful, say so up top; ≤5 steps, then why."
  fi
  # A concept line ("one sentence on where it's used + one example") was tested in F3 and dropped: coverage 90% → 89%.
  # A math/trace line was tested too (B40) and dropped: sentence 1 was already right in 6/6 without it.
fi
[ -z "$extra" ] && exit 0
printf '{"hookSpecificOutput":{"hookEventName":"UserPromptSubmit","additionalContext":"%s"}}\n' "brainres (skip if the user turned it off):$extra"
