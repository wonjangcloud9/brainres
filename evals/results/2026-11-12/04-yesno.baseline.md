<!-- Q: Is 0.1 + 0.2 === 0.3 true in JavaScript? -->

No, it evaluates to `false`.

JavaScript uses IEEE 754 double-precision floats, and neither 0.1 nor 0.2 can be represented exactly in binary. The sum comes out as:

```js
0.1 + 0.2  // 0.30000000000000004
```

which differs slightly from the double closest to 0.3.

To compare floats, use a tolerance:

```js
Math.abs((0.1 + 0.2) - 0.3) < Number.EPSILON  // true
```

For money or other exact decimal needs, work in integer units (e.g., cents) or use a decimal library.
