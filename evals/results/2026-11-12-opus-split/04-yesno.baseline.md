<!-- Q: Is 0.1 + 0.2 === 0.3 true in JavaScript? -->

No, it's `false`.

```js
0.1 + 0.2 === 0.3   // false
0.1 + 0.2           // 0.30000000000000004
```

JavaScript numbers are IEEE 754 double-precision binary floats. Values like 0.1 and 0.2 have no exact binary representation, much like 1/3 has no exact decimal one. Each is stored as the nearest representable value, and adding those two approximations gives a result that lands on a slightly different double than the one closest to 0.3.

**How to compare floats instead:**

```js
// Tolerance comparison
Math.abs((0.1 + 0.2) - 0.3) < Number.EPSILON   // true
```

`Number.EPSILON` (about 2.22e-16) works for values near 1. For larger magnitudes, use a relative tolerance:

```js
const nearlyEqual = (a, b, eps = Number.EPSILON) =>
  Math.abs(a - b) <= eps * Math.max(Math.abs(a), Math.abs(b));
```

**For money or other exact decimals:** work in integer units (cents), use `BigInt`, or use a decimal library such as `decimal.js` or `big.js`.

This isn't specific to JavaScript. Python, Java, C, and any other language using IEEE 754 doubles behave the same way.
