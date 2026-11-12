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

This function removes duplicates from a list (or any iterable) while preserving the original order of first appearance.

**How it works:**
- `seen` is a set that tracks which items have already been encountered (set lookups are O(1) on average).
- `out` collects the unique items in order.
- For each `x`, if it hasn't been seen, it's added to both `seen` and `out`; otherwise it's skipped.

**Example:**
```python
f([3, 1, 3, 2, 1])  # [3, 1, 2]
```

**Notes:**
- Runs in O(n) time on average, with O(n) extra space.
- Items must be hashable (so lists or dicts as elements would raise `TypeError`).
- It keeps the first occurrence of each value, unlike `list(set(xs))`, which loses ordering.
- In Python 3.7+, `list(dict.fromkeys(xs))` does the same thing more concisely.
