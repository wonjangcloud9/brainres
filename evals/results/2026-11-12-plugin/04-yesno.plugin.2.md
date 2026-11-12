<!-- Q: Is 0.1 + 0.2 === 0.3 true in JavaScript? -->

No. `0.1 + 0.2 === 0.3` is `false` in JavaScript, because `0.1 + 0.2` evaluates to `0.30000000000000004`.

JavaScript stores numbers as binary floating-point (IEEE 754 doubles). Neither 0.1 nor 0.2 has an exact binary representation, so each is slightly off. The errors add up to a result that differs from the stored value of 0.3.

To compare, check that the difference is smaller than a tolerance:

```js
Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON  // true
```

For money, use integer cents (`10 + 20 === 30`) instead of fractional values.
