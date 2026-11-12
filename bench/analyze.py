#!/usr/bin/env python3
"""Analyze benchmark submissions exactly as pre-registered in bench/PROTOCOL.md.

  python3 bench/analyze.py                       # read bench/results/*.json
  python3 bench/analyze.py --from-issues         # fetch "benchmark-result" issues with gh, then analyze
  python3 bench/analyze.py --out bench/REPORT.md

Stdlib only. This implements the protocol's pre-registered *fallback* analysis:
per-participant condition means, paired tests across participants.
  H1  find faster:   per-participant mean log(ms) on correct Q1 trials; brainres − baseline;
                     Wilcoxon signed-rank + geometric-mean time ratio with 95% t-CI
  H2  not worse:     per-participant Q2 accuracy difference; non-inferior if the lower 95% bound > −10 pp
                     (margin amended from 5 pp before data collection; see PROTOCOL.md amendment v1.1)
  H3  calibration:   per-participant Brier score (confidence 1–5 → p = .25 … 1.0); Wilcoxon signed-rank
  E1  preference:    sign test on brainres vs baseline choices ("same" excluded)
Exclusions (pre-registered): failed attention check, total time < 3 min, not fluent.
"""
from __future__ import annotations

import argparse
import datetime as dt
import itertools
import json
import math
import re
import statistics as st
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NI_MARGIN = 0.10  # PROTOCOL.md v1.1
T95 = {1: 12.71, 2: 4.30, 3: 3.18, 4: 2.78, 5: 2.57, 6: 2.45, 7: 2.36, 8: 2.31, 9: 2.26, 10: 2.23, 11: 2.20,
       12: 2.18, 13: 2.16, 14: 2.14, 15: 2.13, 20: 2.09, 25: 2.06, 30: 2.04, 40: 2.02, 60: 2.00, 120: 1.98}


def t95(df: int) -> float:
    return T95.get(df) or T95[max(k for k in T95 if k <= df)] if df >= 1 else float("nan")


def norm_sf(z: float) -> float:
    return 0.5 * math.erfc(z / math.sqrt(2))


def wilcoxon(d: list[float]) -> float:
    """Two-sided Wilcoxon signed-rank p-value (exact for n ≤ 20, normal approximation otherwise)."""
    d = [x for x in d if x != 0]
    n = len(d)
    if n == 0:
        return 1.0
    order = sorted(range(n), key=lambda i: abs(d[i]))
    ranks = [0.0] * n
    i = 0
    while i < n:  # average ranks for ties
        j = i
        while j + 1 < n and abs(d[order[j + 1]]) == abs(d[order[i]]):
            j += 1
        for k in range(i, j + 1):
            ranks[order[k]] = (i + j) / 2 + 1
        i = j + 1
    w_plus = sum(r for r, x in zip(ranks, d) if x > 0)
    total = n * (n + 1) / 2
    if n <= 20:
        count = sum(1 for signs in itertools.product((0, 1), repeat=n)
                    if sum(r for r, s in zip(ranks, signs) if s) <= min(w_plus, total - w_plus) + 1e-9)
        return min(1.0, 2 * count / 2 ** n)
    mean, sd = total / 2, math.sqrt(n * (n + 1) * (2 * n + 1) / 24)
    return min(1.0, 2 * norm_sf((abs(w_plus - mean) - 0.5) / sd))


def sign_test(k: int, n: int) -> float:
    if n == 0:
        return 1.0
    tail = sum(math.comb(n, i) for i in range(0, min(k, n - k) + 1)) / 2 ** n
    return min(1.0, 2 * tail)


def mean_ci(v: list[float]) -> tuple[float, float, float]:
    m = st.mean(v)
    if len(v) < 2:
        return m, float("nan"), float("nan")
    h = t95(len(v) - 1) * st.stdev(v) / math.sqrt(len(v))
    return m, m - h, m + h


def load_local() -> list[dict]:
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted((ROOT / "bench/results").glob("*.json"))]


def load_issues() -> list[dict]:
    out = subprocess.run(["gh", "issue", "list", "--label", "benchmark-result", "--state", "all", "--limit", "500",
                          "--json", "number,body"], capture_output=True, text=True, check=True).stdout
    subs = []
    for issue in json.loads(out):
        m = re.search(r"\{.*\}", issue["body"], re.S)
        if m:
            try:
                d = json.loads(m.group(0)); d["_issue"] = issue["number"]; subs.append(d)
            except json.JSONDecodeError:
                pass
    return subs


def exclusion(s: dict) -> str | None:
    if s.get("attention") is not True:
        return "attention check"
    if not s.get("fluent"):
        return "not fluent"
    try:
        dur = (dt.datetime.fromisoformat(s["finished"].replace("Z", "+00:00"))
               - dt.datetime.fromisoformat(s["started"].replace("Z", "+00:00"))).total_seconds()
    except (KeyError, ValueError):
        return "missing timestamps"
    return "under 3 minutes" if dur < 180 else None


def conf_p(c: int) -> float:
    return 0.25 + 0.75 * (c - 1) / 4  # 1 = chance among 4 options, 5 = certain


