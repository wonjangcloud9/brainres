#!/usr/bin/env bash
# D4: end-to-end install check from GitHub in an isolated Claude Code config (never touches ~/.claude).
# Installs brainres@brainres via the public marketplace, runs the installed hooks, and starts one session
# to confirm the SessionStart card lands in the transcript. That session needs no login: the hook fires
# before any API call. Network required; opt in from validate.sh with BRAINRES_NET_CHECKS=1.
set -euo pipefail
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
export CLAUDE_CONFIG_DIR="$tmp/config"
claude plugin install brainres --marketplace wonjangcloud9/brainres --json > "$tmp/install.json"
grep -q '"outcome":"ok"' "$tmp/install.json" || { cat "$tmp/install.json"; exit 1; }
root=$(claude plugin list --json | python3 -c "import json,sys; print([p for p in json.load(sys.stdin) if p['id']=='brainres@brainres'][0]['installPath'])")
CLAUDE_PLUGIN_ROOT="$root" bash "$root/hooks/brainres-context.sh" | grep -q "brainres is active"
printf '{"prompt":"I am learning Python"}' | bash "$root/hooks/brainres-reminder.sh" | grep -q "Learner:"
mkdir -p "$tmp/work" && (cd "$tmp/work" && claude -p "Reply with exactly: OK" --output-format json --strict-mcp-config --mcp-config '{"mcpServers":{}}' < /dev/null > /dev/null 2>&1 || true)
grep -rq "brainres is active" "$CLAUDE_CONFIG_DIR/projects" || { echo "card not injected in a fresh session"; exit 1; }
echo "install from GitHub ok · hooks ok · card injected in a fresh session ($(du -sh "$root" | cut -f1) installed)"
