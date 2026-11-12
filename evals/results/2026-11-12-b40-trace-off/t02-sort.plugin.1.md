<!-- Q: What does this output?

```js
console.log([10, 1, 2].sort());
``` -->

It prints `[ 1, 10, 2 ]`.

`sort()` with no comparator converts items to strings and compares them in UTF-16 order, so `"10"` comes before `"2"` because `"1"` < `"2"`. That puts `1`, `10`, `2` in that order.

For numeric order, use `[10, 1, 2].sort((a, b) => a - b)`, which gives `[1, 2, 10]`.
