<!-- Q: What does this output?

```js
console.log([10, 1, 2].sort());
``` -->

It prints `[ 1, 10, 2 ]`, because `sort()` with no comparator converts items to strings and compares them lexicographically, so `"10"` < `"2"` and `"1"` < `"10"`.

To sort numerically, use `[10, 1, 2].sort((a, b) => a - b)`, which gives `[1, 2, 10]`.
