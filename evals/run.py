#!/usr/bin/env python3
"""brainres eval harness: same questions, with and without brainres, scored by brainlint.

  python3 evals/run.py                 # 12 prompts × 2 conditions = 24 headless calls
  python3 evals/run.py --model sonnet --jobs 6
  python3 evals/run.py --ids 09-ko-concept,10-ko-debug --conditions brainres --samples 2 --tag ko-check

Conditions
  baseline  : `claude -p` with tools and MCP disabled, run from an empty directory
  brainres  : same, plus the plugin's SessionStart card and per-turn reminder appended to
              the system prompt (a proxy for the installed hooks)

Writes evals/results/<date>/<id>.<condition>.md, summary.json and REPORT.md.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import importlib.util
import json
import statistics
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("brainlint", ROOT / "skills/brainres/scripts/brainlint.py")
brainlint = importlib.util.module_from_spec(spec)
sys.modules["brainlint"] = brainlint
spec.loader.exec_module(brainlint)

FRONT = {"preamble", "meta_talk", "buried_answer"}
# Rule 3 length budgets: facts ≤100 words, explanations ≤300 (SKILL.md).
BUDGET = {"yes/no": 100, "misconception": 100}
DEFAULT_BUDGET = 300


def card_sha() -> str:
    import hashlib
    return hashlib.sha256((ROOT / "hooks/core-card.md").read_bytes()).hexdigest()[:12]


def brainres_prompt() -> str:
    card = (ROOT / "hooks/core-card.md").read_text(encoding="utf-8")
    reminder = json.loads(subprocess.run(["bash", str(ROOT / "hooks/brainres-reminder.sh")],
                                         capture_output=True, text=True, check=True).stdout)
    return card + "\n\n" + reminder["hookSpecificOutput"]["additionalContext"]


def ask(q: str, model: str, system: str | None, cwd: str) -> dict:
    args = ["claude", "-p", q, "--model", model, "--output-format", "json", "--tools", "",
            "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}']
    if system:
        args += ["--append-system-prompt", system]
    p = subprocess.run(args, capture_output=True, text=True, cwd=cwd, stdin=subprocess.DEVNULL, timeout=300)
    d = json.loads(p.stdout)
    return {"text": d.get("result", ""), "output_tokens": d.get("usage", {}).get("output_tokens", 0)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--ids", help="comma-separated prompt ids (default: all)")
    ap.add_argument("--conditions", default="baseline,brainres")
    ap.add_argument("--samples", type=int, default=1, help="answers per prompt and condition")
    ap.add_argument("--tag", default="", help="suffix for the results folder")
    a = ap.parse_args()
    prompts = [json.loads(l) for l in (ROOT / "evals/prompts.jsonl").read_text().splitlines() if l.strip()]
    if a.ids:
        wanted = set(a.ids.split(","))
        prompts = [p for p in prompts if p["id"] in wanted]
    conds = a.conditions.split(",")
    out_dir = ROOT / "evals/results" / (dt.date.today().isoformat() + (f"-{a.tag}" if a.tag else ""))
    out_dir.mkdir(parents=True, exist_ok=True)
    system = brainres_prompt()
    jobs = [(p, c, k) for p in prompts for c in conds for k in range(a.samples)]
    rows = []
    with tempfile.TemporaryDirectory() as empty, cf.ThreadPoolExecutor(a.jobs) as ex:
        futs = {ex.submit(ask, p["q"], a.model, system if c == "brainres" else None, empty): (p, c, k) for p, c, k in jobs}
        for f in cf.as_completed(futs):
            p, c, k = futs[f]
            r = f.result()
            rep = brainlint.lint(r["text"])
            checks = sorted({x.check for x in rep.findings})
            suffix = f".{k + 1}" if a.samples > 1 else ""
            (out_dir / f"{p['id']}.{c}{suffix}.md").write_text(f"<!-- Q: {p['q']} -->\n\n{r['text']}\n", encoding="utf-8")
            budget = BUDGET.get(p["type"], DEFAULT_BUDGET)
            rows.append({"id": p["id"], "type": p["type"], "lang": p["lang"], "condition": c, "sample": k + 1, "score": rep.score,
                         "words": rep.words, "output_tokens": r["output_tokens"], "within_budget": rep.words <= budget,
                         "answer_first": not (FRONT & set(checks)), "checks": checks})
            print(f"{p['id']:<16} {c:<9} score={rep.score:>3} words={rep.words:>4} {','.join(checks)}", flush=True)
    rows.sort(key=lambda r: (r["id"], r["condition"], r["sample"]))
    (out_dir / "summary.json").write_text(json.dumps({"model": a.model, "samples": a.samples, "card_sha": card_sha(), "rows": rows},
                                                     ensure_ascii=False, indent=2))

    def agg(cond, key, fn=statistics.mean, rs=None):
        vals = [r[key] for r in (rs or rows) if r["condition"] == cond]
        return fn(vals) if vals else float("nan")

    n = len(prompts) * a.samples
    lines = [f"# Eval report ({out_dir.name}, model={a.model}, {len(prompts)} prompts × {a.samples} sample(s))", "",
             "| Metric | " + " | ".join(conds) + " |", "|---|" + "---:|" * len(conds),
             "| Mean Brain Score | " + " | ".join(f"{agg(c, 'score'):.1f}" for c in conds) + " |",
             "| Median words | " + " | ".join(f"{agg(c, 'words', statistics.median):.0f}" for c in conds) + " |",
             "| Mean output tokens | " + " | ".join(f"{agg(c, 'output_tokens'):.0f}" for c in conds) + " |",
             "| No preamble / buried answer | " + " | ".join(
                 f"{sum(r['answer_first'] for r in rows if r['condition'] == c)}/{n}" for c in conds) + " |",
             "", "| Prompt | Type | " + " | ".join(f"{c} score" for c in conds) + " | "
             + " | ".join(f"{c} words" for c in conds) + " |", "|---|---|" + "---:|" * (2 * len(conds))]
    for p in prompts:
        rs = [r for r in rows if r["id"] == p["id"]]
        lines.append(f"| {p['id']} | {p['type']} | " + " | ".join(f"{agg(c, 'score', rs=rs):.0f}" for c in conds)
                     + " | " + " | ".join(f"{agg(c, 'words', rs=rs):.0f}" for c in conds) + " |")
    (out_dir / "REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
