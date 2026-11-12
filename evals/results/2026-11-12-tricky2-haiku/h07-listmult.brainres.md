<!-- Q: In Python: a = [[0] * 2] * 2; a[0][0] = 1; print(a). What is printed? -->

[[0, 0], [0, 0]] is wrong. The output is:

```
[[1, 0], [1, 0]]
```

Because `[0] * 2` creates one list `[0, 0]`, and `* 2` on the outer list repeats the same reference twice. So `a[0]` and `a[1]` are the same object, and setting `a[0][0] = 1` changes both rows.

To get independent rows, use `a = [[0] * 2 for _ in range(2)]`.
