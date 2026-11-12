<!-- Q: I'm a beginner. Why does this print 5 five times instead of 0 to 4?

```js
for (var i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
``` -->

Because `var i` creates one single variable shared by all five callbacks, and the loop has already finished and set it to 5 by the time any callback runs.

**What happens, in order**

1. The loop runs instantly. Each pass schedules a callback with `setTimeout` and then adds 1 to `i`.
2. After the fifth pass, `i++` makes `i` equal 5, and the check `5 < 5` fails, so the loop stops.
3. About 100 ms later, the five callbacks run. Each one reads `i`, and `i` is now 5.

The callbacks don't save the value `i` had when they were scheduled. They look up `i` when they run. With `var`, there is only one `i` to look up.

**The fix: change `var` to `let`**

```js
for (let i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
// prints 0 1 2 3 4
```

`let` gives each pass of the loop its own fresh copy of `i`. Each callback keeps the copy from its own pass.

**Terms**
- **Scope:** the region of code where a variable exists. `var` is scoped to the whole function (or the file, outside a function). `let` is scoped to the nearest `{ }` block, and a `for` loop gets a new block each pass.
- **Callback:** the function you pass to `setTimeout`, which runs later.

Prefer `let` (or `const` for values that never change) over `var` in new code.

**Try this:** what would this print, and why?

```js
let j = 0;
for (; j < 3; j++) {
  setTimeout(() => console.log(j), 100);
}
```

Here `let` is declared outside the loop. Make your guess before you run it.
