<!-- Q: Write a Python function that checks whether a string is a palindrome. -->

This function ignores case, spaces, and punctuation, and compares the cleaned string to its reverse:

```python
def is_palindrome(s: str) -> bool:
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]
```

Examples:

```python
is_palindrome("A man, a plan, a canal: Panama")  # True
is_palindrome("race a car")                      # False
is_palindrome("")                                # True (empty string counts as a palindrome)
```

For strict matching (case, spaces, and punctuation all count), use `return s == s[::-1]` instead.

One caveat: `str.isalnum()` also accepts non-ASCII letters and digits, so `"été"` is handled correctly. If you need accent-insensitive matching (`"é"` equals `"e"`), normalize first with `unicodedata.normalize("NFD", s)` and drop the combining marks.
