<!-- Q: Is 0.1 + 0.2 === 0.3 true in JavaScript? -->

No. `0.1 + 0.2 === 0.3` is `false` in JavaScript, because `0.1 + 0.2` evaluates to `0.30000000000000004`.

JavaScript numbers are IEEE 754 64-bit binary floats. 0.1, 0.2, and 0.3 have no exact binary representation, so each is stored as the nearest representable value. Adding the two stored values for 0.1 and 0.2 rounds to a double slightly above the double nearest 0.3, so the strict comparison fails.

To compare floats, check that the difference is within a tolerance:

```js
Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON  // true
```

`Number.EPSILON` (about 2.22e-16) works for values near 1. For larger magnitudes, scale the tolerance or use a relative comparison. For money, store integer cents instead of fractional dollars.

Next step: if you have a specific comparison in your code that's misbehaving, paste it and I'll suggest the right tolerance.
