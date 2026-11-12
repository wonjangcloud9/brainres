<!-- Q: I'm a beginner. Why does this print 5 five times instead of 0 to 4?

```js
for (var i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
``` -->

It prints 5 five times because `var` creates one single `i` shared by the whole loop, and the `setTimeout` callbacks run after the loop has already finished and left `i` at 5.

**What happens, in order:**

1. The loop runs instantly. Each pass schedules a callback to run in 100 ms, but does not run it yet.
2. After the last pass, `i++` makes `i` equal 5, the check `5 < 5` fails, and the loop ends.
3. 100 ms later, all five callbacks run. Each one reads `i`, which is now 5.

The callback `() => console.log(i)` does not save the value of `i` at the time it was scheduled. It looks up `i` when it runs, and there is only one `i`.

**Fix: use `let` instead of `var`.**

```js
for (let i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
```

This prints 0, 1, 2, 3, 4. With `let`, each pass of the loop gets its own fresh `i`, so each callback remembers its own value.

The reason is scope. `var` is scoped to the whole function (or the file), while `let` is scoped to the block `{ ... }`, and in a `for` loop it is created anew per iteration.

Next step: run both versions in your terminal with `node file.js` and compare the output.
