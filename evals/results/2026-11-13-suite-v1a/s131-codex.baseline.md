<!-- Q: What does this do?

```python
pairs = [(x, y) for x in range(3) for y in range(x)]
``` -->

It builds a list of `(x, y)` tuples where `y` ranges over values less than `x`, as a nested loop in one expression.

Equivalent to:

```python
pairs = []
for x in range(3):        # x = 0, 1, 2
    for y in range(x):    # y = 0..x-1
        pairs.append((x, y))
```

Stepping through:

- `x = 0`: `range(0)` is empty, so nothing is added.
- `x = 1`: `y = 0`, which adds `(1, 0)`.
- `x = 2`: `y = 0, 1`, which adds `(2, 0)` and `(2, 1)`.

Result:

```python
[(1, 0), (2, 0), (2, 1)]
```

These are all pairs with `x > y` drawn from `0..2`. The `for` clauses read left to right in the same order as the nested loops, and the inner one can use the outer variable (`range(x)`).
