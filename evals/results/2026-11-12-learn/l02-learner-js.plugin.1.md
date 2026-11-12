<!-- Q: I'm a beginner. Why does this print 5 five times instead of 0 to 4?

```js
for (var i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
``` -->

All five callbacks share one `i`, because `var` creates a single variable for the whole loop, and by the time the callbacks run, that variable is 5.

**What happens, in order:**

1. The loop runs instantly. `i` goes 0, 1, 2, 3, 4, and then becomes 5, which ends the loop.
2. `setTimeout` doesn't run your function right away. It schedules it to run about 100 ms later, after the loop has finished.
3. When the five callbacks finally run, each one reads the same `i`, which is now 5. So you get 5 five times.

**Fix: use `let` instead of `var`.**

```js
for (let i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
// prints 0 1 2 3 4
```

`let` gives each loop pass its own fresh copy of `i`. Each callback remembers the copy from its own pass, so it prints 0, 1, 2, 3, 4.

**Why `var` behaves this way:** `var` is scoped to the whole function (or the whole file), not to the loop body. `let` is scoped to the nearest `{ }` block, and a `for` loop with `let` makes a new block scope on every pass.

For new code, prefer `let` (or `const` when the value never changes) and avoid `var`. Try changing `var` to `let` in your snippet and run it to see the difference.
