<!-- Q: What does this print?

```python
x = [1, 2, 3]
y = x
y.append(4)
print(len(x))
``` -->

It prints `4`, because `y = x` copies the reference, not the list, so `x` and `y` are the same list object. `y.append(4)` changes that shared list to `[1, 2, 3, 4]`, and `len(x)` sees the change.

To get an independent copy, use `y = x.copy()` or `y = x[:]`. Then `len(x)` stays `3`.
