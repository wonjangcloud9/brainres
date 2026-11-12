#!/usr/bin/env python3
"""Re-score saved eval answers with the current brainlint (no model calls).

Keeps the previous value as score_before_<tag>. run.py rows: score = lint(text), score_q = lint(text, question).
multiturn rows (have "turn"): score = lint(text, question), as multiturn.py computes it.

  python3 evals/rescore.py --tag k1 2026-11-13-suite-v1a 2026-11-13-f6 ...
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("brainlint", ROOT / "skills/brainres/scripts/brainlint.py")
bl = importlib.util.module_from_spec(spec)
sys.modules["brainlint"] = bl
spec.loader.exec_module(bl)
sys.path.insert(0, str(ROOT / "evals"))


def prompts(name: str) -> dict:
    return {json.loads(l)["id"]: json.loads(l)["q"] for l in (ROOT / "evals" / name).read_text().splitlines() if l.strip()}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", required=True)
    ap.add_argument("folders", nargs="+")
    a = ap.parse_args()
    import multiturn  # noqa: E402  (question text for multi-turn rows)
    for folder in a.folders:
        p = ROOT / "evals/results" / folder / "summary.json"
        d = json.loads(p.read_text())
        Q = prompts(d["prompt_set"]) if d.get("prompt_set") else {}
        changed = 0
        for r in d["rows"]:
            if "turn" in r:
                if "text" not in r:
                    continue
                convs = multiturn.LONG if "long" in folder else multiturn.CONVERSATIONS
                q = r.get("q") or convs[r["lang"]][r["turn"] - 1]
                rep = bl.lint(r["text"], q)
                r.setdefault(f"score_before_{a.tag}", r["score"])
                new = sorted({x.check for x in rep.findings})
                changed += new != r["checks"]
                r["score"], r["checks"] = rep.score, new
                continue
            suf = f".{r['sample']}" if d.get("samples", 1) > 1 else ""
            f = p.parent / f"{r['id']}.{r['condition']}{suf}.md"
            text = f.read_text().split("-->", 1)[1].strip()
            rep = bl.lint(text)
            r.setdefault(f"score_before_{a.tag}", r["score"])
            new = sorted({x.check for x in rep.findings})
            changed += new != r["checks"]
            r["score"], r["checks"] = rep.score, new
            if r["id"] in Q:
                r["score_q"] = bl.lint(text, Q[r["id"]]).score
        d.setdefault("rescored_by", []).append(a.tag)
        p.write_text(json.dumps(d, ensure_ascii=False, indent=2))
        print(f"{folder}: {changed} rows changed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
