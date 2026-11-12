<!-- Q: Is 0.1 + 0.2 === 0.3 true in JavaScript? -->

No, it's `false`.

```js
0.1 + 0.2            // 0.30000000000000004
0.1 + 0.2 === 0.3    // false
```

JavaScript numbers are IEEE 754 double-precision floats. Neither 0.1 nor 0.2 can be represented exactly in binary, so each is stored as the nearest representable value. When you add those approximations, the rounding errors add up, and the result lands on a different double than the one closest to 0.3.

This isn't specific to JavaScript. Python, Java, C, and any other language using binary floating point behave the same way.

**How to compare instead:**

```js
// Tolerance-based comparison
Math.abs((0.1 + 0.2) - 0.3) < Number.EPSILON   // true
```

`Number.EPSILON` (about 2.22e-16) works for values near 1. For larger magnitudes, scale the tolerance:

```js
const nearlyEqual = (a, b) =>
  Math.abs(a - b) <= Number.EPSILON * Math.max(Math.abs(a), Math.abs(b));
```

**For money or other exact decimals,** don't use floats at all:
- Store integer cents (`10 + 20 === 30`), or
- Use `BigInt` for whole numbers, or a decimal library like `decimal.js` or `big.js`.
