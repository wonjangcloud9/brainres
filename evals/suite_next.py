#!/usr/bin/env python3
"""Suite helper (V1): which prompts still need a run, and a running report.

  python3 evals/suite_next.py --n 15      # ids of the next 15 unrun prompts (comma-separated)
  python3 evals/suite_next.py --report    # per-prompt scores of the latest chunk + check counts so far
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def suite_runs() -> list[Path]:
    out = []
    for p in sorted((ROOT / "evals/results").glob("*/summary.json")):
        d = json.loads(p.read_text())
        if d.get("prompt_set") == "suite.jsonl":
            out.append(p)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int)
    ap.add_argument("--report", action="store_true")
    a = ap.parse_args()
    runs = suite_runs()
    done = {r["id"] for p in runs for r in json.loads(p.read_text())["rows"]}
    prompts = [json.loads(l) for l in (ROOT / "evals/suite.jsonl").read_text().splitlines() if l.strip()]
    order = sorted(prompts, key=lambda x: (x["id"][3], x["id"][1:3]))  # sample index first, then category
    if a.n:
        print(",".join([x["id"] for x in order if x["id"] not in done][: a.n]))
    if a.report:
        latest = json.loads(runs[-1].read_text())["rows"]
        by: dict = {}
        for r in latest:
            by.setdefault(r["id"], {})[r["condition"]] = r
        print(f"latest chunk: {runs[-1].parent.name}")
        for i, v in sorted(by.items()):
            b, s = v.get("baseline", {}), v.get("brainres", {})
            lower = " <-- brainres lower" if s.get("score", 0) < b.get("score", 0) else ""
            tool = " TOOL" if b.get("tool_markup") or s.get("tool_markup") else ""
            print(f"  {i:<18} base {b.get('score')}/{b.get('words')} · brainres {s.get('score')}/{s.get('words')} {','.join(s.get('checks', []))}{lower}{tool}")
        cnt = {"baseline": Counter(), "brainres": Counter()}
        n = Counter()
        for p in runs:
            for r in json.loads(p.read_text())["rows"]:
                if r.get("tool_markup"):
                    continue
                n[r["condition"]] += 1
                cnt[r["condition"]].update(r["checks"])
        print(f"prompts run: {len(done)}/80")
        for c in cnt:
            print(f"  {c:<9} n={n[c]} " + ", ".join(f"{k} {v}" for k, v in cnt[c].most_common(6)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
