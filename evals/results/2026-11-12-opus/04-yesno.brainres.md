<!-- Q: Is 0.1 + 0.2 === 0.3 true in JavaScript? -->

**No.** `0.1 + 0.2` evaluates to `0.30000000000000004`, so `0.1 + 0.2 === 0.3` is `false`.

JavaScript stores numbers as IEEE 754 64-bit binary floats. Neither `0.1` nor `0.2` has an exact binary representation, so their sum carries a tiny rounding error.

To compare floats, check that the difference falls within a tolerance:

```js
Math.abs((0.1 + 0.2) - 0.3) < Number.EPSILON // true
```

For money, store integer cents (`10 + 20 === 30`) instead of fractional dollars. You can confirm the result yourself by running `node -e "console.log(0.1 + 0.2)"`.
