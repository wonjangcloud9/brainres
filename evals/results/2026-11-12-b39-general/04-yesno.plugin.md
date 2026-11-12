<!-- Q: Is 0.1 + 0.2 === 0.3 true in JavaScript? -->

No. `0.1 + 0.2` evaluates to `0.30000000000000004`, so `0.1 + 0.2 === 0.3` is `false`.

JavaScript uses 64-bit binary floating point (IEEE 754), and 0.1, 0.2 and 0.3 can't be stored exactly in binary. The tiny rounding errors in 0.1 and 0.2 add up to a result slightly above the stored 0.3.

To compare, use a tolerance:

```js
Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON  // true
```

For money, store integer cents (`10 + 20 === 30`) instead of fractional dollars.
