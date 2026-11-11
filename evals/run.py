#!/usr/bin/env python3
"""brainres eval harness: same questions, with and without brainres, scored by brainlint.

  python3 evals/run.py                 # 12 prompts × 2 conditions = 24 headless calls
  python3 evals/run.py --model sonnet --jobs 6

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
    a = ap.parse_args()
    prompts = [json.loads(l) for l in (ROOT / "evals/prompts.jsonl").read_text().splitlines() if l.strip()]
    out_dir = ROOT / "evals/results" / dt.date.today().isoformat()
    out_dir.mkdir(parents=True, exist_ok=True)
    system = brainres_prompt()
    jobs = [(p, cond) for p in prompts for cond in ("baseline", "brainres")]
    rows = []
    with tempfile.TemporaryDirectory() as empty, cf.ThreadPoolExecutor(a.jobs) as ex:
        futs = {ex.submit(ask, p["q"], a.model, system if c == "brainres" else None, empty): (p, c) for p, c in jobs}
        for f in cf.as_completed(futs):
            p, c = futs[f]
            r = f.result()
            rep = brainlint.lint(r["text"])
            checks = sorted({x.check for x in rep.findings})
            (out_dir / f"{p['id']}.{c}.md").write_text(f"<!-- Q: {p['q']} -->\n\n{r['text']}\n", encoding="utf-8")
            rows.append({"id": p["id"], "type": p["type"], "lang": p["lang"], "condition": c, "score": rep.score,
                         "words": rep.words, "output_tokens": r["output_tokens"],
                         "answer_first": not (FRONT & set(checks)), "checks": checks})
            print(f"{p['id']:<16} {c:<9} score={rep.score:>3} words={rep.words:>4} {','.join(checks)}", flush=True)
    rows.sort(key=lambda r: (r["id"], r["condition"]))
    (out_dir / "summary.json").write_text(json.dumps({"model": a.model, "rows": rows}, ensure_ascii=False, indent=2))

    def agg(cond, key, fn=statistics.mean):
        return fn([r[key] for r in rows if r["condition"] == cond])
    lines = [f"# Eval report ({out_dir.name}, model={a.model}, n={len(prompts)} prompts)", "",
             "| Metric | baseline | brainres |", "|---|---:|---:|",
             f"| Mean Brain Score | {agg('baseline','score'):.1f} | {agg('brainres','score'):.1f} |",
             f"| Median words | {agg('baseline','words',statistics.median):.0f} | {agg('brainres','words',statistics.median):.0f} |",
             f"| Mean output tokens | {agg('baseline','output_tokens'):.0f} | {agg('brainres','output_tokens'):.0f} |",
             f"| No preamble / buried answer | {sum(r['answer_first'] for r in rows if r['condition']=='baseline')}/{len(prompts)} | {sum(r['answer_first'] for r in rows if r['condition']=='brainres')}/{len(prompts)} |",
             "", "| Prompt | Type | baseline | brainres | baseline words | brainres words |", "|---|---|---:|---:|---:|---:|"]
    by = {(r["id"], r["condition"]): r for r in rows}
    for p in prompts:
        b, x = by[(p["id"], "baseline")], by[(p["id"], "brainres")]
        lines.append(f"| {p['id']} | {p['type']} | {b['score']} | {x['score']} | {b['words']} | {x['words']} |")
    (out_dir / "REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:9]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
