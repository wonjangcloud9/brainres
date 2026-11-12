<!-- Q: What does this code do?

```python
def f(xs):
    seen = set()
    out = []
    for x in xs:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out
``` -->

This function removes duplicates from a list while preserving the original order. It returns a new list containing each element from `xs` the first time it appears.

How it works:

1. `seen` is a set that tracks elements already encountered. Set lookups are O(1) on average.
2. `out` is the result list.
3. For each `x` in `xs`, if `x` isn't in `seen`, it gets added to both `seen` and `out`. Repeats are skipped.

For example:

```python
f([3, 1, 3, 2, 1])  # returns [3, 1, 2]
```

Notes:

- **Requires hashable elements.** Items must be hashable to go in a set, so `f([[1], [2]])` raises `TypeError`.
- **Uses equality and hashing.** Elements are considered duplicates if they are equal and have the same hash. For example, `1`, `1.0`, and `True` are treated as the same value.
- **Complexity:** O(n) time and O(n) extra space.
- **Equivalent in modern Python:** `list(dict.fromkeys(xs))` does the same thing in one line and also preserves order.
