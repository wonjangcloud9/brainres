#!/usr/bin/env python3
"""V3: compare card-ablation runs with the full card on the same suite prompts (no model calls).

  python3 evals/ablation_report.py --out evals/ablation/RESULTS.md
"""
from __future__ import annotations

import argparse
import json
import statistics as st
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GROUPS = {"G1": "1 sentence-1 answer + 2 agree only with evidence", "G2": "3 fit expertise + 4 be concrete",
          "G3": "5 length + 6 ≤4 items + 7 prose/steps/tables + 11 end on next action",
          "G4": "8 uncertainty once + 9 keep exact + 10 plain sentences/bold/Korean"}


def rows(folder: str) -> dict:
    d = json.loads((ROOT / "evals/results" / folder / "summary.json").read_text())
    return {(r["id"], r["condition"]): r for r in d["rows"]}


def full_card() -> dict:
    out = {}
    for p in sorted((ROOT / "evals/results").glob("2026-11-13-suite-v1*/summary.json")):
        for r in json.loads(p.read_text())["rows"]:
            out[(r["id"], r["condition"])] = r
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    a = ap.parse_args()
    F = full_card()
    lines = ["# Card ablation results (V3)", "",
             "Each group's lines were removed from the card and the 15-prompt V1a subset was re-run (Sonnet, card proxy, "
             "1 sample). Δ = ablated − full card, per prompt, on the same prompts. Noise, measured from 36 repeat-sample pairs "
             "of the same prompts: SD of a single-prompt difference is 4.7 points and 25 words, so the SE of a 15-prompt mean "
             "difference is about 1.2 points and 7 words. A Δ inside ±2.4 points or ±14 words is not a measurable effect. "
             "These prompts are general; rules aimed at specific situations (math in sentence 1, false premises, Korean speech "
             "level, invented confidence) were measured by their own evals and must be judged there too.", "",
             "| Group removed | n | Δ Brain Score | Δ words | Δ thinking tokens | answer-first fails | question-check fails (ablated vs full) | checks that fire more without the group |",
             "|---|---:|---:|---:|---:|---:|---|---|"]
    for g, desc in GROUPS.items():
        folder = next((p.parent.name for p in sorted((ROOT / "evals/results").glob(f"*-v3-{g}/summary.json"))), None)
        if not folder:
            lines.append(f"| {g}: {desc} | — | not run yet | | | | | |")
            continue
        A = rows(folder)
        ids = sorted(i for (i, c) in A if c == "brainres" and (i, "brainres") in F)
        ds = [A[(i, "brainres")]["score"] - F[(i, "brainres")]["score"] for i in ids]
        dw = [A[(i, "brainres")]["words"] - F[(i, "brainres")]["words"] for i in ids]
        dt = [A[(i, "brainres")].get("thinking_tokens", 0) - F[(i, "brainres")].get("thinking_tokens", 0) for i in ids]
        af = sum(not A[(i, "brainres")]["answer_first"] for i in ids)
        qa = Counter(c for i in ids for c in A[(i, "brainres")].get("question_checks", []))
        qf = Counter(c for i in ids for c in F[(i, "brainres")].get("question_checks", []))
        ca = Counter(c for i in ids for c in A[(i, "brainres")]["checks"])
        cf = Counter(c for i in ids for c in F[(i, "brainres")]["checks"])
        more = ", ".join(f"{k} {cf[k]}→{v}" for k, v in ca.most_common() if v > cf[k]) or "none"
        q = ", ".join(f"{k} {qf[k]}→{qa[k]}" for k in sorted(set(qa) | set(qf))) or "none"
        lines.append(f"| {g}: {desc} | {len(ids)} | {st.mean(ds):+.1f} | {st.mean(dw):+.0f} | {st.mean(dt):+.0f} | {af} | {q} | {more} |")
    text = "\n".join(lines) + "\n"
    print(text)
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
