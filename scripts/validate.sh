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

# 5b. Always-on card budget: 500 tokens measured at 1,349 bytes (~2.7 bytes/token); cap ≈500 tokens
card_chars=$(wc -c < hooks/core-card.md | tr -d ' ')
[ "$card_chars" -le 1350 ] && ok "core card $card_chars chars (<=1350, ~500 tokens)" || err "core card $card_chars chars > 1350 — re-rank (research/core-card-ranking.md)"

# 6. Hook emits valid JSON
out=$(CLAUDE_PLUGIN_ROOT="$PWD" bash hooks/brainres-context.sh)
printf '%s' "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['hookSpecificOutput']['additionalContext']" && ok "session hook emits context" || err "session hook output invalid"
[ -z "$(bash hooks/brainres-reminder.sh < /dev/null)" ] && ok "situation hook silent without a prompt" || err "situation hook should emit nothing without a signal"
[ -z "$(printf '{"prompt":"How do I rename a git branch?"}' | bash hooks/brainres-reminder.sh)" ] && ok "situation hook silent on a general prompt (B46)" || err "situation hook emitted on a general prompt"
printf '{"prompt":"I am learning Python"}' | bash hooks/brainres-reminder.sh | python3 -c "import json,sys; c=json.load(sys.stdin)['hookSpecificOutput']['additionalContext']; assert 0 < len(c) <= 300" && ok "situation line valid JSON (<=300 chars)" || err "situation line invalid or too long"
# Situation line (B40): learner prompts get it, general prompts and learner-ish paths in cwd don't.
rem() { printf '{"prompt":%s,"cwd":"/home/homework/beginner"}' "$(python3 -c 'import json,sys; print(json.dumps(sys.argv[1]))' "$1")" | bash hooks/brainres-reminder.sh; }
learner_ok=1
for p in "I'm learning Python. This returns 0" "파이썬 공부 중인데요" "C 배우는 중이에요"; do rem "$p" | grep -q "Learner:" || learner_ok=0; done
for p in "CORS가 뭐야?" "How do I rename a git branch?" "Why is my query slow?"; do rem "$p" | grep -q "Learner:" && learner_ok=0; done
BRAINRES_SITUATIONS=off rem "I'm learning Python" | grep -q "Learner:" && learner_ok=0
for p in "URGENT: our production site is down" "급해요 ㅠㅠ 작업한 거 다 날아갔어요" "I ran DROP TABLE users by accident"; do rem "$p" | grep -q "Emergency:" || learner_ok=0; done
for p in "CORS가 뭐야?" "How do I rename a git branch?" "What should I check before deploying to production?"; do rem "$p" | grep -q "Emergency:" && learner_ok=0; done
[ $learner_ok = 1 ] && ok "reminder adds learner / emergency lines only on matching prompts" || err "reminder situation-line routing wrong"
# B48: the always-on line returns automatically for Haiku sessions (transcript's last model), never for others
tmpd=$(mktemp -d); printf '{"message":{"model":"claude-haiku-5-5"}}\n' > "$tmpd/h.jsonl"; printf '{"message":{"model":"claude-sonnet-5-5"}}\n' > "$tmpd/s.jsonl"
hk=$(printf '{"prompt":"What is CORS?","transcript_path":"%s"}' "$tmpd/h.jsonl" | bash hooks/brainres-reminder.sh)
sn=$(printf '{"prompt":"What is CORS?","transcript_path":"%s"}' "$tmpd/s.jsonl" | bash hooks/brainres-reminder.sh)
hoff=$(printf '{"prompt":"What is CORS?","transcript_path":"%s"}' "$tmpd/h.jsonl" | BRAINRES_REMINDER=off bash hooks/brainres-reminder.sh)
printf '%s' "$hk" | grep -q "answer in sentence 1" && [ -z "$sn" ] && [ -z "$hoff" ] && ok "always-on line auto-enables for Haiku only (B48)" || err "Haiku auto-reminder routing wrong"
printf '%s' "$hk" | python3 -c "import json,sys; c=json.load(sys.stdin)['hookSpecificOutput']['additionalContext']; assert len(c) <= 300" && ok "Haiku reminder <=300 chars" || err "Haiku reminder too long"
rm -rf "$tmpd"
[ -z "$(BRAINRES=off bash hooks/brainres-reminder.sh < /dev/null)" ] && ok "BRAINRES=off silences reminder" || err "BRAINRES=off did not silence reminder"
[ -z "$(BRAINRES=off bash hooks/brainres-context.sh)" ] && ok "BRAINRES=off silences hook" || err "BRAINRES=off did not silence hook"

