<!-- Q: Write a Python function that checks whether a string is a palindrome. -->

```python
def is_palindrome(s: str) -> bool:
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]
```

It ignores case, spaces, and punctuation, so `is_palindrome("A man, a plan, a canal: Panama")` returns `True`, and an empty string returns `True`.

If you want a strict check that compares the raw string, use `s == s[::-1]` instead.

Want me to save this to a file with a few tests?
