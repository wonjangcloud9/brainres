#!/usr/bin/env bash
# Measure brainres's real prompt cost with Claude's own tokenizer.
# Method: send the same tiny prompt with a 1-character appended system prompt
# (control) and with each brainres text appended instead. Both calls pay the same
# fixed overhead for --append-system-prompt, so the difference is the text's cost.
# Each measurement is repeated (REPS, default 3) and the median kept.
# Requires the Claude Code CLI; uses 4×REPS headless calls.
set -euo pipefail
cd "$(dirname "$0")/.."
MODEL=${MODEL:-sonnet}

total_input() {
  # $1 = text to append to the system prompt ("" for baseline)
  # MCP servers are disabled: their tool lists load asynchronously and make the
  # baseline jump by thousands of tokens between runs.
  local args=(-p "Reply with exactly: OK" --model "$MODEL" --output-format json
              --strict-mcp-config --mcp-config '{"mcpServers":{}}')
  args+=(--append-system-prompt "$1")
  claude "${args[@]}" < /dev/null | python3 -c "
import json,sys
u=json.load(sys.stdin)['usage']
print(u.get('input_tokens',0)+u.get('cache_creation_input_tokens',0)+u.get('cache_read_input_tokens',0))"
}

reminder=$(bash hooks/brainres-reminder.sh | python3 -c "import json,sys; print(json.load(sys.stdin)['hookSpecificOutput']['additionalContext'])")
skill_body=$(awk 'NR==1{next} /^---$/ && !d{d=1; next} d' skills/brainres/SKILL.md)

REPS=${REPS:-3}
median() { python3 -c "import statistics,sys; print(int(statistics.median(map(int,sys.argv[1:]))))" "$@"; }
measure() { local vals=(); for _ in $(seq "$REPS"); do vals+=("$(total_input "$1")"); done; median "${vals[@]}"; }

base=$(measure ".")
card=$(( $(measure "$(cat hooks/core-card.md)") - base ))
rem=$(( $(measure "$reminder") - base ))
skill=$(( $(measure "$skill_body") - base ))

echo "model=$MODEL baseline_input=$base"
echo "core_card_tokens=$card        # once per session (SessionStart hook)"
echo "reminder_tokens=$rem          # every user turn (UserPromptSubmit hook)"
echo "skill_body_tokens=$skill      # only when the skill is invoked"
