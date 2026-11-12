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

Yes, it returns the input's unique items in their first-seen order. It's an order-preserving deduplication.

How it works:
- `seen` is a set that records items already encountered. Membership checks on a set take O(1) on average.
- `out` is a list that collects each item the first time it appears.
- For each `x`, if it isn't in `seen`, the function adds it to both `seen` and `out`. Repeats are skipped.

Example:

```python
f([3, 1, 3, 2, 1])  # [3, 1, 2]
```

The items must be hashable, because `set` stores them. Passing lists or dicts raises `TypeError`. Overall cost is O(n) time and O(n) extra space.
