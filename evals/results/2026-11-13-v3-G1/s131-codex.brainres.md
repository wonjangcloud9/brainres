<!-- Q: What does this do?

```python
pairs = [(x, y) for x in range(3) for y in range(x)]
``` -->

It builds a list of `(x, y)` tuples where `y` is strictly less than `x`, for `x` in 0 to 2.

The two `for` clauses nest left to right, like this:

```python
pairs = []
for x in range(3):
    for y in range(x):
        pairs.append((x, y))
```

Trace:

| x | `range(x)` | tuples added |
|---|-----------|--------------|
| 0 | empty | none |
| 1 | 0 | `(1, 0)` |
| 2 | 0, 1 | `(2, 0)`, `(2, 1)` |

Result:

```python
[(1, 0), (2, 0), (2, 1)]
```

These are all pairs with `x > y` in the range 0–2. It's the same as `itertools.combinations(range(3), 2)` with each pair reversed.
