<!-- Q: What does this print?

```python
x = [1, 2, 3]
y = x
y.append(4)
print(len(x))
``` -->

It prints `4`, because `y = x` makes both names point to the same list object, so `y.append(4)` changes the list that `x` also sees.

To get an independent copy, use `y = x.copy()` (or `list(x)`). Then `len(x)` would stay `3`.
