<!-- Q: What does this do?

```python
pairs = [(x, y) for x in range(3) for y in range(x)]
``` -->

It builds the list `[(1, 0), (2, 0), (2, 1)]`: every pair `(x, y)` where `x` is in `0..2` and `y` is in `0..x-1`, so `y < x`.

The nested loops run in the order they're written, with the first `for` as the outer loop:

| x | `range(x)` | pairs added |
|---|------------|-------------|
| 0 | empty | none |
| 1 | 0 | `(1, 0)` |
| 2 | 0, 1 | `(2, 0)`, `(2, 1)` |

It's equivalent to:

```python
pairs = []
for x in range(3):
    for y in range(x):
        pairs.append((x, y))
```

Because `range(x)` depends on the outer `x`, this gives the strictly lower-triangular index pairs, which is a common pattern for visiting each unordered pair once.

If you want to confirm, run `print(pairs)` after the line.
