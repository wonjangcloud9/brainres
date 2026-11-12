<!-- Q: What does this output?

```js
console.log([10, 1, 2].sort());
``` -->

It outputs `[ 1, 10, 2 ]`, because `sort()` with no comparator converts items to strings and compares them in UTF-16 order, so `"10"` comes before `"2"`.

For numeric order, pass a comparator: `[10, 1, 2].sort((a, b) => a - b)` gives `[1, 2, 10]`.
