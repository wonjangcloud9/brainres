<!-- Q: What does this do?

```python
pairs = [(x, y) for x in range(3) for y in range(x)]
``` -->

It builds `[(1, 0), (2, 0), (2, 1)]`: every pair where `y` is strictly less than `x`, for `x` in 0–2.

The two `for` clauses nest left to right, like this loop:

```python
pairs = []
for x in range(3):
    for y in range(x):
        pairs.append((x, y))
```

The inner range depends on `x`, so each step produces:

| `x` | `range(x)` | pairs added |
|---|---|---|
| 0 | empty | none |
| 1 | 0 | `(1, 0)` |
| 2 | 0, 1 | `(2, 0)`, `(2, 1)` |

This is a common way to get each unordered pair of distinct items exactly once. For `n` items you get `n*(n-1)/2` pairs, so `3*2/2 = 3` here. `itertools.combinations(range(3), 2)` gives the same pairs with each tuple flipped: `(0, 1), (0, 2), (1, 2)`.

To check it, run it in a REPL with `range(4)`, which should give 6 pairs.
