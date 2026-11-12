<!-- Q: What does this do?

```python
pairs = [(x, y) for x in range(3) for y in range(x)]
``` -->

It builds the list `[(1, 0), (2, 0), (2, 1)]`: every pair `(x, y)` with `x` in `0..2` and `y` strictly less than `x`.

The two `for` clauses nest left to right, like this:

```python
pairs = []
for x in range(3):
    for y in range(x):
        pairs.append((x, y))
```

Trace:

| x | range(x) | pairs added |
|---|----------|-------------|
| 0 | empty | none |
| 1 | 0 | (1, 0) |
| 2 | 0, 1 | (2, 0), (2, 1) |

Since `x = 0` gives an empty inner range, it contributes nothing. The result is the pairs with `y < x`, i.e. the strict lower triangle of a 3×3 grid. `itertools.combinations(range(3), 2)` gives the same pairs with the order flipped, `(0, 1), (0, 2), (1, 2)`.
