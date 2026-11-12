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

It removes duplicates from `xs` while keeping the first occurrence of each item in its original order, and returns the result as a new list.

How it works: `seen` is a set that records items already encountered, so each membership check is O(1) on average. `out` collects an item only the first time it appears.

Example: `f([3, 1, 3, 2, 1])` returns `[3, 1, 2]`.

Two things to know:
- Items must be hashable (numbers, strings, tuples). A list or dict in `xs` raises `TypeError`.
- Total time is O(n), which beats the naive `if x not in out` approach at O(n²).

In Python 3.7+, `list(dict.fromkeys(xs))` does the same thing in one line.
