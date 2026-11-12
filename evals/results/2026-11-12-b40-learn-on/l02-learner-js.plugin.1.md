<!-- Q: I'm a beginner. Why does this print 5 five times instead of 0 to 4?

```js
for (var i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
``` -->

Because `var` makes one shared `i` for the whole loop, and the `setTimeout` callbacks run after the loop has finished, when `i` is already 5.

**Fix: change `var` to `let`.**

```js
for (let i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
// prints 0 1 2 3 4
```

**What happens with `var`:**

1. The loop runs 5 times. Each pass schedules a callback to run in 100 ms, but it doesn't run it yet.
2. The loop ends when `i++` makes `i` equal 5, and the check `5 < 5` fails.
3. After 100 ms, all 5 callbacks run. They read the same `i`, which is now 5, so each prints 5.

**Why `let` works:** `let` gives each pass of the loop its own copy of `i`. The first callback keeps the `i` that was 0, the second keeps the one that was 1, and so on.

A callback that remembers variables from where it was created is called a *closure*. Here, all five closures with `var` point at the same variable. With `let`, each points at its own.

Prediction question: if you keep `var` but change the delay to `0` (`setTimeout(..., 0)`), what do you think it prints? Try it and compare with your guess.
