<!-- Q: What does this do?

```python
pairs = [(x, y) for x in range(3) for y in range(x)]
``` -->

This is a list comprehension that builds a list of tuples `(x, y)` where `y` is always less than `x`.

- `for x in range(3)` gives `x` = 0, 1, 2.
- `for y in range(x)` gives `y` from 0 up to `x - 1`. When `x` is 0, `range(0)` is empty, so nothing is added.

The result is:

```python
[(1, 0), (2, 0), (2, 1)]
```

It's equivalent to these nested loops:

```python
pairs = []
for x in range(3):
    for y in range(x):
        pairs.append((x, y))
```

This pattern is often used to enumerate the unique pairs of distinct indices (strictly lower-triangular positions), such as all unordered pairs `(i, j)` with `i > j`.
