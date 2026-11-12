<!-- Q: Is 0.1 + 0.2 === 0.3 true in JavaScript? -->

No, `0.1 + 0.2 === 0.3` is `false` in JavaScript. The sum is `0.30000000000000004`.

JavaScript uses IEEE 754 double-precision floats, which store numbers in binary. 0.1 and 0.2 have no exact binary representation, so each is stored as a slightly rounded value. Adding them carries the rounding error into the result, which lands one step above the double closest to 0.3.

To compare floats, check that the difference is within a small tolerance:

```js
Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON  // true
```

`Number.EPSILON` is about 2.2e-16, which works for values near 1. For larger magnitudes, scale the tolerance. For money, use integer cents instead (`10 + 20 === 30`).
