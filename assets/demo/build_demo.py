#!/usr/bin/env python3
"""D7: build assets/demo.gif from REAL saved suite answers (no model calls).

Renders 3 scenes (question → default answer → brainres answer beside it) with headless Chrome, then
stitches them into a looping GIF with ffmpeg. Source answers: evals/results/2026-11-13-suite-v1*/s153-multi.*.md
"""
from __future__ import annotations

import html
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "assets/demo"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PID = "s153-multi"


def md(text: str) -> str:
    """Tiny Markdown → HTML for the constructs these answers use (bold, italics, lists, tables, paragraphs)."""
    inline = lambda s: re.sub(r"\*(.+?)\*", r"<i>\1</i>", re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", html.escape(s)))
    out, lines, i = [], text.strip().splitlines(), 0
    while i < len(lines):
        l = lines[i]
        if l.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                if not re.match(r"^\|[-|: ]+\|$", lines[i]):
                    rows.append([c.strip() for c in lines[i].strip("|").split("|")])
                i += 1
            out.append("<table>" + "".join("<tr>" + "".join(f"<{'th' if k == 0 else 'td'}>{inline(c)}</{'th' if k == 0 else 'td'}>" for c in r) + "</tr>" for k, r in enumerate(rows)) + "</table>")
            continue
        if l.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(lines[i][2:]); i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
            continue
        if l.strip():
            out.append(f"<p>{inline(l)}</p>")
        i += 1
    return "\n".join(out)


def answer(cond: str) -> tuple[str, dict]:
    for p in sorted((ROOT / "evals/results").glob("2026-11-13-suite-v1*/summary.json")):
        d = json.loads(p.read_text())
        row = next((r for r in d["rows"] if r["id"] == PID and r["condition"] == cond), None)
        if row:
            t = (p.parent / f"{PID}.{cond}.md").read_text()
            return t.split("-->", 1)[1].strip(), row
    raise SystemExit(f"{PID} {cond} not found")


CSS = """
html,body{margin:0;background:#0f1117;color:#e9e7e3;font:14px/1.45 -apple-system,"Segoe UI",Helvetica,Arial,sans-serif}
.wrap{width:1000px;height:640px;box-sizing:border-box;padding:22px 26px;display:flex;flex-direction:column;gap:14px}
.q{background:#1c1e25;border:1px solid #2c2f39;border-radius:10px;padding:12px 16px;font-size:17px}
.q span{color:#a19d96;font-size:13px;display:block;margin-bottom:2px}
.cols{display:flex;gap:16px;flex:1;min-height:0}
.col{flex:1;background:#151821;border:1px solid #2c2f39;border-radius:10px;padding:12px 14px;overflow:hidden;display:flex;flex-direction:column}
.col h3{margin:0 0 8px;font-size:14px;color:#a19d96;font-weight:600}
.col.br h3{color:#7ee2a8}
.body{font-size:10.6px;line-height:1.38;flex:1;overflow:hidden;position:relative}
.base .body:after{content:"… continues";position:absolute;left:0;right:0;bottom:0;height:34px;padding-top:16px;box-sizing:border-box;text-align:right;font-size:10px;color:#a19d96;background:linear-gradient(transparent,#151821 55%)}
.body p{margin:0 0 5px}.body ul{margin:0 0 5px;padding-left:16px}.body li{margin:0 0 2px}
.body table{border-collapse:collapse;margin:2px 0 6px;width:100%}.body th,.body td{border:1px solid #2c2f39;padding:2px 5px;text-align:left}
.stat{margin-top:8px;font-size:15px;font-weight:700}.base .stat{color:#f0a36b}.br .stat{color:#7ee2a8}
.hide{visibility:hidden}
.foot{font-size:11px;color:#a19d96}
"""


def page(scene: int, q: str, base: str, brn: str, rb: dict, rs: dict) -> str:
    left = "" if scene >= 2 else " hide"
    right = "" if scene >= 3 else " hide"
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="wrap">
<div class="q"><span>Same question, real answers (Sonnet)</span>{html.escape(q)}</div>
<div class="cols">
 <div class="col base{left}"><h3>Default Claude</h3><div class="body">{md(base)}</div><div class="stat">{rb['words']} words · Brain Score {rb['score']}</div></div>
 <div class="col br{right}"><h3>With brainres</h3><div class="body">{md(brn)}</div><div class="stat">{rs['words']} words · Brain Score {rs['score']}</div></div>
</div>
<div class="foot">Prompt s153 from the 80-prompt suite; full answers in evals/results/. Across the suite (78 pairs): −29% words, Brain Score +4.6.</div>
</div></body></html>"""


def main() -> int:
    q = json.loads(next(l for l in (ROOT / "evals/suite.jsonl").read_text().splitlines() if f'"{PID}"' in l))["q"]
    base, rb = answer("baseline")
    brn, rs = answer("brainres")
    frames = []
    for scene in (1, 2, 3):
        h = OUT / f"scene{scene}.html"
        h.write_text(page(scene, q, base, brn, rb, rs), encoding="utf-8")
        png = OUT / f"scene{scene}.png"
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1000,640",
                        f"--screenshot={png}", f"file://{h}"], check=True, capture_output=True)
        frames.append(png)
    lst = OUT / "frames.txt"
    durations = (1.6, 2.6, 5.5)
    lst.write_text("".join(f"file '{f.name}'\nduration {d}\n" for f, d in zip(frames, durations)) + f"file '{frames[-1].name}'\n")
    gif = ROOT / "assets/demo.gif"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-vf",
                    "fps=10,scale=1000:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=64[p];[b][p]paletteuse=dither=none",
                    "-loop", "0", str(gif)], check=True, cwd=OUT)
    for f in frames + [lst] + [OUT / f"scene{s}.html" for s in (1, 2, 3)]:
        f.unlink()
    print(f"{gif.relative_to(ROOT)}: {gif.stat().st_size // 1024} KB · {rb['words']} → {rs['words']} words · {rb['score']} → {rs['score']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
