#!/usr/bin/env bash
# OPTIONAL (owner's choice): install a git pre-commit hook that blocks commits when validate.sh fails.
# Not installed automatically. Run it yourself if you want local enforcement: bash scripts/install-hooks.sh
set -euo pipefail
cd "$(dirname "$0")/.."
cat > .git/hooks/pre-commit <<'HOOK'
#!/usr/bin/env bash
# brainres: refuse to commit if validation fails (judged by exit status, not grep output).
log=$(mktemp)
if ! bash scripts/validate.sh > "$log" 2>&1; then
  grep FAIL "$log"
  echo "pre-commit: validate.sh failed, commit blocked (full log: $log)"
  exit 1
fi
HOOK
chmod +x .git/hooks/pre-commit
echo "installed .git/hooks/pre-commit"
