# Launch drafts

Drafts for the owner to post. The loop never posts anywhere.

| File | Where | Best time (rule of thumb) |
|---|---|---|
| [show-hn.md](show-hn.md) | Hacker News "Show HN" | Tue–Thu, 8–10am US Eastern |
| [x-thread.md](x-thread.md) | X / Twitter | Weekday morning US or KST evening |
| [geeknews.md](geeknews.md) | GeekNews (news.hada.io) | Weekday morning KST |
| [reddit-claudeai.md](reddit-claudeai.md) | r/ClaudeAI | Weekday, US daytime |

Before posting:

0. **Set the GitHub social preview once:** Settings → General → Social preview → upload [`assets/social-preview.png`](../assets/social-preview.png), which is 1280×640. Its source is `assets/social-preview.html`; re-render it with headless Chrome after the numbers change. The same image works as the first X tweet's picture.

1. Re-run `python3 scripts/coverage.py` and `brainlint` on the examples, and update any number that changed.
2. Stay in the HN thread for the first 2 hours. Answer critics with data, and concede what is true. The coverage ledger and "honest limits" are the moat.
3. Don't claim comprehension gains that haven't been measured yet (B10 is still open).
