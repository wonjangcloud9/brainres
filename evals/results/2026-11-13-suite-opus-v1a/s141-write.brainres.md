<!-- Q: Write a Python function that checks whether a string is a palindrome. -->

This function ignores case, spaces and punctuation, so `"A man, a plan, a canal: Panama"` counts as a palindrome:

```python
def is_palindrome(s: str) -> bool:
    """Return True if s reads the same forwards and backwards,
    ignoring case and non-alphanumeric characters."""
    cleaned = [c.casefold() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]
```

Example:

```python
>>> is_palindrome("A man, a plan, a canal: Panama")
True
>>> is_palindrome("racecar")
True
>>> is_palindrome("hello")
False
>>> is_palindrome("")
True
```

How it works:

1. It keeps only letters and digits, lowercased with `casefold()`. That method handles non-English case rules better than `lower()`.
2. It compares the cleaned list to its reverse (`[::-1]`).

For a strict check where `"Racecar"` is **not** a palindrome, use `return s == s[::-1]`.

If you want it saved to a file with tests, tell me the filename.
