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

It removes duplicates from a list while keeping the first occurrence of each item, in the original order.

How it works:

1. `seen` is a set that records items already processed. Set lookups are O(1) on average, so the membership test is fast.
2. For each `x`, the code checks whether it is already in `seen`. If not, it adds `x` to `seen` and appends it to `out`. If it is, the item is skipped.
3. `out` is returned with each unique value appearing once, in first-seen order.

Example: `f([3, 1, 3, 2, 1])` returns `[3, 1, 2]`.

This works only if the items are hashable (for example, numbers, strings, or tuples). A list of lists raises `TypeError` when `x` goes into the set. On Python 3.7+, `dict.fromkeys(xs)` gives the same result in a single line.
