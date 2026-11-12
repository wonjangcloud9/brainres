<!-- Q: I'm a beginner. Why does this print 5 five times instead of 0 to 4?

```js
for (var i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
``` -->

Because `var` creates one shared `i` for the whole loop, and the callbacks run after the loop has already finished, when `i` is 5.

**What happens, step by step:**

1. The loop runs instantly. It schedules 5 callbacks, then `i++` makes `i` equal 5, and the loop ends.
2. About 100 ms later, the 5 callbacks run.
3. Each callback looks up `i` at that moment. They all share the same `i`, which is now 5, so each prints 5.

The callback doesn't save the value `i` had when it was scheduled. It keeps a reference to the variable itself.

**Fix: use `let` instead of `var`.**

```js
for (let i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
```

This prints 0, 1, 2, 3, 4. `let` gives each loop pass its own fresh `i`, so each callback keeps its own value.

The reason is scope. `var` is scoped to the whole function (or file), so there is only one `i`. `let` is scoped to each block `{ }`, so there are five.

Next step: run both versions in your browser console or with `node file.js` and compare the output.