# 7. brainlint sanity: bad example scores lower than good example
b=$(python3 skills/brainres/scripts/brainlint.py --json examples/01-react-rerender/before.md | python3 -c "import json,sys; print(json.load(sys.stdin)['score'])")
a=$(python3 skills/brainres/scripts/brainlint.py --json examples/01-react-rerender/after.md | python3 -c "import json,sys; print(json.load(sys.stdin)['score'])")
[ "$a" -gt "$b" ] && ok "brainlint ranks after ($a) > before ($b)" || err "brainlint ranking broken ($a vs $b)"

# 7b. brainlint golden + unit tests (tests/)
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -q >/dev/null 2>&1 && ok "brainlint tests ($(grep -c 'def test_' tests/test_brainlint.py) tests)" || err "brainlint tests failed — run python3 -m unittest discover -s tests -v"

# 7c. README Brain Score badges match the current score (we eat our own cooking)
for f in README.md README.ko.md; do
  b=$(PYTHONDONTWRITEBYTECODE=1 python3 skills/brainres/scripts/brainlint.py --badge "$f")
  grep -qF "$b" "$f" && ok "$f badge matches score" || err "$f Brain Score badge is stale; expected: $b"
done

# 8. Research coverage may only go up (ratchet in research/.coverage-floor)
python3 scripts/coverage.py --check >/dev/null && ok "coverage ratchet: $(python3 scripts/coverage.py | sed -n 2p)" || err "coverage fell below floor — a cited finding was removed"

# 8b. Portable builds in dist/ match the sources (rebuild with scripts/build_dist.py)
python3 scripts/build_dist.py --check >/dev/null && ok "dist/ up to date" || err "dist/ is stale — run python3 scripts/build_dist.py"

# 8b2. Eval suite (owner direction 2026-11-13): 80 prompts, 16 types x 5, unique ids, Korean included
python3 -c "
import json; r=[json.loads(l) for l in open('evals/suite.jsonl') if l.strip()]
from collections import Counter; t=Counter(x['type'] for x in r)
assert len(r)==80 and len({x['id'] for x in r})==80 and len(t)==16 and set(t.values())=={5} and sum(x['lang']=='ko' for x in r)>=30
" && ok "eval suite: 80 prompts, 16 types x 5" || err "evals/suite.jsonl malformed"

# 8c. Benchmark page works end to end (headless Chrome autotest), when Chrome is available
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [ -x "$CHROME" ]; then
  dom=$("$CHROME" --headless=new --disable-gpu --virtual-time-budget=5000 --dump-dom "file://$PWD/bench/index.html#autotest" 2>/dev/null)
  printf '%s' "$dom" | python3 -c "
import sys,re,json,html
m=re.search(r'<textarea[^>]*>(.*?)</textarea>', sys.stdin.read(), re.S)
d=json.loads(html.unescape(m.group(1))); v=[t['version'] for t in d['trials']]
assert len(v)==8 and v.count('brainres')==4 and d['attention'] is not None and len(d['preference'])==2
" && ok "benchmark page autotest (8 trials, 4/4 counterbalanced)" || err "benchmark page autotest failed"
  dom=$("$CHROME" --headless=new --disable-gpu --virtual-time-budget=5000 --dump-dom "file://$PWD/bench/study2/index.html#autotest" 2>/dev/null)
  printf '%s' "$dom" | python3 -c "
import sys,re,json,html
m=re.search(r'<textarea[^>]*>(.*?)</textarea>', sys.stdin.read(), re.S)
d=json.loads(html.unescape(m.group(1))); t=d['trials']
cell=lambda c,v: sum(1 for x in t if x['content']==c and x['version']==v)
assert d['study']==2 and len(t)==8 and all(cell(c,v)==2 for c in ('causal','parallel') for v in ('prose','bullets'))
assert d['attention'] is not None and d['preference']==[]
" && ok "study 2 page autotest (8 trials, 2 per content × format cell)" || err "study 2 page autotest failed"
fi

# 8d. Playground parity with brainlint.py (needs network for Pyodide; opt-in)
if [ "${BRAINRES_NET_CHECKS:-0}" = "1" ]; then
  bash scripts/check_playground.sh >/dev/null && ok "playground parity with brainlint.py" || err "playground score differs from brainlint.py"
fi

# 9. Official plugin validator, when the CLI is available
if command -v claude >/dev/null 2>&1; then
  claude plugin validate . >/dev/null 2>&1 && ok "claude plugin validate" || err "claude plugin validate failed"
fi

[ $fail -eq 0 ] && echo "ALL CHECKS PASSED" || { echo "VALIDATION FAILED"; exit 1; }
