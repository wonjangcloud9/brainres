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

It returns the unique items from `xs` in their first-seen order. It drops every later duplicate.

- `seen` is a set that records what has already been kept. Set membership checks run in about O(1), so the whole function is O(n) on average.
- `out` is a list that keeps the first occurrence of each value, in input order.

For example, `f([3, 1, 3, 2, 1])` returns `[3, 1, 2]`. The items must be hashable, so a list of lists would raise a `TypeError`.
