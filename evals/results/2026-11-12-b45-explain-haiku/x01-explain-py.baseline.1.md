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

This function removes duplicates from a list while preserving the order of first occurrence.

It works like this:

1. `seen` is a set that records every value already encountered.
2. `out` is a list that collects the unique values in order.
3. For each element `x` in `xs`, it checks whether `x` is already in `seen`. If not, it adds `x` to both `seen` and `out`. If it is, the element is skipped.
4. It returns `out`.

For example:

```python
f([3, 1, 3, 2, 1])  # returns [3, 1, 2]
```

The set gives fast membership checks, so the function runs in O(n) time on average. This is much faster than a naive approach that checks membership in a list, which would be O(n²).

The elements must be hashable (such as numbers, strings, or tuples), because they're stored in a set. Passing a list of lists, for instance, raises a `TypeError`.
