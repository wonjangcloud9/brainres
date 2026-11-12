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

It removes duplicates from `xs` and keeps the first occurrence of each value, in its original order.

- `seen` is a set of values already added to `out`. Set lookups take constant time on average, so the whole function runs in O(n) time for n items.
- Each value is checked with `x not in seen`. If it's new, it goes into both `seen` and `out`.
- Every element must be hashable (for example, numbers, strings, or tuples). A list element raises `TypeError`.

Example: `f([3, 1, 3, 2, 1])` returns `[3, 1, 2]`.

If you need this for unhashable items such as dicts, I can show a version that compares with `==` instead, at O(n²) cost.
