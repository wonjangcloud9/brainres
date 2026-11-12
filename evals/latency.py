#!/usr/bin/env python3
"""L1: does the card delay the first visible text? (Its extra thinking happens before the answer streams.)

For each prompt × condition, streams `claude -p --output-format stream-json --include-partial-messages` and records:
  first_text_s   seconds from launch to the first text delta (what a reader sees first)
  total_s        seconds to the end of the run
  thought        whether any thinking delta arrived before the text
Conditions run interleaved in a seeded random order, 3 at a time, so load affects both alike.

  python3 evals/latency.py --ids s011-debug,... --model sonnet
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import json
import random
import statistics as st
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "evals"))
import run  # noqa: E402  (card text)


def one(q: str, model: str, system: str | None, cwd: str) -> dict:
    args = ["claude", "-p", q, "--model", model, "--output-format", "stream-json", "--verbose", "--include-partial-messages",
            "--tools", "", "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}']
    if system:
        args += ["--append-system-prompt", system]
    t0 = time.monotonic()
    first_text = first_any = None
    thought = False
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL, text=True, cwd=cwd)
    for line in p.stdout:
        now = time.monotonic() - t0
        if '"thinking_delta"' in line or '"thinking"' in line and '"content_block_start"' in line:
            thought = True
            first_any = first_any or now
        if '"text_delta"' in line and first_text is None:
            first_text = now
            first_any = first_any or now
    p.wait()
    return {"first_text_s": round(first_text, 2) if first_text else None, "first_any_s": round(first_any, 2) if first_any else None,
            "total_s": round(time.monotonic() - t0, 2), "thought": thought}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", required=True)
    ap.add_argument("--model", default="sonnet")
    a = ap.parse_args()
    S = {json.loads(l)["id"]: json.loads(l) for l in (ROOT / "evals/suite.jsonl").read_text().splitlines() if l.strip()}
    ids = a.ids.split(",")
    jobs = [(i, c) for i in ids for c in ("baseline", "brainres")]
    random.Random(7).shuffle(jobs)
    card = run.brainres_prompt()
    rows = []
    with tempfile.TemporaryDirectory() as cwd, cf.ThreadPoolExecutor(3) as ex:
        futs = {ex.submit(one, S[i]["q"], a.model, card if c == "brainres" else None, cwd): (i, c) for i, c in jobs}
        for f in cf.as_completed(futs):
            i, c = futs[f]
            r = {"id": i, "condition": c, **f.result()}
            rows.append(r)
            print(f"{i:<16} {c:<9} first text {r['first_text_s']}s · total {r['total_s']}s · thought {r['thought']}", flush=True)
    out = ROOT / "evals/results" / f"{dt.date.today().isoformat()}-latency-{a.model}"
    out.mkdir(parents=True, exist_ok=True)
    (out / "summary.json").write_text(json.dumps({"model": a.model, "card_sha": run.card_sha(), "rows": rows}, indent=2))
    by = {}
    for r in rows:
        by.setdefault(r["id"], {})[r["condition"]] = r
    pairs = [v for v in by.values() if len(v) == 2 and v["baseline"]["first_text_s"] and v["brainres"]["first_text_s"]]
    d = [v["brainres"]["first_text_s"] - v["baseline"]["first_text_s"] for v in pairs]
    for c in ("baseline", "brainres"):
        print(f"{c:<9} median first text {st.median(v[c]['first_text_s'] for v in pairs):.2f}s · median total "
              f"{st.median(v[c]['total_s'] for v in pairs):.2f}s · thought {sum(v[c]['thought'] for v in pairs)}/{len(pairs)}")
    print(f"paired Δ first text: median {st.median(d):+.2f}s, mean {st.mean(d):+.2f}s (n={len(d)})")
    th = [v["brainres"]["first_text_s"] - v["baseline"]["first_text_s"] for v in pairs if v["brainres"]["thought"]]
    if th:
        print(f"  on prompts where brainres thought: median Δ {st.median(th):+.2f}s (n={len(th)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
