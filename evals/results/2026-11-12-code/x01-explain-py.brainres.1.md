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

How it works: `seen` is a set for fast membership checks (average O(1)), and `out` collects items in order. For each `x`, if it hasn't been seen, it is added to both. Later repeats are skipped.

Example:

```python
f([3, 1, 3, 2, 1])  # [3, 1, 2]
```

Two things to know:
- Items must be hashable (ints, strings, tuples). Lists or dicts in `xs` raise `TypeError`.
- The whole thing runs in O(n) time. `list(set(xs))` is also O(n) but loses order. In Python 3.7+, `list(dict.fromkeys(xs))` does the same job as `f` in one line.
