<!-- Q: Is 0.1 + 0.2 === 0.3 true in JavaScript? -->

No, `0.1 + 0.2 === 0.3` evaluates to `false` in JavaScript.

JavaScript numbers are IEEE 754 double-precision floats, and 0.1 and 0.2 can't be represented exactly in binary. The sum is slightly off:

```javascript
0.1 + 0.2        // 0.30000000000000004
0.1 + 0.2 === 0.3 // false
```

To compare floats safely, check whether the difference is within a small tolerance:

```javascript
Math.abs((0.1 + 0.2) - 0.3) < Number.EPSILON  // true
```

`Number.EPSILON` is about 2.2e-16. For values larger than 1, a relative tolerance or a fixed tolerance you choose for your domain works better. For money, use integer cents or a decimal library rather than floats.
