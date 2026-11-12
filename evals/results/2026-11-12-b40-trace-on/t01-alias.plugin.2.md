<!-- Q: What does this print?

```python
x = [1, 2, 3]
y = x
y.append(4)
print(len(x))
``` -->

It prints `4`, because `y = x` makes both names point to the same list, so `y.append(4)` changes the list that `x` sees too.

To get an independent copy, use `y = x.copy()` (or `list(x)`). Then `len(x)` stays `3`.
