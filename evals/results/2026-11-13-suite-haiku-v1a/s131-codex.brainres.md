<!-- Q: What does this do?

```python
pairs = [(x, y) for x in range(3) for y in range(x)]
``` -->

It builds a list of pairs with `y < x`: `[(1, 0), (2, 0), (2, 1)]`.

The comprehension has two loops, read left to right:

1. `for x in range(3)` runs `x` through 0, 1, 2.
2. `for y in range(x)` runs `y` through `range(x)`, so `y` is always less than `x`.

When `x = 0`, `range(0)` is empty, so it adds nothing. The equivalent nested loops are:

```python
pairs = []
for x in range(3):
    for y in range(x):
        pairs.append((x, y))
```
