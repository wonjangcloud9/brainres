<!-- Q: Is 0.1 + 0.2 === 0.3 true in JavaScript? -->

No, it evaluates to `false`. JavaScript uses IEEE 754 double-precision floats, and neither 0.1 nor 0.2 can be stored exactly in binary, so the sum comes out as `0.30000000000000004`, which is not the same double as `0.3`.

To compare floats, check that the difference is within a tolerance:

```js
Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON  // true
```

`Number.EPSILON` (~2.22e-16) works here because the values are near 1 or below. For larger magnitudes, scale the tolerance to the numbers you compare. For money, use integer cents instead of floats.

Next step: paste `0.1 + 0.2` into your browser console or `node -e "console.log(0.1+0.2)"` to see the result yourself.
