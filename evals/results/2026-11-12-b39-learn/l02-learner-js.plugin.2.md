<!-- Q: I'm a beginner. Why does this print 5 five times instead of 0 to 4?

```js
for (var i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
``` -->

All five callbacks print the same `i`, and by the time they run, the loop has finished and `i` is 5.

**Why:**

1. `var i` creates one variable shared by the whole loop, not a new one per round.
2. `setTimeout` doesn't run its function right away. It schedules it for 100 ms later.
3. The loop finishes in a few microseconds, and `i` ends at 5 (the loop stops when `i < 5` fails).
4. After 100 ms, all five callbacks run. Each one reads the same `i`, which is now 5.

**Fix:** use `let` instead of `var`.

```js
for (let i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
// prints 0 1 2 3 4
```

`let` creates a fresh `i` for each round of the loop. Each callback keeps its own copy: 0, 1, 2, 3, 4.

Try changing `let` back to `var` and run both versions to see the difference. In new code, prefer `let` or `const` over `var`.
