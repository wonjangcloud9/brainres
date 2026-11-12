<!-- Q: In JavaScript, what does [10, 1, 2].sort() return? -->

`[10, 1, 2].sort()` returns `[1, 10, 2]`.

By default, `sort()` converts elements to strings and compares them by UTF-16 code units, so `"10"` comes before `"2"`. To sort numerically, pass a comparator:

```js
[10, 1, 2].sort((a, b) => a - b); // [1, 2, 10]
```

Note that `sort()` mutates the original array and returns a reference to it.
