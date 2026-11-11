#!/usr/bin/env python3
"""Build portable brainres artifacts into dist/ (deterministic output).

  dist/system-prompt.md      paste into any LLM's system prompt / custom instructions
  dist/AGENTS.md             drop into a repo for agents that read AGENTS.md (Codex, etc.)
  dist/cursor/brainres.mdc   Cursor project rule (always applied)
  dist/brainres-skill.zip    upload to claude.ai / Claude desktop (Customize → Skills)
  output-styles/brainres.md  opt-in Claude Code output style shipped with the plugin (/output-style)

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
        "description: Answers shaped for how people read — answer first, chunked, calibrated, honest (725 cognitive-science findings)\n"
        "keep-coding-instructions: true\n"
        "---\n\n" + (ROOT / "hooks" / "core-card.md").read_text(encoding="utf-8").replace("brainres is active. ", "").strip() + "\n"
    ).encode()
    return out


def main() -> int:
    files = build()
    if "--check" in sys.argv:
        stale = [p for p, data in files.items() if not (ROOT / p).exists() or (ROOT / p).read_bytes() != data]
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
