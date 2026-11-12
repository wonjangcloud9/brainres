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


def _card_sha() -> str:
    import hashlib
    return hashlib.sha256((ROOT / "hooks/core-card.md").read_bytes()).hexdigest()[:12]


def suite() -> dict:
    return {json.loads(l)["id"]: json.loads(l) for l in (ROOT / "evals/suite.jsonl").read_text().splitlines() if l.strip()}


def pairs() -> dict:
    found = {}
    for p in sorted((ROOT / "evals/results").glob("*/summary.json")):
        d = json.loads(p.read_text())
        if d.get("prompt_set") != "suite.jsonl":
            continue
        if d.get("samples", 1) != 1:  # the V1 suite runs are single-sample; other suite runs (F3) are read separately
            continue
        if d.get("card_sha") and d["card_sha"] != _card_sha():  # skip ablation runs (other cards)
            continue
        for r in d["rows"]:
            if r.get("tool_markup") or r["condition"] not in ("baseline", "brainres"):
                continue
            text = (p.parent / f"{r['id']}.{r['condition']}.md").read_text().split("-->", 1)[1].strip()
            found.setdefault(r["id"], {})[r["condition"]] = text
    return {i: v for i, v in found.items() if "baseline" in v and "brainres" in v}


def load_prompts(name: str) -> dict:
    return {json.loads(l)["id"]: json.loads(l) for l in (ROOT / "evals" / name).read_text().splitlines() if l.strip()}


def phase_checklists(prompts: str = "suite.jsonl", keys_name: str = "checklists.json") -> None:
    S = load_prompts(prompts)
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
    (OUT / keys_name).write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"checklists: {len(out)} prompts, {sum(len(v) for v in out.values())} facts; missing {missing}")


def phase_mark(limit: int | None, marks_name: str = "marks.json", subset: int | None = None) -> None:
    S, P = suite(), pairs()
    keys = json.loads((OUT / "checklists.json").read_text())
    marks_path = OUT / marks_name
    marks = json.loads(marks_path.read_text()) if marks_path.exists() else {}
    pool = sorted(P)
    if subset:  # F4: a fixed random subset for the cross-judge check
        pool = sorted(random.Random(4).sample(pool, subset))
    todo = [i for i in pool if i not in marks and i in keys]
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


def treatment_pairs(folder: str, cond: str) -> dict:
    """F3: answers of one condition from one results folder (any sample), each paired with the suite baseline."""
    base = pairs()
    out = {}
    for f in sorted((ROOT / "evals/results" / folder).glob(f"*.{cond}*.md")):
        stem = f.name[:-3]
        iid, _, k = stem.partition(f".{cond}")
        if iid in base:
            out[f"{iid}#{k.strip('.') or '1'}"] = {"baseline": base[iid]["baseline"], "brainres": f.read_text().split("-->", 1)[1].strip()}
    return out


def phase_mark_treatment(folder: str, cond: str, marks_name: str, limit: int | None) -> None:
    S = suite()
    keys = json.loads((OUT / "checklists.json").read_text())
    P = treatment_pairs(folder, cond)
    marks_path = OUT / marks_name
    marks = json.loads(marks_path.read_text()) if marks_path.exists() else {}
    rng = random.Random(3)
    todo = [k for k in sorted(P) if k not in marks]
    order = {k: rng.random() < 0.5 for k in sorted(P)}
    batches = [todo[i:i + 3] for i in range(0, len(todo), 3)][: limit or None]
    def run(batch):
        parts = []
        for k in batch:
            iid = k.split("#")[0]
            a, b = (P[k]["brainres"], P[k]["baseline"]) if order[k] else (P[k]["baseline"], P[k]["brainres"])
            facts = "\n".join(f"{n + 1}. {x}" for n, x in enumerate(keys[iid]))
            parts.append(f"=== [{k}]\nQUESTION:\n{S[iid]['q']}\n\nKEY FACTS:\n{facts}\n\nANSWER A:\n{a}\n\nANSWER B:\n{b}")
        prompt = ("Grade information coverage. For each item, mark every key fact for Answer A and Answer B: 1 = clearly "
                  "present and correct, 0.5 = partly present or vague, 0 = missing or wrong. Judge content only, not "
                  "length or style. Reply with only a JSON object: {\"<id>\": {\"A\": [scores...], \"B\": [scores...]}}.\n\n"
                  + "\n\n".join(parts))
        return batch, first_json(ask(prompt))
    with cf.ThreadPoolExecutor(6) as ex:
        for batch, res in ex.map(run, batches):
            for k in batch:
                if k in res:
                    A, B = res[k]["A"], res[k]["B"]
                    t, b = (A, B) if order[k] else (B, A)
                    marks[k] = {"brainres": t, "baseline": b, "a_is_brainres": order[k]}
    marks_path.write_text(json.dumps(marks, ensure_ascii=False, indent=2))
    print(f"marked {len(marks)}/{len(P)} answers")


