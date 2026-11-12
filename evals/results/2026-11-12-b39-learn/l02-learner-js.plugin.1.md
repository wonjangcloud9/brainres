<!-- Q: I'm a beginner. Why does this print 5 five times instead of 0 to 4?

```js
for (var i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
``` -->

All five callbacks share one variable `i`, and they run after the loop has finished, when `i` is already 5.

**Why it happens**

1. `var i` creates a single `i` for the whole scope, not a new one per loop pass.
2. `setTimeout` doesn't run the function now. It schedules it for about 100 ms later.
3. The loop finishes immediately. `i` goes 0, 1, 2, 3, 4, and then becomes 5, which ends the loop.
4. After 100 ms, each callback runs `console.log(i)` and reads the current value of that one shared `i`, which is 5.

**Fix: use `let`**

```js
for (let i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
// prints 0 1 2 3 4
```

`let` gives each loop pass its own copy of `i`. Each callback keeps the copy from its own pass, so it prints 0 to 4.

Try changing `let` back to `var` and run both versions to see the difference. Then look up "closures" next, since this behavior is a classic example of one.
