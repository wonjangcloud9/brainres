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

It removes duplicates from `xs` while keeping the first occurrence of each item, in the original order.

How it works:

1. `seen` is a set that records items already encountered.
2. `out` is a list that collects the results.
3. For each `x`, the code checks whether `x` is in `seen`. If not, it adds `x` to `seen` and appends it to `out`. If it is, the item is skipped.

For example, `f([3, 1, 3, 2, 1])` returns `[3, 1, 2]`.

Because set lookups take constant time on average, the whole function runs in O(n) time. The items must be hashable (for example, numbers, strings, or tuples). A list of lists would raise a `TypeError`.
