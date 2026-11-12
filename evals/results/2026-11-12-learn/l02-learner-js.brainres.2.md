<!-- Q: I'm a beginner. Why does this print 5 five times instead of 0 to 4?

```js
for (var i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
``` -->

It prints 5 five times because `var` creates one single `i` shared by the whole loop, and the callbacks run after the loop has already finished and set `i` to 5.

**What happens, in order:**

1. The loop runs 5 times. Each pass schedules a callback with `setTimeout` but does not run it yet.
2. After the last pass, `i++` makes `i` equal to 5, and the check `i < 5` fails, so the loop ends.
3. About 100 ms later, the 5 callbacks run. Each one reads `i`, which is now 5.

The callbacks don't save the value `i` had when they were created. They look up `i` at the moment they run, and by then there is only one `i`, holding 5.

**Fix: use `let` instead of `var`.**

```js
for (let i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
```

This prints 0, 1, 2, 3, 4. With `let`, JavaScript creates a new `i` for each pass of the loop, so each callback keeps its own copy.

Change `var` to `let` in your file and run it to confirm. As a habit, prefer `let` and `const` over `var`.