def analyze(subs: list[dict], lang: str = "en") -> dict:
    subs = [s for s in subs if s.get("lang") == lang]
    excluded = {}
    kept = []
    seen = set()
    for s in subs:
        if s.get("id") in seen:
            excluded["duplicate id"] = excluded.get("duplicate id", 0) + 1
            continue
        seen.add(s.get("id"))
        why = exclusion(s)
        if why:
            excluded[why] = excluded.get(why, 0) + 1
        else:
            kept.append(s)
    h1, h2, h3 = [], [], []
    for s in kept:
        by = {c: [t for t in s["trials"] if t["version"] == c] for c in ("baseline", "brainres")}
        if not by["baseline"] or not by["brainres"]:
            continue
        lt = {c: [math.log(t["q1"]["ms"]) for t in by[c] if t["q1"]["correct"] and t["q1"]["ms"] > 0] for c in by}
        if lt["baseline"] and lt["brainres"]:
            h1.append(st.mean(lt["brainres"]) - st.mean(lt["baseline"]))
        acc = {c: st.mean(1.0 if t["q2"]["correct"] else 0.0 for t in by[c]) for c in by}
        h2.append(acc["brainres"] - acc["baseline"])
        brier = {c: st.mean((conf_p(t[q]["conf"]) - (1.0 if t[q]["correct"] else 0.0)) ** 2
                            for t in by[c] for q in ("q1", "q2")) for c in by}
        h3.append(brier["brainres"] - brier["baseline"])
    prefs = [p["choice"] for s in kept for p in s.get("preference", [])]
    r = {"lang": lang, "submitted": len(subs), "analyzed": len(kept), "excluded": excluded}
    if len(h1) >= 2:
        m, lo, hi = mean_ci(h1)
        r["H1"] = {"n": len(h1), "time_ratio": math.exp(m), "ci": (math.exp(lo), math.exp(hi)), "p": wilcoxon(h1),
                   "supported": wilcoxon(h1) < 0.05 and m < 0}
    if len(h2) >= 2:
        m, lo, hi = mean_ci(h2)
        r["H2"] = {"n": len(h2), "diff_pp": 100 * m, "ci_pp": (100 * lo, 100 * hi), "non_inferior": lo > -NI_MARGIN}
    if len(h3) >= 2:
        r["H3"] = {"n": len(h3), "brier_diff": st.mean(h3), "p": wilcoxon(h3), "supported": wilcoxon(h3) < 0.05 and st.mean(h3) < 0}
    k, n = prefs.count("brainres"), prefs.count("brainres") + prefs.count("baseline")
    r["E1"] = {"brainres": k, "baseline": n - k, "same": prefs.count("same"), "p": sign_test(k, n)}
    r["claim_allowed"] = bool(r.get("H1", {}).get("supported") and r.get("H2", {}).get("non_inferior"))
    return r


def report(results: list[dict]) -> str:
    lines = ["# Reading benchmark report", "", f"Generated {dt.date.today().isoformat()} by `bench/analyze.py`, using the pre-registered fallback analysis in [PROTOCOL.md](PROTOCOL.md).", ""]
    for r in results:
        lines += [f"## {r['lang'].upper()} set", "",
                  f"- Submitted: {r['submitted']} · analyzed: {r['analyzed']} · excluded: "
                  + (", ".join(f"{k} {v}" for k, v in r["excluded"].items()) or "none")]
        if "H1" in r:
            h = r["H1"]
            lines.append(f"- **H1 (find faster):** brainres/baseline time ratio {h['time_ratio']:.2f} "
                         f"(95% CI {h['ci'][0]:.2f}–{h['ci'][1]:.2f}), Wilcoxon p = {h['p']:.3f}, n = {h['n']} → "
                         + ("**supported**" if h["supported"] else "not supported"))
        if "H2" in r:
            h = r["H2"]
            lines.append(f"- **H2 (comprehension not worse):** accuracy difference {h['diff_pp']:+.1f} pp "
                         f"(95% CI {h['ci_pp'][0]:+.1f} to {h['ci_pp'][1]:+.1f}), margin −{100*NI_MARGIN:.0f} pp → "
                         + ("**non-inferior**" if h["non_inferior"] else "non-inferiority **not shown**"))
        if "H3" in r:
            h = r["H3"]
            lines.append(f"- **H3 (calibration):** Brier difference {h['brier_diff']:+.3f} (negative = better), "
                         f"Wilcoxon p = {h['p']:.3f} → " + ("**supported**" if h["supported"] else "not supported"))
        e = r["E1"]
        lines.append(f"- **E1 (preference, exploratory):** brainres {e['brainres']}, baseline {e['baseline']}, same {e['same']}, sign test p = {e['p']:.3f}")
        lines += ["", f"**Decision rule:** the README may claim \"improves comprehension\": **{'yes' if r['claim_allowed'] else 'no'}**.", ""]
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-issues", action="store_true")
    ap.add_argument("--out")
    a = ap.parse_args()
    subs = load_issues() if a.from_issues else load_local()
    text = report([analyze(subs, "en"), analyze(subs, "ko")])
    print(text)
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
