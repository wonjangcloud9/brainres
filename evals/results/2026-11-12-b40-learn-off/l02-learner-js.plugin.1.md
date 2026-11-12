<!-- Q: I'm a beginner. Why does this print 5 five times instead of 0 to 4?

```js
for (var i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
``` -->

All five callbacks share one `i` because `var` makes a single variable for the whole loop, and the callbacks run after the loop has finished, when `i` is 5.

1. The loop runs 5 times. Each pass schedules a callback with `setTimeout` but doesn't run it yet.
2. After the last pass, `i++` makes `i` equal to 5, and the check `i < 5` fails, so the loop stops.
3. About 100 ms later, the five callbacks run. Each one reads the same `i`, which is now 5.

**Fix:** use `let` instead of `var`. `let` creates a new `i` for each pass of the loop, so each callback keeps its own value.

```js
for (let i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
// prints 0 1 2 3 4
```

Use `let` (or `const`) instead of `var` in new code. `var` has this shared-variable behavior, and `let` avoids it.
