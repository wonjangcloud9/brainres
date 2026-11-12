<!-- Q: Write a Python function that checks whether a string is a palindrome. -->

Here is a function that ignores case and punctuation, so `"A man, a plan, a canal: Panama"` counts as a palindrome.

```python
def is_palindrome(s: str) -> bool:
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]
```

Examples:

```python
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("racecar"))                         # True
print(is_palindrome("hello"))                           # False
print(is_palindrome(""))                                # True (empty string)
```

The function keeps only letters and digits, lowercases them, and compares the list with its reverse. It runs in O(n) time and uses O(n) extra memory.

If you need exact matching instead, remove the filtering and compare `s` with `s[::-1]`. Tell me if you want a version that uses O(1) extra memory with two pointers.
