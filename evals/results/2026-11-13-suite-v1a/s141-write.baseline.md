<!-- Q: Write a Python function that checks whether a string is a palindrome. -->

```python
def is_palindrome(s: str) -> bool:
    """Return True if s reads the same forwards and backwards,
    ignoring case and non-alphanumeric characters."""
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]
```

Examples:

```python
is_palindrome("A man, a plan, a canal: Panama")  # True
is_palindrome("racecar")                          # True
is_palindrome("hello")                            # False
is_palindrome("")                                 # True
```

If you want a strict check (case- and punctuation-sensitive), use `return s == s[::-1]` instead.
