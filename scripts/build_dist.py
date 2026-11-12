#!/usr/bin/env python3
"""Build portable brainres artifacts into dist/ (deterministic output).

  dist/system-prompt.md      paste into any LLM's system prompt / custom instructions
  dist/AGENTS.md             drop into a repo for agents that read AGENTS.md (Codex, etc.)
  dist/cursor/brainres.mdc   Cursor project rule (always applied)
  dist/brainres-skill.zip    upload to claude.ai / Claude desktop (Customize → Skills)
  output-styles/brainres.md  opt-in Claude Code output style shipped with the plugin (/output-style)
  bench/index.html           human comprehension benchmark page (items embedded from bench/items/)
  playground/index.html      Brain Score playground (runs brainlint.py itself in the browser via Pyodide)

Usage: python3 scripts/build_dist.py [--check]
  --check  rebuild in memory and exit 1 if any generated file is stale (used by validate.sh)
"""
from __future__ import annotations

import io
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
SKILL_DIR = ROOT / "skills" / "brainres"
REPO = "https://github.com/wonjangcloud9/brainres"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)  # zip entries get a fixed mtime so builds are reproducible


def card() -> str:
    text = (ROOT / "hooks" / "core-card.md").read_text(encoding="utf-8").strip()
    # Outside Claude Code there is no skill to hand off to; point at the repo instead.
    lines = [l for l in text.splitlines() if not l.startswith("For long or high-stakes answers")]
    return "\n".join(lines).rstrip()


def build() -> dict[str, bytes]:
    c = card()
    out: dict[str, bytes] = {}

    out["dist/system-prompt.md"] = (
        c.replace("brainres is active. ", "")
        + "\n"
    ).encode()

    out["dist/AGENTS.md"] = (
        "# Answer style (brainres)\n\n"
        "When you reply to the user in chat, follow these rules. They are evidence-based; sources: "
        f"{REPO}\n\n" + c.replace("brainres is active. ", "") + "\n"
    ).encode()

    out["dist/cursor/brainres.mdc"] = (
        "---\n"
        "description: brainres — answer style grounded in cognitive science (answer first, chunked, calibrated, honest)\n"
        "globs:\n"
        "alwaysApply: true\n"
        "---\n\n" + c.replace("brainres is active. ", "") + f"\n\nSource and full rules: {REPO}\n"
    ).encode()

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(SKILL_DIR.rglob("*")):
            if f.is_file() and "__pycache__" not in f.parts:
                info = zipfile.ZipInfo(f"brainres/{f.relative_to(SKILL_DIR).as_posix()}", FIXED_TIME)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                z.writestr(info, f.read_bytes())
    out["dist/brainres-skill.zip"] = buf.getvalue()

    # Output style: same rules, selectable with /output-style. keep-coding-instructions
    # keeps Claude Code's engineering behavior; brainres only changes how answers read.
    out["output-styles/brainres.md"] = (
        "---\n"
        "name: brainres\n"
        "description: Answers shaped for how people read — answer first, chunked, calibrated, honest (799 cognitive-science findings)\n"
        "keep-coding-instructions: true\n"
        "---\n\n" + (ROOT / "hooks" / "core-card.md").read_text(encoding="utf-8").replace("brainres is active. ", "").strip() + "\n"
    ).encode()
    out["bench/index.html"] = build_bench()
    out["bench/study2/index.html"] = build_bench2()
    out["playground/index.html"] = build_playground()
    return out


def build_playground() -> bytes:
    import json
    src = (SKILL_DIR / "scripts/brainlint.py").read_text(encoding="utf-8")
    ex = {"en": (ROOT / "examples/01-react-rerender/before.md").read_text(encoding="utf-8"),
          "ko": (ROOT / "examples/02-ko-cache/before.md").read_text(encoding="utf-8"),
          "good": (ROOT / "examples/01-react-rerender/after.md").read_text(encoding="utf-8")}
    page = (ROOT / "playground/template.html").read_text(encoding="utf-8")
    page = page.replace('/*__BRAINLINT__*/""', json.dumps(src).replace("</", "<\\/"))
    page = page.replace("/*__EXAMPLES__*/{}", json.dumps(ex, ensure_ascii=False).replace("</", "<\\/"))
    return page.encode()


def build_bench2() -> bytes:
    """Study 2 (bench/study2/PROTOCOL.md): the same engine, prose vs bullets, balanced within content type."""
    import hashlib, json
    items = []
    for d in sorted((ROOT / "bench/study2/items").iterdir()):
        if not d.is_dir():
            continue
        prose = (d / "prose.md").read_text(encoding="utf-8")
        q = prose.splitlines()[0].removeprefix("<!-- Q: ").removesuffix(" -->")
        strip = lambda t: "\n".join(t.splitlines()[1:]).strip()
        quiz = json.loads((d / "quiz.json").read_text(encoding="utf-8"))
        items.append({"id": d.name, "lang": "en", "content": quiz["content"], "question": q, "prose": strip(prose),
                      "bullets": strip((d / "bullets.md").read_text(encoding="utf-8")), "quiz": quiz})
    sha = hashlib.sha256((ROOT / "bench/study2/items/MANIFEST.sha256").read_bytes()).hexdigest()[:16]
    data = json.dumps({"study": 2, "versions": ["prose", "bullets"], "preference": False, "items": items, "items_sha": sha},
                      ensure_ascii=False).replace("</", "<\\/")
    return (ROOT / "bench/template.html").read_text(encoding="utf-8").replace("/*__DATA__*/null", data).encode()


def build_bench() -> bytes:
    import hashlib, json
    langs = {json.loads(l)["id"]: json.loads(l)["lang"] for l in (ROOT / "evals/prompts.jsonl").read_text().splitlines() if l.strip()}
    items = []
    for d in sorted((ROOT / "bench/items").iterdir()):
        if not d.is_dir():
            continue
        base = (d / "baseline.md").read_text(encoding="utf-8")
        q = base.splitlines()[0].removeprefix("<!-- Q: ").removesuffix(" -->")
        strip = lambda t: "\n".join(t.splitlines()[1:]).strip()
        items.append({"id": d.name, "lang": langs[d.name], "question": q, "baseline": strip(base),
                      "brainres": strip((d / "brainres.md").read_text(encoding="utf-8")),
                      "quiz": json.loads((d / "quiz.json").read_text(encoding="utf-8"))})
    sha = hashlib.sha256((ROOT / "bench/items/MANIFEST.sha256").read_bytes()).hexdigest()[:16]
    data = json.dumps({"items": items, "items_sha": sha}, ensure_ascii=False).replace("</", "<\\/")
    return (ROOT / "bench/template.html").read_text(encoding="utf-8").replace("/*__DATA__*/null", data).encode()


def same(path: Path, data: bytes) -> bool:
    if not path.exists():
        return False
    if path.suffix == ".zip":  # compressed bytes differ across zlib builds; compare the entries instead
        def entries(b: bytes) -> dict:
            with zipfile.ZipFile(io.BytesIO(b)) as z:
                return {n: z.read(n) for n in z.namelist()}
        return entries(path.read_bytes()) == entries(data)
    return path.read_bytes() == data


def main() -> int:
    files = build()
    if "--check" in sys.argv:
        stale = [p for p, data in files.items() if not same(ROOT / p, data)]
        if stale:
            print("stale: " + ", ".join(stale) + " — run python3 scripts/build_dist.py")
            return 1
        print("generated files up to date")
        return 0
    for p, data in files.items():
        target = ROOT / p
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        print(f"wrote {p} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
