#!/usr/bin/env bash
# Structural checks for the brainres repo. Run before every commit.
set -euo pipefail
cd "$(dirname "$0")/.."

fail=0
err() { echo "FAIL: $*"; fail=1; }
ok()  { echo "ok:   $*"; }

SKILL=skills/brainres/SKILL.md
MAX_WORDS=${MAX_WORDS:-1800}   # ~1.9k tokens when invoked; the always-on card is separate (hooks/core-card.md)

[ -f "$SKILL" ] || { err "$SKILL missing"; exit 1; }

# 1. Frontmatter
head -1 "$SKILL" | grep -q '^---$' || err "SKILL.md must start with YAML frontmatter"
fm=$(awk 'NR==1{next} /^---$/{exit} {print}' "$SKILL")
name=$(printf '%s\n' "$fm" | sed -n 's/^name: *//p')
desc=$(printf '%s\n' "$fm" | sed -n 's/^description: *//p')
[ "$name" = "brainres" ] && ok "name = brainres" || err "frontmatter name must be 'brainres' (got '$name')"
[ -n "$desc" ] && ok "description present" || err "description missing"
[ "${#desc}" -le 1024 ] && ok "description ${#desc} chars (<=1024)" || err "description too long (${#desc})"

# 2. Body budget
words=$(awk 'BEGIN{c=0} NR==1{next} /^---$/ && !d{d=1; next} d{c+=NF} END{print c}' "$SKILL")
[ "$words" -le "$MAX_WORDS" ] && ok "SKILL.md body $words words (<=$MAX_WORDS)" || err "SKILL.md body $words words > $MAX_WORDS — move detail to references/"

# 3. Every relative link in skill files resolves
tmp=$(mktemp)
while IFS= read -r f; do
  dir=$(dirname "$f")
  grep -oE '\]\([^)#]+\)' "$f" | sed -E 's/^\]\(//; s/\)$//' | grep -vE '^(https?:|mailto:)' | while IFS= read -r link; do
    [ -e "$dir/$link" ] || echo "FAIL: broken link in $f -> $link"
  done
done < <(find skills README*.md -name '*.md' 2>/dev/null) > "$tmp" || true
cat "$tmp"
if grep -q FAIL "$tmp"; then fail=1; else ok "relative links resolve"; fi
rm -f "$tmp"

# 4. JSON manifests parse
for j in $(find . -path ./node_modules -prune -o -name '*.json' -print | grep -v '^./.git/'); do
  python3 -c "import json,sys; json.load(open(sys.argv[1]))" "$j" && ok "json $j" || err "invalid json $j"
done

# 5. Neuromyths must not be used as support inside the skill
if grep -RniE 'learning styles?|left[- ]brain|right[- ]brain|10% of (the|your) brain' skills/ | grep -viE 'myth|not |never|avoid' ; then
  err "neuromyth referenced as support in skills/"
else
  ok "no neuromyths used as support"
fi

# 5b. Always-on card budget: 418 tokens measured at 1,140 chars (~2.7 chars/token); cap ≈500 tokens
card_chars=$(wc -c < hooks/core-card.md | tr -d ' ')
[ "$card_chars" -le 1350 ] && ok "core card $card_chars chars (<=1350, ~500 tokens)" || err "core card $card_chars chars > 1350 — re-rank (research/core-card-ranking.md)"

# 6. Hook emits valid JSON
out=$(CLAUDE_PLUGIN_ROOT="$PWD" bash hooks/brainres-context.sh)
printf '%s' "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['hookSpecificOutput']['additionalContext']" && ok "session hook emits context" || err "session hook output invalid"
bash hooks/brainres-reminder.sh | python3 -c "import json,sys; c=json.load(sys.stdin)['hookSpecificOutput']['additionalContext']; assert 0 < len(c) <= 300" && ok "per-turn reminder valid (<=300 chars)" || err "per-turn reminder invalid or too long"
[ -z "$(BRAINRES=off bash hooks/brainres-reminder.sh)" ] && ok "BRAINRES=off silences reminder" || err "BRAINRES=off did not silence reminder"
[ -z "$(BRAINRES=off bash hooks/brainres-context.sh)" ] && ok "BRAINRES=off silences hook" || err "BRAINRES=off did not silence hook"

# 7. brainlint sanity: bad example scores lower than good example
b=$(python3 skills/brainres/scripts/brainlint.py --json examples/01-react-rerender/before.md | python3 -c "import json,sys; print(json.load(sys.stdin)['score'])")
a=$(python3 skills/brainres/scripts/brainlint.py --json examples/01-react-rerender/after.md | python3 -c "import json,sys; print(json.load(sys.stdin)['score'])")
[ "$a" -gt "$b" ] && ok "brainlint ranks after ($a) > before ($b)" || err "brainlint ranking broken ($a vs $b)"

# 8. Research coverage may only go up (ratchet in research/.coverage-floor)
python3 scripts/coverage.py --check >/dev/null && ok "coverage ratchet: $(python3 scripts/coverage.py | sed -n 2p)" || err "coverage fell below floor — a cited finding was removed"

# 8b. Portable builds in dist/ match the sources (rebuild with scripts/build_dist.py)
python3 scripts/build_dist.py --check >/dev/null && ok "dist/ up to date" || err "dist/ is stale — run python3 scripts/build_dist.py"

# 9. Official plugin validator, when the CLI is available
if command -v claude >/dev/null 2>&1; then
  claude plugin validate . >/dev/null 2>&1 && ok "claude plugin validate" || err "claude plugin validate failed"
fi

[ $fail -eq 0 ] && echo "ALL CHECKS PASSED" || { echo "VALIDATION FAILED"; exit 1; }
