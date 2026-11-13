# Curated-list submissions (owner submits)

The loop drafted these on 2026-11-13 from each list's own rules. Every submission must be made by the owner. Two of the lists explicitly reject agent-made submissions or PRs.

**Suggested order:**

| # | Where | Reach | Effort | When |
|---|---|---|---|---|
| 1 | [claudemarketplaces.com](https://claudemarketplaces.com/submit) | Directory of Claude plugins, refreshed daily from GitHub | 2 min | Now |
| 2 | [Anthropic community marketplace](https://clau.de/plugin-directory-submission) | Installable with `claude plugin marketplace add anthropics/claude-plugins-community`; listed on claude.com/plugins | 10 min, plus a security scan | After D8a, the version bump |
| 3 | [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) (57.9k ★) | The canonical Claude Code list | 5 min | **From 2026-11-26.** The repo needs to be 14 days old with ongoing commits, since it has fewer than 100 stars |
| 4 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) (2k ★) | A plugin list that hosts its own copies | 20 min, fork + PR | Optional; best after D13 (slim plugin folder) |

---

## 1. claudemarketplaces.com

The site crawls GitHub daily, so it may pick up `.claude-plugin/marketplace.json` on its own. Search the site for "brainres" first. If it isn't listed, use **Submit** with:

- **Repository:** `https://github.com/wonjangcloud9/brainres`
- **Install:** `/plugin marketplace add wonjangcloud9/brainres`, then `/plugin install brainres@brainres`
- **One-line description:** Shapes Claude's answers for how people read: answer first, chunked to working-memory limits, exact code and numbers. Ships with a readability scorer. Measured on 80 prompts: 29% shorter, Brain Score +4.6.

## 2. Anthropic community marketplace

Submit at **clau.de/plugin-directory-submission**. PRs to `anthropics/claude-plugins-community` are closed automatically. Listed plugins pass automated security scanning, so describe the hooks plainly:

- **Plugin name:** `brainres`
- **Source:** `https://github.com/wonjangcloud9/brainres` (marketplace `.claude-plugin/marketplace.json`, plugin at the repo root)
- **Short description:** Shapes Claude's answers for how people read: answer in the first sentence, chunk to working-memory limits, keep code, numbers and warnings exact. Bundles brainlint, a dependency-free readability scorer for English and Korean.
- **What it installs:**
  - **SessionStart hook** (`hooks/brainres-context.sh`, bash): prints a 500-token rule card once per session.
  - **UserPromptSubmit hook** (`hooks/brainres-reminder.sh`, bash + python3): reads the prompt from stdin. It adds one line only on a learner or emergency signal, plus a short reminder line if the user sets `BRAINRES_REMINDER=on`. Nothing else is read, and nothing is written.
  - **Skill** `skills/brainres` and **output style** `output-styles/brainres.md`.
- **Network, files, secrets:** none. The hooks make no network calls and write no files.
- **Off switch:** `export BRAINRES=off` or `touch ~/.claude/brainres.off`.
- **Before submitting:** do the 0.2.0 release (D8), so the reviewed version matches a tag. D8a, the version bump, is done. The icon `.claude-plugin/icon.png` is in place, and the directory takes the icon only on the first submission.

## 3. awesome-claude-code (from 2026-11-26)

Submit **only** through the web issue form: [Recommend a resource](https://github.com/hesreallyhim/awesome-claude-code/issues/new?template=recommend-resource.yml). The `gh` CLI and PRs aren't accepted, and recommendations "must be created by human beings". Descriptions must be descriptive, not promotional, must not address the reader, and must be 10–500 characters on one line.

- **Display Name:** `brainres`
- **Category:** `Writing & Prose Quality`
- **Link:** `https://github.com/wonjangcloud9/brainres`
- **Author Name:** `wonjangcloud9`
- **Author Link:** `https://github.com/wonjangcloud9`
- **Description** (429 characters):

  > Claude Code plugin that applies reading-research rules to answers: answer in the first sentence, chunk to working-memory limits, keep code and numbers exact. A 500-token session card plus situational lines for learners and emergencies; includes brainlint, a stdlib readability scorer for English and Korean. Evaluated on an 80-prompt suite: answers 29% shorter, Brain Score +4.6, with the 1.8 pp loss in key-fact detail reported.

- **Checklist:** tick the boxes yourself after you've actually checked them. That includes looking through the current list for anything similar, such as caveman, humanizer, i-have-adhd and talk-normal. Leave the last box unchecked, as the form says.
- If it's accepted, you may add their "Mentioned in Awesome Claude Code" badge to the README.

## 4. ComposioHQ/awesome-claude-plugins (optional)

Their list hosts a copy of each plugin: fork the repo, add a folder, add a README line and open a PR. That copy goes stale whenever brainres changes, so treat it as optional and do it after D13, which makes the plugin folder small and self-contained.

- **Folder** `brainres/` containing `.claude-plugin/plugin.json`, `hooks/`, `skills/brainres/` and `output-styles/`, copied from this repo.
- **README line** (under a writing/documentation section, or wherever fits best):

  `- [brainres](./brainres) - Shapes Claude's answers for how people read: answer first, chunked, exact code and numbers; includes a readability scorer.`

- **Entry for their root `marketplace.json`:** `{"name": "brainres", "source": "./brainres", "description": "Shapes Claude's answers for how people read."}`
