#!/usr/bin/env python3
"""B46: does the per-turn reminder keep brainres rules active over a long session?

Runs scripted multi-turn conversations with the real plugin (SessionStart card + UserPromptSubmit
reminder), resuming the same session each turn, with the reminder on vs off (BRAINRES_REMINDER=off;
the card stays on). Each answer is scored with brainlint (question-aware) per turn.

  python3 evals/multiturn.py --model sonnet
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "skills/brainres/scripts"))
import brainlint  # noqa: E402

CONVERSATIONS = {
    "en": ["My Flask app returns 500 on /login after I added a database. Where do I start?",
           "What's the difference between a session cookie and a JWT?",
           "Should I store the JWT in localStorage or an httpOnly cookie?",
           "Is bcrypt still OK for hashing passwords in 2026?",
           "How do I add rate limiting to the login route?",
           "If 3% of 40,000 monthly logins fail, how many failures is that per day?",
           "Explain what this does: `@app.after_request\ndef h(r): r.headers['X-Frame-Options'] = 'DENY'; return r`"],
    "ko": ["Next.js 앱에서 빌드는 되는데 배포하면 흰 화면만 나와요. 어디부터 봐야 해요?",
           "SSR이랑 SSG 차이가 뭐예요?",
           "블로그면 SSR이랑 SSG 중에 뭐가 나아요?",
           "이미지 최적화에 next/image 꼭 써야 해요?",
           "환경 변수를 클라이언트에서 쓰려면 어떻게 해요?",
           "월 방문자 12만 명이고 평균 3페이지를 보면 하루 페이지뷰가 몇이에요?",
           "이 코드 뭐 하는 거예요? `export const revalidate = 60`"],
}


def _log(n: int, seed: int) -> str:
    import random
    r = random.Random(seed)
    paths = ["/api/users", "/api/orders", "/health", "/api/login", "/static/app.js"]
    lines = [f"2026-11-12T10:{i // 60:02d}:{i % 60:02d}Z INFO {r.choice(['GET', 'POST'])} {r.choice(paths)} 200 {r.randint(3, 90)}ms"
             for i in range(n)]
    lines[n * 2 // 3] = "2026-11-12T10:40:12Z ERROR POST /api/orders 500 3012ms psycopg2.OperationalError: connection pool exhausted"
    return "```\n" + "\n".join(lines) + "\n```"


def _code(n_funcs: int) -> str:
    body = []
    for i in range(n_funcs):
        body.append(f"def handler_{i}(req):\n    data = req.json()\n    if not data.get('id'):\n        return {{'error': 'missing id'}}, 400\n"
                    f"    item = db.get(data['id'])\n    return {{'item': item, 'n': {i}}}, 200\n")
    return "```python\n" + "\n".join(body) + "```"


# B47: long context. Turns 1–4 paste ~3k-token logs or code; turns 5–7 are plain questions that are
# also asked in fresh sessions as the control.
LONG = {
    "en": [f"Here's our API log from this morning. Anything wrong?\n\n{_log(260, 1)}",
           f"Here's the handlers file. Is there a pattern I should refactor?\n\n{_code(45)}",
           f"Another log from the afternoon. Same problem?\n\n{_log(260, 2)}",
           f"And the older handlers, for comparison:\n\n{_code(45)}",
           "Should I use PgBouncer or just raise max_connections?",
           "Is it safe to run VACUUM FULL during business hours?",
           "How do I find which queries hold connections the longest in Postgres?"],
    "ko": [f"오늘 아침 API 로그예요. 이상한 거 있어요?\n\n{_log(260, 3)}",
           f"핸들러 파일이에요. 리팩터링할 패턴이 있어요?\n\n{_code(45)}",
           f"오후 로그도 있어요. 같은 문제예요?\n\n{_log(260, 4)}",
           f"비교용으로 예전 핸들러도 붙여요.\n\n{_code(45)}",
           "PgBouncer를 쓰는 게 나아요, 아니면 max_connections를 올리는 게 나아요?",
           "업무 시간에 VACUUM FULL 돌려도 안전해요?",
           "Postgres에서 커넥션을 가장 오래 잡고 있는 쿼리는 어떻게 찾아요?"],
}


def turn(q: str, model: str, session: str | None, cwd: str, env: dict) -> dict:
    args = ["claude", "-p", q, "--model", model, "--output-format", "json", "--tools", "",
            "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}', "--plugin-dir", str(ROOT)]
    if session:
        args += ["--resume", session]
    p = subprocess.run(args, capture_output=True, text=True, cwd=cwd, env=env, stdin=subprocess.DEVNULL, timeout=300)
    return json.loads(p.stdout)


def conversation(lang: str, cond: str, model: str, convs: dict | None = None) -> list[dict]:
    convs = convs or CONVERSATIONS
    env = dict(os.environ)
    if cond == "no-reminder":
        env["BRAINRES_REMINDER"] = "off"
    rows, session = [], None
    with tempfile.TemporaryDirectory() as cwd:
        for i, q in enumerate(convs[lang], 1):
            try:
                d = turn(q, model, session, cwd, env)
            except Exception as e:  # keep the turns we have
                rows.append({"lang": lang, "condition": cond, "turn": i, "error": f"{type(e).__name__}: {e}"[:200]})
                break
            session = d.get("session_id", session)
            text = d.get("result", "")
            rep = brainlint.lint(text, q)
            rows.append({"lang": lang, "condition": cond, "turn": i, "q": q, "text": text, "score": rep.score, "words": rep.words,
                         "checks": sorted({x.check for x in rep.findings})})
            print(f"{lang} {cond:<12} turn {i} ctx={d.get('usage', {}).get('cache_read_input_tokens', 0) + d.get('usage', {}).get('input_tokens', 0) + d.get('usage', {}).get('cache_creation_input_tokens', 0)} score={rep.score:>3} words={rep.words:>4} {','.join(rows[-1]['checks'])}", flush=True)
    return rows


def long_main(model: str) -> int:
    out = ROOT / "evals/results" / f"{dt.date.today().isoformat()}-multiturn-long-{model}"
    out.mkdir(parents=True, exist_ok=True)
    jobs = [("long", l, None) for l in LONG] + [("fresh", l, (q, k)) for l in LONG for q in LONG[l][4:] for k in (1, 2)]
    def run(job):
        kind, lang, extra = job
        if kind == "long":
            return conversation(lang, "long", model, LONG)
        q, k = extra
        rows = conversation(lang, "fresh", model, {lang: [q]})
        for r in rows:
            r["turn"] = LONG[lang].index(q) + 1; r["sample"] = k
        return rows
    with cf.ThreadPoolExecutor(6) as ex:
        rows = [r for f in [ex.submit(run, j) for j in jobs] for r in f.result()]
    rows.sort(key=lambda r: (r["lang"], r["condition"], r["turn"], r.get("sample", 0)))
    (out / "summary.json").write_text(json.dumps({"model": model, "rows": [{k: v for k, v in r.items() if k != "q" or len(v) < 500} for r in rows]},
                                                 ensure_ascii=False, indent=2))
    for c in ("long", "fresh"):
        rs = [r for r in rows if r["condition"] == c and r["turn"] >= 5 and "score" in r]
        print(f"{c:<6} turns 5-7: mean score {sum(r['score'] for r in rs)/len(rs):.1f} · mean words {sum(r['words'] for r in rs)/len(rs):.0f} (n={len(rs)})")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--long", action="store_true", help="B47: long-context sessions vs fresh-session control")
    a = ap.parse_args()
    if a.long:
        return long_main(a.model)
    out = ROOT / "evals/results" / f"{dt.date.today().isoformat()}-multiturn-{a.model}"
    out.mkdir(parents=True, exist_ok=True)
    with cf.ThreadPoolExecutor(4) as ex:
        rows = [r for f in [ex.submit(conversation, l, c, a.model) for l in CONVERSATIONS for c in ("reminder", "no-reminder")]
                for r in f.result()]
    rows.sort(key=lambda r: (r["lang"], r["condition"], r["turn"]))
    (out / "summary.json").write_text(json.dumps({"model": a.model, "rows": rows}, ensure_ascii=False, indent=2))
    for c in ("reminder", "no-reminder"):
        for span, lo, hi in (("turns 1-2", 1, 2), ("turns 3-4", 3, 4), ("turns 5-7", 5, 7)):
            rs = [r for r in rows if r["condition"] == c and lo <= r["turn"] <= hi and "score" in r]
            if rs:
                print(f"{c:<12} {span}: mean score {sum(r['score'] for r in rs)/len(rs):.1f} · mean words {sum(r['words'] for r in rs)/len(rs):.0f} (n={len(rs)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
