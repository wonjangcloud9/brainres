<!-- Q: What does this do?

```python
pairs = [(x, y) for x in range(3) for y in range(x)]
``` -->

It builds the list `[(1, 0), (2, 0), (2, 1)]`: every pair `(x, y)` where `y` is a smaller non-negative integer than `x`, with `x` in 0–2.

The two `for` clauses nest left to right, like this loop:

```python
pairs = []
for x in range(3):
    for y in range(x):
        pairs.append((x, y))
```

Step by step:

| x | `range(x)` | pairs added |
|---|------------|-------------|
| 0 | empty | none |
| 1 | 0 | `(1, 0)` |
| 2 | 0, 1 | `(2, 0)`, `(2, 1)` |

Because the inner range depends on `x`, `x=0` contributes nothing. The result is the strict lower triangle of a 3×3 grid.
