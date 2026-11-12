#!/usr/bin/env python3
"""V2: information coverage — do shorter brainres answers drop facts a good answer needs?

Phase 1 (checklists): a judge writes 3–6 essential facts per suite prompt from the QUESTION ALONE
(batches of 20, before it sees any answer). The checklists are frozen in checklists.json.
Phase 2 (mark): the judge sees a question, its frozen checklist and two answers labelled A/B in a
seeded random order (it is never told which is brainres), and marks each fact 1 / 0.5 / 0 per answer.
Phase 3 (report): per-prompt coverage = mean fact score; paired brainres − baseline with a 95% CI.

  python3 evals/coverage_judge.py --phase checklists
  python3 evals/coverage_judge.py --phase mark [--limit 26]
  python3 evals/coverage_judge.py --phase report
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import random
import re
import statistics as st
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "evals/results/suite-coverage"
JUDGE = "sonnet"


def ask(prompt: str) -> str:
    p = subprocess.run(["claude", "-p", prompt, "--model", JUDGE, "--output-format", "json", "--tools", "",
                        "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}'],
                       capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=600, cwd="/tmp")
    return json.loads(p.stdout).get("result", "")


def first_json(text: str):
    m = re.search(r"\{.*\}", text, re.S)
    return json.loads(m.group(0))


def suite() -> dict:
    return {json.loads(l)["id"]: json.loads(l) for l in (ROOT / "evals/suite.jsonl").read_text().splitlines() if l.strip()}


def pairs() -> dict:
    found = {}
    for p in sorted((ROOT / "evals/results").glob("*/summary.json")):
        d = json.loads(p.read_text())
        if d.get("prompt_set") != "suite.jsonl":
            continue
        for r in d["rows"]:
            if r.get("tool_markup"):
                continue
            text = (p.parent / f"{r['id']}.{r['condition']}.md").read_text().split("-->", 1)[1].strip()
            found.setdefault(r["id"], {})[r["condition"]] = text
    return {i: v for i, v in found.items() if "baseline" in v and "brainres" in v}


def phase_checklists() -> None:
    S = suite()
    ids = sorted(S)
    out = {}
    batches = [ids[i:i + 20] for i in range(0, len(ids), 20)]
    def run(batch):
        qs = "\n\n".join(f"[{i}]\n{S[i]['q']}" for i in batch)
        prompt = ("You are preparing a grading key. For each question below, list the 3 to 6 essential facts, steps or "
                  "points that a complete, correct answer must contain for this asker. Base it only on the question. "
                  "Each item is one short, checkable statement. Reply with only a JSON object mapping each id to a list "
                  "of strings.\n\n" + qs)
        return first_json(ask(prompt))
    with cf.ThreadPoolExecutor(4) as ex:
        for res in ex.map(run, batches):
            out.update(res)
    missing = [i for i in ids if i not in out]
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "checklists.json").write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"checklists: {len(out)} prompts, {sum(len(v) for v in out.values())} facts; missing {missing}")


def phase_mark(limit: int | None) -> None:
    S, P = suite(), pairs()
    keys = json.loads((OUT / "checklists.json").read_text())
    marks_path = OUT / "marks.json"
    marks = json.loads(marks_path.read_text()) if marks_path.exists() else {}
    todo = [i for i in sorted(P) if i not in marks and i in keys]
    rng = random.Random(20261113)
    order = {i: rng.random() < 0.5 for i in sorted(P)}  # True → A is brainres
    batches = [todo[i:i + 3] for i in range(0, len(todo), 3)]
    if limit:
        batches = batches[:limit]
    def run(batch):
        parts = []
        for i in batch:
            a, b = (P[i]["brainres"], P[i]["baseline"]) if order[i] else (P[i]["baseline"], P[i]["brainres"])
            facts = "\n".join(f"{k + 1}. {f}" for k, f in enumerate(keys[i]))
            parts.append(f"=== [{i}]\nQUESTION:\n{S[i]['q']}\n\nKEY FACTS:\n{facts}\n\nANSWER A:\n{a}\n\nANSWER B:\n{b}")
        prompt = ("Grade information coverage. For each item, mark every key fact for Answer A and Answer B: 1 = clearly "
                  "present and correct, 0.5 = partly present or vague, 0 = missing or wrong. Judge content only, not "
                  "length or style. Reply with only a JSON object: {\"<id>\": {\"A\": [scores...], \"B\": [scores...]}}.\n\n"
                  + "\n\n".join(parts))
        return batch, first_json(ask(prompt))
    with cf.ThreadPoolExecutor(6) as ex:
        for batch, res in ex.map(run, batches):
            for i in batch:
                if i not in res:
                    continue
                A, B = res[i]["A"], res[i]["B"]
                bres, base = (A, B) if order[i] else (B, A)
                marks[i] = {"brainres": bres, "baseline": base, "a_is_brainres": order[i]}
    marks_path.write_text(json.dumps(marks, ensure_ascii=False, indent=2))
    print(f"marked {len(marks)}/{len(P)} prompts")


def phase_report() -> None:
    S = suite()
    marks = json.loads((OUT / "marks.json").read_text())
    def cov(v):
        return sum(v) / len(v) if v else 0.0
    d = [cov(m["brainres"]) - cov(m["baseline"]) for m in marks.values()]
    b = [cov(m["baseline"]) for m in marks.values()]
    s = [cov(m["brainres"]) for m in marks.values()]
    n = len(d)
    sd = st.stdev(d) if n > 1 else 0.0
    t = {10: 2.23, 20: 2.09, 30: 2.04, 40: 2.02, 60: 2.0, 80: 1.99}
    tc = next(v for k, v in sorted(t.items()) if n <= k) if n <= 80 else 1.99
    half = tc * sd / n ** 0.5
    lines = [f"# Information coverage (V2): {n} paired prompts", "",
             "Each prompt's key facts were written by the judge from the question alone, before it saw any answer. Each fact was "
             "then marked 1 / 0.5 / 0 per answer, with the two answers blinded and order-randomized.", "",
             "| | baseline | brainres | brainres − baseline (95% CI) |", "|---|---:|---:|---|",
             f"| Mean coverage | {st.mean(b):.1%} | {st.mean(s):.1%} | {st.mean(d) * 100:+.1f} pp ({(st.mean(d) - half) * 100:+.1f} to {(st.mean(d) + half) * 100:+.1f}) |",
             f"| Prompts where brainres covers less / same / more | | | {sum(x < 0 for x in d)} / {sum(x == 0 for x in d)} / {sum(x > 0 for x in d)} |", "",
             "## By type", "", "| Type | n | baseline | brainres | Δ pp |", "|---|---:|---:|---:|---:|"]
    by = {}
    for i, m in marks.items():
        by.setdefault(S[i]["type"], []).append(m)
    for typ, ms in sorted(by.items()):
        bb = st.mean(cov(m["baseline"]) for m in ms); ss = st.mean(cov(m["brainres"]) for m in ms)
        lines.append(f"| {typ} | {len(ms)} | {bb:.0%} | {ss:.0%} | {(ss - bb) * 100:+.0f} |")
    order_bias = st.mean(cov(m["brainres"] if m["a_is_brainres"] else m["baseline"]) for m in marks.values()) - \
        st.mean(cov(m["baseline"] if m["a_is_brainres"] else m["brainres"]) for m in marks.values())
    lines += ["", f"Position check: answers shown as A scored {order_bias * 100:+.1f} pp vs B on average."]
    text = "\n".join(lines) + "\n"
    (OUT / "REPORT.md").write_text(text)
    print(text)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", choices=["checklists", "mark", "report"], required=True)
    ap.add_argument("--limit", type=int, help="max judge calls in the mark phase (eval budget)")
    a = ap.parse_args()
    {"checklists": phase_checklists, "mark": lambda: phase_mark(a.limit), "report": phase_report}[a.phase]()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
