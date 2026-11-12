<!-- Q: Write a Python function that checks whether a string is a palindrome. -->

```python
import re


def is_palindrome(text: str) -> bool:
    """Return True if `text` reads the same forwards and backwards.

    Case, spaces, and punctuation are ignored, so "A man, a plan, a canal: Panama"
    counts as a palindrome.
    """
    cleaned = re.sub(r"[^0-9a-z]", "", text.lower())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    tests = [
        ("racecar", True),
        ("A man, a plan, a canal: Panama", True),
        ("hello", False),
        ("", True),
        ("No 'x' in Nixon", True),
    ]
    for text, expected in tests:
        result = is_palindrome(text)
        print(f"{text!r:35} -> {result} (expected {expected})")
        assert result == expected
```

The function lowercases the input, strips everything except letters and digits, then compares the result to its reverse. If you want a stricter check that treats the string literally (case and punctuation matter), drop the regex and compare `text == text[::-1]`.
