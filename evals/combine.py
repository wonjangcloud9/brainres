#!/usr/bin/env python3
"""Combine eval runs (results/*/summary.json) made with the same core card and model.

  python3 evals/combine.py                      # all runs matching the current card
  python3 evals/combine.py --out results/combined-<date>.md

Reports per-condition means with SD and the paired per-prompt difference
(brainres − baseline) with a 95% t-interval across prompts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import statistics as st
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUDGET = {"yes/no": 100, "misconception": 100}  # same as run.py; older runs lack within_budget
DEFAULT_BUDGET = 300
# two-sided 95% t critical values by degrees of freedom (enough for ≤30 prompts)
T95 = {1: 12.71, 2: 4.30, 3: 3.18, 4: 2.78, 5: 2.57, 6: 2.45, 7: 2.36, 8: 2.31, 9: 2.26, 10: 2.23,
       11: 2.20, 12: 2.18, 13: 2.16, 14: 2.14, 15: 2.13, 20: 2.09, 25: 2.06, 29: 2.05}


def t95(df: int) -> float:
    return T95.get(df) or T95[max(k for k in T95 if k <= df)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--out")
    ap.add_argument("--prompts", default="prompts.jsonl", help="only combine runs of this prompt set")
    ap.add_argument("--treatment", default="brainres", help="condition to compare with baseline (brainres or plugin)")
    a = ap.parse_args()
    sha = hashlib.sha256((ROOT / "hooks/core-card.md").read_bytes()).hexdigest()[:12]
    rows, used = [], []
    for f in sorted((ROOT / "evals/results").glob("*/summary.json")):
        d = json.loads(f.read_text())
        if d.get("model") != a.model or d.get("style") or d.get("prompt_set", "prompts.jsonl") != a.prompts:
            continue  # style experiments and other prompt sets are reported separately
        keep = [r for r in d["rows"] if r["condition"] == "baseline" or (d.get("card_sha") == sha and r["condition"] == a.treatment)]
        for r in keep:
            if r["condition"] == a.treatment:
                r["condition"] = "brainres"  # the comparison column; the label below names the treatment
        for r in keep:
            r.setdefault("within_budget", r["words"] <= BUDGET.get(r["type"], DEFAULT_BUDGET))
        if keep:
            rows += keep
            used.append(f"{f.parent.name} ({len(keep)} answers)")
    by = defaultdict(list)
    for r in rows:
        by[(r["id"], r["condition"])].append(r)
    ids = sorted({r["id"] for r in rows})
    paired = [i for i in ids if by[(i, "baseline")] and by[(i, "brainres")]]

    def cond_stats(c, key, fn=st.mean):
        v = [r[key] for r in rows if r["condition"] == c and r["id"] in paired]
        return fn(v), (st.stdev(v) if len(v) > 1 else 0.0), len(v)

    def diff_ci(key):
        d = [st.mean(r[key] for r in by[(i, "brainres")]) - st.mean(r[key] for r in by[(i, "baseline")]) for i in paired]
        m = st.mean(d)
        half = t95(len(d) - 1) * st.stdev(d) / len(d) ** 0.5 if len(d) > 1 else float("nan")
        return m, m - half, m + half

    lines = [f"# Combined eval (card {sha}, model={a.model}, treatment={a.treatment})", "", "Runs: " + "; ".join(used), "",
             f"Paired prompts: {len(paired)}. Baseline rows are card-independent; brainres rows only from card {sha}.", "",
             "| Metric | baseline mean (SD, n) | brainres mean (SD, n) | brainres − baseline per prompt (95% CI) |",
             "|---|---|---|---|"]
    metrics = [("score", "Brain Score"), ("words", "Words"), ("output_tokens", "Output tokens (incl. hidden reasoning)")]
    if all("visible_output_tokens" in r for r in rows if r["id"] in paired):
        metrics.append(("visible_output_tokens", "Visible output tokens"))
    for key, label in metrics:
        b, x, (m, lo, hi) = cond_stats("baseline", key), cond_stats("brainres", key), diff_ci(key)
        lines.append(f"| {label} | {b[0]:.1f} ({b[1]:.1f}, {b[2]}) | {x[0]:.1f} ({x[1]:.1f}, {x[2]}) | {m:+.1f} ({lo:+.1f} to {hi:+.1f}) |")
    for key, label in [("within_budget", "Within length budget"), ("answer_first", "No preamble / buried answer")]:
        cells = []
        for c in ("baseline", "brainres"):
            v = [r.get(key) for r in rows if r["condition"] == c and r["id"] in paired and r.get(key) is not None]
            cells.append(f"{sum(v)}/{len(v)}" if v else "n/a")
        lines.append(f"| {label} | {cells[0]} | {cells[1]} | |")
    text = "\n".join(lines) + "\n"
    print(text)
    if a.out:
        (ROOT / "evals" / a.out).write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
