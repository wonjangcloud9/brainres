<!-- Q: What does this do?

```python
pairs = [(x, y) for x in range(3) for y in range(x)]
``` -->

It builds the list `[(1, 0), (2, 0), (2, 1)]`: every pair `(x, y)` where `x` is in `0..2` and `y` is a smaller non-negative integer than `x`.

The two `for` clauses nest left to right, like this loop:

```python
pairs = []
for x in range(3):
    for y in range(x):
        pairs.append((x, y))
```

Trace:

| x | `range(x)` | pairs added |
|---|------------|-------------|
| 0 | empty | none |
| 1 | 0 | (1, 0) |
| 2 | 0, 1 | (2, 0), (2, 1) |

So `x=0` contributes nothing because `range(0)` is empty. The result is all pairs with `y < x`, which is the strict lower triangle of a 3×3 grid.
