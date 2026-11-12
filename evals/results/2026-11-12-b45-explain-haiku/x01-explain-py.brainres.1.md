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

It returns the input's unique elements in their first-seen order: `f([3, 1, 3, 2, 1])` gives `[3, 1, 2]`.

It works in one pass:

1. `seen` is a set that records every value already added.
2. `out` is a list that keeps the kept values in order.
3. For each `x`, the function checks membership in `seen`, which is O(1) on average. If `x` is new, it goes into both `seen` and `out`.

Because the list is built as it goes, the first occurrence wins and later duplicates are dropped. The set is what makes this fast. Without it, `x not in out` would scan the list each time and the whole function would be O(n²).

Two limits follow from using a set:
- Every element must be hashable. A list inside `xs` raises `TypeError`.
- Equality decides duplicates. `1`, `1.0`, and `True` count as the same value, so only the first one is kept.

On Python 3.7+, `list(dict.fromkeys(xs))` does the same thing in one line.
