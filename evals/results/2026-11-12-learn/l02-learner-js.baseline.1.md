<!-- Q: I'm a beginner. Why does this print 5 five times instead of 0 to 4?

```js
for (var i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
``` -->

There are two things combining here: how `var` is scoped, and when `setTimeout` runs its callback.

**1. `var` creates one shared variable**

`var i` is scoped to the whole function (or the global scope), not to each loop iteration. So there is only a single `i` for the entire loop, and every callback refers to that same variable.

**2. `setTimeout` runs later**

`setTimeout` doesn't run the callback right away. It schedules it for after the current code finishes. So the loop runs all the way through first:

- `i` is 0, schedule a callback
- `i` is 1, schedule a callback
- ...
- `i` is 4, schedule a callback
- `i` becomes 5, the condition `i < 5` fails, and the loop ends

By the time 100ms passes and the callbacks run, `i` is already 5. All five callbacks read the same `i`, so you get `5` five times.

**The fix: use `let`**

```js
for (let i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
```

`let` is block-scoped, and in a `for` loop JavaScript creates a fresh copy of `i` for each iteration. Each callback captures its own `i`, so this prints `0 1 2 3 4`.

**Older workaround (you may see it in old code)**

An IIFE creates a new scope per iteration by passing `i` in as a parameter:

```js
for (var i = 0; i < 5; i++) {
  ((j) => setTimeout(() => console.log(j), 100))(i);
}
```

**Rule of thumb:** prefer `let` and `const`, and avoid `var` in new code.
