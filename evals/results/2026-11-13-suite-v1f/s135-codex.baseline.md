<!-- Q: What does this regex match?

```
^\d{3}-\d{4}$
``` -->

It matches a string that is exactly a 7-digit, US-style local phone number in the format `XXX-XXXX`:

- `^` and `$` anchor the match to the start and end of the string, so nothing else can come before or after.
- `\d{3}` matches exactly three digits.
- `-` matches a literal hyphen.
- `\d{4}` matches exactly four digits.

**Matches:** `555-1234`, `000-0000`

**Doesn't match:** `5551234` (no hyphen), `555-12345` (too many digits), `55-1234` (too few), ` 555-1234` (leading space), `555-1234\n` in some engines depending on how `$` handles a trailing newline.

Note that `\d` can match non-ASCII digits in some engines (e.g., Python 3 `str` patterns match Arabic-Indic digits too). Use `[0-9]` if you need strictly ASCII digits.
