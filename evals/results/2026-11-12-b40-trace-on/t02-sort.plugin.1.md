<!-- Q: What does this output?

```js
console.log([10, 1, 2].sort());
``` -->

`[10, 1, 2].sort()` compares elements as strings, so it prints `[ 1, 10, 2 ]`.

The strings sort as "10" < "1"? No: "1" is a prefix of "10", so "1" < "10", and "10" < "2" because "1" < "2". For numeric order, use `.sort((a, b) => a - b)`, which gives `[ 1, 2, 10 ]`.
