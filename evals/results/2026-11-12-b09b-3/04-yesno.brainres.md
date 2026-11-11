<!-- Q: Is 0.1 + 0.2 === 0.3 true in JavaScript? -->

No, it evaluates to `false`. `0.1 + 0.2` gives `0.30000000000000004` because JavaScript uses IEEE 754 64-bit floats, and neither 0.1 nor 0.2 can be stored exactly in binary, so the tiny rounding errors add up to a value slightly above 0.3.

To compare floats, check that the difference is smaller than a tolerance:

```js
Math.abs((0.1 + 0.2) - 0.3) < Number.EPSILON  // true
```

`Number.EPSILON` (~2.2e-16) works for values near 1. For larger magnitudes, scale the tolerance, or use integers (e.g. cents instead of dollars) when exactness matters, as with money.

You can confirm it in any console with `0.1 + 0.2` (prints `0.30000000000000004`).
