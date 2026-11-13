<!-- Q: What does this regex match?

```
^\d{3}-\d{4}$
``` -->

It matches a string of exactly three digits, a hyphen, then exactly four digits, such as `555-1234`, which is the shape of a 7-digit US phone number without an area code.

- `^` and `$` anchor the match to the whole string, so `555-12345` and ` 555-1234` fail.
- `\d{3}` is exactly three digits, `-` is a literal hyphen, and `\d{4}` is exactly four digits.

One caveat: in some engines (Python 3 `str` patterns, .NET, Java with Unicode flags) `\d` also matches non-ASCII digits like Arabic-Indic `٥٥٥-١٢٣٤`. Use `[0-9]` if you need ASCII only. Also, `$` in Python and Perl allows a trailing newline, so `555-1234\n` can match unless you use `\Z` or `fullmatch`.
