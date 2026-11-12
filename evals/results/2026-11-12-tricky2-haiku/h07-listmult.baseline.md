<!-- Q: In Python: a = [[0] * 2] * 2; a[0][0] = 1; print(a). What is printed? -->

The output is:

```
[[1, 0], [1, 0]]
```

The outer `* 2` doesn't copy the inner list. `[0] * 2` creates one list `[0, 0]`, and the outer `* 2` puts two references to that same list into `a`. So `a[0]` and `a[1]` are the same object, and `a[0][0] = 1` changes both rows.

To get independent rows, use a list comprehension: `a = [[0] * 2 for _ in range(2)]`.
