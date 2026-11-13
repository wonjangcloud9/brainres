<!-- Q: What does this do?

```python
pairs = [(x, y) for x in range(3) for y in range(x)]
``` -->

It's a nested list comprehension that builds every pair `(x, y)` where `0 ≤ y < x < 3`.

It's equivalent to:

```python
pairs = []
for x in range(3):        # x = 0, 1, 2
    for y in range(x):    # y runs from 0 up to x-1
        pairs.append((x, y))
```

The `for` clauses are read left to right, outer loop first.

| `x` | `range(x)` | pairs added |
|-----|------------|-------------|
| 0   | empty      | none        |
| 1   | `0`        | `(1, 0)`    |
| 2   | `0, 1`     | `(2, 0), (2, 1)` |

**Result:**
```python
[(1, 0), (2, 0), (2, 1)]
```

Because `y` is always less than `x`, you get each unordered pair of distinct numbers from `{0, 1, 2}` exactly once, with no `(x, x)` pairs and no mirrored duplicates. It gives the same pairs as `itertools.combinations(range(3), 2)`, except each tuple is written larger-first.
