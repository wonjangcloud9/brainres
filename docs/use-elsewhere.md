# Using brainres outside Claude Code

In Claude Code, install the plugin: it's the only route with the hooks. Everywhere else you paste or upload the same rule card. The card is the same 11 rules measured on the 80-prompt suite, but these routes themselves haven't been measured.

| Where | Always on? | What to use |
|---|---|---|
| claude.ai Project | Yes, inside that project | Paste [`dist/system-prompt.md`](../dist/system-prompt.md) into the project instructions |
| claude.ai Skill | Only when Claude decides it's relevant | Upload [`dist/brainres-skill.zip`](../dist/brainres-skill.zip) |
| ChatGPT | Yes | Paste `dist/system-prompt.md` into Custom instructions, or a GPT's instructions |
| Gemini | Yes, inside that Gem | Paste `dist/system-prompt.md` into a Gem's instructions |
| Codex, Cursor, other agents | Yes | See the README's "Use it anywhere" table (`AGENTS.md`, Cursor rule, `npx skills add`) |

## claude.ai and Claude desktop

**For everyday use, add it to a Project:**
1. Open or create a Project.
2. Open its instructions.
3. Paste the contents of `dist/system-prompt.md` (1,188 characters).

Every chat in that project then gets the card.

**As a Skill** (Pro, Max, Team or Enterprise; code execution must be on):
1. Go to Customize → Skills. Older versions put it at Settings → Capabilities.
2. Upload `dist/brainres-skill.zip`. It contains the folder `brainres/` with `SKILL.md` and the reference files.

A skill loads only when Claude judges it relevant. In our Claude Code tests that happened in 1 of 24 answers, so don't rely on it for every reply. It's useful when you ask for it by name: "use brainres to rewrite this", "brainres score this", "brainres scan mode".

## ChatGPT

- **Custom instructions:** go to Settings → Personalization → Custom instructions and paste `dist/system-prompt.md`. At 1,188 characters it fits the 1,500-character field on every plan. Paid plans were reported to allow 5,000.
- **A GPT:** create a GPT and paste the same text into Instructions.

## Gemini

Create a Gem and paste `dist/system-prompt.md` into its instructions.

## What you lose outside the plugin

| Plugin feature | Outside Claude Code |
|---|---|
| Rule card at session start | Same text, pasted once |
| Learner line ("fix their own line, end with a predict-first question") | Missing |
| Emergency line ("next action first") | Missing |
| Haiku auto-reminder | Missing |
| Skill modes (scan, learn, rewrite, score) | Only with the claude.ai Skill upload |
| Scoring answers | Use the [playground](../playground/) or `python3 skills/brainres/scripts/brainlint.py` |

---

## 한국어 요약

- **Claude Code:** 플러그인을 설치하세요. 훅까지 들어가는 방법은 플러그인뿐입니다.
- **claude.ai:**
  - 프로젝트 지침에 `dist/system-prompt.md`를 붙여 넣으면 그 프로젝트의 모든 대화에 적용됩니다.
  - 스킬 업로드(Customize → Skills, 유료 요금제 + 코드 실행 필요)는 Claude가 필요하다고 판단할 때만 불러옵니다. 우리 측정에서는 24번 중 1번이었습니다.
- **ChatGPT:** Settings → Personalization → 맞춤 지침에 `dist/system-prompt.md`를 붙여 넣으세요. 1,188자라서 1,500자 칸에 들어갑니다.
- **Gemini:** Gem을 만들고 지침에 붙여 넣으세요.
- **빠지는 것:** 학습자 줄, 긴급 상황 줄, Haiku 자동 리마인더는 플러그인에서만 동작합니다.
