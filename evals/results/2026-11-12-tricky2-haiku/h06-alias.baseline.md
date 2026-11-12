<!-- Q: In Python: x = [1, 2, 3]; y = x; y += [4]; print(len(x)). What is printed? -->

**Output: `4`**

`y = x` makes both names refer to the same list object. `y += [4]` calls `list.__iadd__`, which extends that list in place rather than creating a new one. Since `x` points to the same object, it now also contains `[1, 2, 3, 4]`.

If you wanted `y` to be an independent copy, use `y = x.copy()` or `y = list(x)`. Writing `y = y + [4]` would also create a new list, leaving `x` unchanged, so `len(x)` would print `3`.
