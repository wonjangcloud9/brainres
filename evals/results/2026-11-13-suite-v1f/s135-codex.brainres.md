<!-- Q: What does this regex match?

```
^\d{3}-\d{4}$
``` -->

It matches a string of exactly three digits, a hyphen, then four digits, such as `555-1234`, which is the shape of a US 7-digit local phone number without an area code.

Breakdown:
- `^` and `$` anchor the match to the whole string, so `555-12345` and ` 555-1234` fail.
- `\d{3}` is exactly three digits.
- `-` is a literal hyphen.
- `\d{4}` is exactly four digits.

Two caveats: in some engines (Python 3 `re` with str, .NET, JavaScript with the `u` flag in some cases) `\d` can match non-ASCII digits like `٣`, so use `[0-9]` if you need ASCII only. Also, in Python and some other engines `$` matches before a trailing newline, so `"555-1234\n"` passes unless you use `\Z` or `fullmatch`.
