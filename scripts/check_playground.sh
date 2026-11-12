#!/usr/bin/env bash
# Parity check: the browser playground (Pyodide) must give the same score as brainlint.py.
# Needs network (downloads Pyodide). validate.sh runs it only when BRAINRES_NET_CHECKS=1.
set -euo pipefail
cd "$(dirname "$0")/.."
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
web=$("$CHROME" --headless=new --disable-gpu --virtual-time-budget=60000 --dump-dom "file://$PWD/playground/index.html#autotest" 2>/dev/null \
      | grep -oE 'id="scoreval">[0-9]+' | grep -oE '[0-9]+$')
py=$(PYTHONDONTWRITEBYTECODE=1 python3 skills/brainres/scripts/brainlint.py --json examples/01-react-rerender/before.md \
     | python3 -c "import json,sys; print(json.load(sys.stdin)['score'])")
[ "$web" = "$py" ] && echo "playground parity OK ($web = $py)" || { echo "playground parity FAILED (web=$web py=$py)"; exit 1; }
