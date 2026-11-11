# Loop log

One line per autonomous iteration: `date · item · change · commit`.

- 2026-11-12 01:11 · B01–B04 · v0.1 initial release (skill, hook, brainlint, research, README) · 9c421f9
- 2026-11-12 01:12 · B05 · per-turn reminder hook (UserPromptSubmit, ~60 tokens) · e6e153f
- 2026-11-12 01:19 · C00 · coverage ledger + ratchet: 50/87 applicable findings applied (57.5%); 6 domain research agents launched
- 2026-11-12 01:21 · C02+C03 · situation router + 9 reference files; coverage 50→87/87 (100%) for the original catalog
- 2026-11-12 01:22 · B07 · Korean README (README.ko.md) with Korean before/after hero
- 2026-11-12 01:38 · C01 · 6 domain catalogs ingested: 725 findings (596 applicable, 129 excluded with reason); applied 87/596
- 2026-11-12 01:43 · C01–C06 · full coverage: 596/596 applicable findings applied (725 reviewed); +4 reference files; honesty rules in core card
- 2026-11-12 01:44 · B14 · launch drafts (Show HN, X thread, GeekNews, r/ClaudeAI) in launch/
- 2026-11-12 02:00 · B25 · measured token cost (card 631, reminder 79, skill 3,893; Sonnet, MCP off, median of 3); README/launch numbers corrected; ~31 headless calls used (1 over budget while debugging the method)
- 2026-11-12 02:18 · C10 · core card v2 by RICE ranking: 631 → 418 tokens (measured, 6 headless calls)
- 2026-11-12 02:37 · B19 · portable builds (system prompt, AGENTS.md, Cursor rule, claude.ai zip) + stale-dist check
- 2026-11-12 04:13 · B12 · brainlint golden/unit tests (15), wired into validate.sh; mutation check passed; fixed stale-.pyc masking
- 2026-11-12 04:18 · B06 · brainlint Korean 어절 thresholds (avg ≤12, long >20) + headings excluded from sentences; KO before 45→41; 18 tests; backlog tidy (B17/B18 superseded)
- 2026-11-12 04:37 · B08 · opt-in output style generated from the core card (/output-style → brainres)
- 2026-11-12 04:59 · B22 · social preview image + brainlint --badge; dogfooding fixed table false-positive and KO README (79→96); badge freshness check
- 2026-11-12 05:18 · B26 · SKILL.md citations moved to references/rule-sources.md: 3,893 → 3,309 tokens (measured, 6 calls); coverage 596/596
