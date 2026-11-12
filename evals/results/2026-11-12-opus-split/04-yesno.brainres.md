<!-- Q: Is 0.1 + 0.2 === 0.3 true in JavaScript? -->

**No.** `0.1 + 0.2` evaluates to `0.30000000000000004`, so `0.1 + 0.2 === 0.3` is `false`.

JavaScript numbers are IEEE 754 binary doubles, and neither `0.1` nor `0.2` has an exact binary representation. Their tiny rounding errors add up to a result one step above the double closest to `0.3`.

To compare floats, check that the difference is within a tolerance:

```js
Math.abs((0.1 + 0.2) - 0.3) < Number.EPSILON  // true
```

`Number.EPSILON` (about `2.2e-16`) only suits values near 1. For larger magnitudes, scale it: `Math.abs(a - b) < Number.EPSILON * Math.max(Math.abs(a), Math.abs(b))`. For money, store integer cents instead of fractional dollars.
