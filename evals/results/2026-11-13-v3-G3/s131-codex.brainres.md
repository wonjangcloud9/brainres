<!-- Q: What does this do?

```python
pairs = [(x, y) for x in range(3) for y in range(x)]
``` -->

It builds the list `[(1, 0), (2, 0), (2, 1)]`: every pair `(x, y)` with `0 <= y < x < 3`.

The loops nest left to right, like this:

```python
pairs = []
for x in range(3):        # x = 0, 1, 2
    for y in range(x):    # y runs from 0 up to x-1
        pairs.append((x, y))
```

Trace:
- `x=0`: `range(0)` is empty, so nothing is added.
- `x=1`: `y=0`, adds `(1, 0)`.
- `x=2`: `y=0, 1`, adds `(2, 0)` and `(2, 1)`.

The inner range depends on `x`, so you get the pairs below the diagonal, and each combination appears once. It is the same as `itertools.combinations(range(3), 2)` with the order of each pair reversed.
