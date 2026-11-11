<!-- Q: Is 0.1 + 0.2 === 0.3 true in JavaScript? -->

No, `0.1 + 0.2 === 0.3` is `false` in JavaScript, because `0.1 + 0.2` evaluates to `0.30000000000000004`.

JavaScript uses 64-bit binary floating point (IEEE 754). Numbers like 0.1 and 0.2 have no exact binary representation, so each is stored as a close approximation. Their sum lands slightly above the approximation of 0.3, and `===` compares exactly.

To compare safely, check that the difference is within a small tolerance:

```js
Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON  // true
```

For money, use integers (cents) instead of decimals: `10 + 20 === 30` is `true`.

Next step: if you hit this in real code, tell me where and I can suggest the right fix for that case.
