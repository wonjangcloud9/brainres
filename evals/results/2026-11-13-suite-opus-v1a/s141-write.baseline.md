<!-- Q: Write a Python function that checks whether a string is a palindrome. -->

```python
def is_palindrome(s: str, ignore_case: bool = True, alnum_only: bool = True) -> bool:
    """
    Return True if `s` reads the same forwards and backwards.

    By default, comparison ignores case and non-alphanumeric characters,
    so "A man, a plan, a canal: Panama" is considered a palindrome.
    """
    if alnum_only:
        s = "".join(ch for ch in s if ch.isalnum())
    if ignore_case:
        s = s.casefold()
    return s == s[::-1]
```

**Examples:**

```python
is_palindrome("racecar")                          # True
is_palindrome("A man, a plan, a canal: Panama")   # True
is_palindrome("hello")                            # False
is_palindrome("")                                 # True (empty string)
is_palindrome("Abba", ignore_case=False)          # False
is_palindrome("ab ba", alnum_only=False)          # False
```

**Notes:**
- `casefold()` is used instead of `lower()` because it handles Unicode case more aggressively (e.g., German `ß` → `ss`).
- `s[::-1]` builds a reversed copy, which takes O(n) extra memory. If memory matters for very large inputs, use a two-pointer version instead:

```python
def is_palindrome_two_pointer(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i].casefold() != s[j].casefold():
            return False
        else:
            i += 1
            j -= 1
    return True
```

This version ignores case and non-alphanumeric characters the same way the default does, but uses O(1) extra space.
