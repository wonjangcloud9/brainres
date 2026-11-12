<!-- Q: Is 0.1 + 0.2 === 0.3 true in JavaScript? -->

No. In JavaScript, `0.1 + 0.2 === 0.3` is `false`, because `0.1 + 0.2` evaluates to `0.30000000000000004`.

Both 0.1 and 0.2 are stored as binary floating-point (IEEE 754 doubles), and neither has an exact binary representation. The small rounding errors add up to a result that differs from the double closest to 0.3.

To compare floats, check that they're within a small tolerance:

```js
Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON  // true
```

For money, use integers (cents) or a decimal library instead of floats.
