<!-- Q: In Python: x = [1, 2, 3]; y = x; y += [4]; print(len(x)). What is printed? -->

4

`y += [4]` calls `list.__iadd__`, which extends the list in place. `y` and `x` point to the same list object, so `x` also gets the 4. The output is `4`.

If you wanted a separate copy, use `y = x + [4]` or `y = x.copy()` before appending.
