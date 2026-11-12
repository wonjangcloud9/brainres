<!-- Q: Is 0.1 + 0.2 === 0.3 true in JavaScript? -->

No. In JavaScript, `0.1 + 0.2 === 0.3` evaluates to `false`, because `0.1 + 0.2` produces `0.30000000000000004`.

The cause is binary floating-point: `0.1` and `0.2` have no exact binary representation, so the sum rounds to a value one step away from the closest double to `0.3`.

To compare such values safely, use a tolerance:

```js
Math.abs((0.1 + 0.2) - 0.3) < Number.EPSILON  // true
```

`Number.EPSILON` works for values near 1. For larger or smaller magnitudes, scale the tolerance to the values you compare.