def phase_pair(prompts: str, keys_name: str, a_spec: str, b_spec: str, marks_name: str) -> None:
    """F6: blind-mark two conditions (DIR:COND each, single-sample files) against question-only keys."""
    S = load_prompts(prompts)
    keys = json.loads((OUT / keys_name).read_text())
    (da, ca), (db, cb) = a_spec.split(":"), b_spec.split(":")
    read = lambda d, c, i: (ROOT / "evals/results" / d / f"{i}.{c}.md").read_text().split("-->", 1)[1].strip()
    ids = [i for i in sorted(S) if i in keys]
    rng = random.Random(6)
    order = {i: rng.random() < 0.5 for i in ids}  # True → A shown first is condition A
    def run(batch):
        parts = []
        for i in batch:
            x, y = read(da, ca, i), read(db, cb, i)
            first, second = (x, y) if order[i] else (y, x)
            facts = "\n".join(f"{n + 1}. {f}" for n, f in enumerate(keys[i]))
            parts.append(f"=== [{i}]\nQUESTION:\n{S[i]['q']}\n\nKEY FACTS:\n{facts}\n\nANSWER A:\n{first}\n\nANSWER B:\n{second}")
        prompt = ("Grade information coverage. For each item, mark every key fact for Answer A and Answer B: 1 = clearly "
                  "present and correct, 0.5 = partly present or vague, 0 = missing or wrong. Judge content only, not "
                  "length or style. Reply with only a JSON object: {\"<id>\": {\"A\": [scores...], \"B\": [scores...]}}.\n\n"
                  + "\n\n".join(parts))
        return batch, first_json(ask(prompt))
    marks = {}
    with cf.ThreadPoolExecutor(6) as ex:
        for batch, res in ex.map(run, [ids[k:k + 3] for k in range(0, len(ids), 3)]):
            for i in batch:
                if i in res:
                    A, B = res[i]["A"], res[i]["B"]
                    marks[i] = {ca: A if order[i] else B, cb: B if order[i] else A}
    (OUT / marks_name).write_text(json.dumps(marks, ensure_ascii=False, indent=2))
    cov = lambda v: sum(v) / len(v) if v else 0.0
    print(f"{len(marks)} prompts · coverage {ca} {st.mean(cov(m[ca]) for m in marks.values()):.1%} · {cb} {st.mean(cov(m[cb]) for m in marks.values()):.1%}")


def phase_agree(other: str) -> None:
    """F4: compare two judges' marks on the prompts both marked."""
    A = json.loads((OUT / "marks.json").read_text())
    B = json.loads((OUT / other).read_text())
    common = sorted(set(A) & set(B))
    def cov(v):
        return sum(v) / len(v) if v else 0.0
    same = total = 0
    for i in common:
        for c in ("baseline", "brainres"):
            for x, y in zip(A[i][c], B[i][c]):
                total += 1
                same += x == y
    def delta(M):
        return st.mean(cov(M[i]["brainres"]) - cov(M[i]["baseline"]) for i in common)
    def counts(M):
        d = [cov(M[i]["brainres"]) - cov(M[i]["baseline"]) for i in common]
        return sum(x < 0 for x in d), sum(x == 0 for x in d), sum(x > 0 for x in d)
    ca = [cov(A[i][c]) for i in common for c in ("baseline", "brainres")]
    cb = [cov(B[i][c]) for i in common for c in ("baseline", "brainres")]
    r = st.correlation(ca, cb) if len(set(ca)) > 1 and len(set(cb)) > 1 else float("nan")
    lines = [f"# Cross-judge check (F4): {len(common)} prompts", "",
             "| | Sonnet judge | Opus judge |", "|---|---:|---:|",
             f"| Mean coverage, baseline | {st.mean(cov(A[i]['baseline']) for i in common):.1%} | {st.mean(cov(B[i]['baseline']) for i in common):.1%} |",
             f"| Mean coverage, brainres | {st.mean(cov(A[i]['brainres']) for i in common):.1%} | {st.mean(cov(B[i]['brainres']) for i in common):.1%} |",
             f"| Δ brainres − baseline | {delta(A) * 100:+.1f} pp | {delta(B) * 100:+.1f} pp |",
             f"| Prompts brainres covers less / same / more | {'/'.join(map(str, counts(A)))} | {'/'.join(map(str, counts(B)))} |", "",
             f"Exact agreement on individual fact marks: {same}/{total} ({same / total:.0%}). Correlation of per-answer coverage: r = {r:.2f}."]
    text = "\n".join(lines) + "\n"
    (OUT / "CROSS-JUDGE.md").write_text(text)
    print(text)


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
    ap.add_argument("--phase", choices=["checklists", "mark", "report", "agree", "pair"], required=True)
    ap.add_argument("--prompts", default="suite.jsonl")
    ap.add_argument("--keys", default="checklists.json")
    ap.add_argument("--a", help="pair phase: DIR:COND")
    ap.add_argument("--b", help="pair phase: DIR:COND")
    ap.add_argument("--limit", type=int, help="max judge calls in the mark phase (eval budget)")
    ap.add_argument("--judge", default="sonnet")
    ap.add_argument("--marks", default="marks.json", help="marks file name (F4: marks-opus.json)")
    ap.add_argument("--subset", type=int, help="mark a fixed random subset of N prompts")
    ap.add_argument("--treatment-dir", help="F3: mark this results folder's answers (condition --treatment) vs the suite baseline")
    ap.add_argument("--treatment", default="plugin")
    a = ap.parse_args()
    global JUDGE
    JUDGE = a.judge
    if a.phase == "checklists":
        return phase_checklists(a.prompts, a.keys)
    if a.phase == "pair":
        return phase_pair(a.prompts, a.keys, a.a, a.b, a.marks)
    if a.phase == "mark" and a.treatment_dir:
        return phase_mark_treatment(a.treatment_dir, a.treatment, a.marks, a.limit)
    {"checklists": phase_checklists, "mark": lambda: phase_mark(a.limit, a.marks, a.subset), "report": phase_report,
     "agree": lambda: phase_agree(a.marks)}[a.phase]()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
