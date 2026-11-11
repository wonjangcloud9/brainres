<!-- Q: Is 0.1 + 0.2 === 0.3 true in JavaScript? -->

No, `0.1 + 0.2 === 0.3` is `false` in JavaScript. `0.1 + 0.2` evaluates to `0.30000000000000004`.

JavaScript numbers are 64-bit binary floats, and 0.1 and 0.2 have no exact binary representation. Each is stored as a slightly rounded value, and the rounding errors add up to a result that differs from the rounded value of 0.3.

To compare floats, check that the difference is within a small tolerance:

```js
Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON  // true
```

`Number.EPSILON` (~2.22e-16) works for values near 1. For larger magnitudes, scale the tolerance, or work in integers (for example, cents instead of dollars).
