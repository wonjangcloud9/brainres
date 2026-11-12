<!-- Q: I'm a beginner. Why does this print 5 five times instead of 0 to 4?

```js
for (var i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
``` -->

All five callbacks share one `i`, because `var` creates a single variable for the whole loop, and the callbacks run after the loop has finished, when `i` is 5.

1. The loop runs with `i` = 0, 1, 2, 3, 4. Each pass schedules a function with `setTimeout` but doesn't run it yet.
2. After `i` = 4, the loop does `i++`. That makes `i` = 5, the check `5 < 5` fails, and the loop ends.
3. About 100 ms later, the five scheduled functions run. Each one reads the same `i`, which is now 5.

The fix is to use `let` instead of `var`:

```js
for (let i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
// prints 0 1 2 3 4
```

`let` creates a new `i` for each pass of the loop, so each callback keeps its own copy. In modern code, use `let` or `const` and avoid `var`.

Try changing `let` back to `var` and run it both ways to see the difference.
