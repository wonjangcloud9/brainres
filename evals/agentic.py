#!/usr/bin/env python3
"""B32: does the brainres plugin change agentic coding outcomes in Claude Code?

Each task in evals/agentic/<task>/ has a small module and failing unittest tests. For each task and
condition, the task is copied to a temp dir and Claude Code is asked to make the tests pass:

  baseline : claude -p, tools Read Edit Write Glob Grep (no Bash), acceptEdits
  plugin   : same, plus --plugin-dir <repo> (brainres hooks + skill)

The harness, not the model, then runs the tests. Recorded per run: tests pass, test files modified,
lines changed in source, words in Claude's final message, turns.

  python3 evals/agentic.py --model sonnet
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import difflib
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TASKS = ROOT / "evals/agentic"
PROMPT = "Make the tests in this directory pass. Do not change the test files."


def snapshot(d: Path) -> dict[str, str]:
    return {p.name: p.read_text(encoding="utf-8") for p in sorted(d.glob("*.py"))}


def run_one(task: Path, cond: str, model: str) -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / task.name
        shutil.copytree(task, work)
        before = snapshot(work)
        args = ["claude", "-p", PROMPT, "--model", model, "--output-format", "json",
                "--tools", "Read Edit Write Glob Grep", "--permission-mode", "acceptEdits",
                "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}']
        if cond == "plugin":
            args += ["--plugin-dir", str(ROOT)]
        p = subprocess.run(args, cwd=work, capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=600)
        d = json.loads(p.stdout)
        after = snapshot(work)
        t = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", ".", "-q"], cwd=work,
                           capture_output=True, text=True, timeout=60, env={"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin"})
        tests_modified = any(before[n] != after.get(n) for n in before if n.startswith("test_"))
        changed = sum(1 for n in before if not n.startswith("test_")
                      for l in difflib.unified_diff(before[n].splitlines(), after.get(n, "").splitlines(), lineterm="")
                      if l[:1] in "+-" and not l.startswith(("+++", "---")))
        return {"task": task.name, "condition": cond, "pass": t.returncode == 0, "tests_modified": tests_modified,
                "lines_changed": changed, "final_words": len(d.get("result", "").split()), "turns": d.get("num_turns"),
                "final_message": d.get("result", "")}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="sonnet")
    a = ap.parse_args()
    tasks = sorted(p for p in TASKS.iterdir() if p.is_dir())
    rows = []
    with cf.ThreadPoolExecutor(4) as ex:
        futs = [ex.submit(run_one, t, c, a.model) for t in tasks for c in ("baseline", "plugin")]
        for f in cf.as_completed(futs):
            r = f.result(); rows.append(r)
            print(f"{r['task']:<18} {r['condition']:<8} pass={r['pass']} tests_modified={r['tests_modified']} "
                  f"lines={r['lines_changed']} final_words={r['final_words']} turns={r['turns']}", flush=True)
    rows.sort(key=lambda r: (r["task"], r["condition"]))
    out = ROOT / "evals/results" / f"{dt.date.today().isoformat()}-agentic-{a.model}"
    out.mkdir(parents=True, exist_ok=True)
    (out / "summary.json").write_text(json.dumps({"model": a.model, "rows": rows}, ensure_ascii=False, indent=2))
    for c in ("baseline", "plugin"):
        rs = [r for r in rows if r["condition"] == c]
        fw = sorted(r["final_words"] for r in rs)
        print(f"{c:<8} pass {sum(r['pass'] for r in rs)}/{len(rs)} · tests modified {sum(r['tests_modified'] for r in rs)}"
              f" · median lines changed {sorted(r['lines_changed'] for r in rs)[len(rs)//2]} · median final-message words {fw[len(fw)//2]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
