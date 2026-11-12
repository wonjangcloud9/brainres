#!/usr/bin/env python3
"""LR-01 risk check (B31): on error-prone prompts, does brainres hide the reasoning a reader
needs to catch a wrong answer? Runs each prompt with and without the brainres card and scores
correctness (sentence-1 verdict vs known answer) and whether a reason appears in the first two
sentences.

  python3 evals/tricky.py --model haiku
  python3 evals/tricky.py --rescore evals/results/<date>-tricky-haiku   # no new calls
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import json
import re
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "evals"))
import run  # noqa: E402  (reuses ask() and the brainres prompt)

REASONING = re.compile(r"\b(because|since|so|therefore|thus|which means|that means)\b|=|때문|그래서|따라서|이므로|^\s*\d+[.)]\s", re.I | re.M)


SET = "tricky.jsonl"


def load_items() -> list[dict]:
    return [json.loads(l) for l in (ROOT / "evals" / SET).read_text().splitlines() if l.strip()]


def classify(text: str, item: dict) -> dict:
    # Judge the verdict from sentence 1 only: explanations often mention the tempting wrong answer
    # ("not $0.10"), which made a whole-text regex mark correct answers wrong (found by hand, B31).
    body = [l for l in text.splitlines() if l.strip() and not l.startswith("<!--")]
    sents = re.split(r"(?<=[.!?。])\s+", " ".join(body).replace("**", ""))
    first, first_two = (sents[0] if sents else ""), " ".join(sents[:2])
    region = first
    if item.get("check") == "first_or_last":  # multi-step problems: answer may come first (brainres) or last (default)
        region = first + " " + " ".join(body[-3:]).replace("**", "")
    correct = bool(re.search(item["expect"], region, re.I)) and not re.search(item["wrong"], first, re.I)
    return {"correct": correct, "reason_in_first_two": bool(REASONING.search(first_two)),
            "reasoning_markers": len(REASONING.findall(text)), "words": len(text.split())}


def report(rows: list[dict]) -> None:
    for c in ("baseline", "brainres"):
        rs = [r for r in rows if r["condition"] == c]
        wrong = [r for r in rs if not r["correct"]]
        print(f"{c:<9} correct {sum(r['correct'] for r in rs)}/{len(rs)} · reason in first 2 sentences "
              f"{sum(r['reason_in_first_two'] for r in rs)}/{len(rs)} · wrong answers {len(wrong)}"
              f" (with a visible reason: {sum(r['reason_in_first_two'] for r in wrong)})"
              f" · median words {sorted(r['words'] for r in rs)[len(rs) // 2]}")


def rescore(folder: Path) -> int:
    items = {it["id"]: it for it in load_items()}
    rows = []
    for f in sorted(folder.glob("*.md")):
        iid, cond = f.stem.rsplit(".", 1)
        rows.append({"id": iid, "condition": cond, **classify(f.read_text(encoding="utf-8"), items[iid])})
    summary = json.loads((folder / "summary.json").read_text())
    summary["rows"] = rows
    (folder / "summary.json").write_text(json.dumps(summary, indent=2))
    report(rows)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="haiku")
    ap.add_argument("--rescore", help="re-score an existing results folder without new calls")
    ap.add_argument("--set", default="tricky.jsonl", help="prompt file in evals/ (tricky.jsonl, tricky2.jsonl)")
    a = ap.parse_args()
    global SET
    SET = a.set
    if a.rescore:
        return rescore(Path(a.rescore))
    items = load_items()
    system = run.brainres_prompt()
    out_dir = ROOT / "evals/results" / f"{dt.date.today().isoformat()}-{Path(a.set).stem}-{a.model}"
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    with tempfile.TemporaryDirectory() as empty, cf.ThreadPoolExecutor(6) as ex:
        futs = {ex.submit(run.ask, it["q"], a.model, system if c == "brainres" else None, empty): (it, c)
                for it in items for c in ("baseline", "brainres")}
        for f in cf.as_completed(futs):
            it, c = futs[f]
            text = f.result()["text"]
            (out_dir / f"{it['id']}.{c}.md").write_text(f"<!-- Q: {it['q']} -->\n\n{text}\n", encoding="utf-8")
            rows.append({"id": it["id"], "condition": c, **classify(text, it)})
    rows.sort(key=lambda r: (r["id"], r["condition"]))
    (out_dir / "summary.json").write_text(json.dumps({"model": a.model, "card_sha": run.card_sha(), "rows": rows}, indent=2))
    report(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
