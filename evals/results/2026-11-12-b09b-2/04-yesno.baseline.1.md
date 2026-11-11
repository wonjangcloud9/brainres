<!-- Q: Is 0.1 + 0.2 === 0.3 true in JavaScript? -->

No, it evaluates to `false`.

JavaScript uses IEEE 754 double-precision floats, and neither 0.1 nor 0.2 can be represented exactly in binary. Their sum comes out as:

```js
0.1 + 0.2        // 0.30000000000000004
0.1 + 0.2 === 0.3 // false
```

To compare floats, use a tolerance:

```js
Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON  // true
```

For money or other cases needing exact decimals, work in integer units (e.g. cents) or use a decimal library.
