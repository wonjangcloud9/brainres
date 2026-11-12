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

This function removes duplicates from a list (or any iterable) while **preserving the original order** of first appearance.

How it works:
- `seen` is a set that tracks which items have already been encountered (O(1) lookups).
- `out` is the result list.
- For each `x`, if it hasn't been seen, it's added to `seen` and appended to `out`. Later repeats are skipped.

Example:
```python
f([3, 1, 3, 2, 1])  # [3, 1, 2]
```

Notes:
- Time complexity is O(n), with O(n) extra space.
- Items must be **hashable** (ints, strings, tuples are fine; lists and dicts will raise `TypeError`).
- Equivalent one-liner in Python 3.7+: `list(dict.fromkeys(xs))`, since dicts preserve insertion order.
- Unlike `list(set(xs))`, the output order is deterministic and matches the input.
