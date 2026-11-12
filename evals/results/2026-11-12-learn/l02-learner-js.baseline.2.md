<!-- Q: I'm a beginner. Why does this print 5 five times instead of 0 to 4?

```js
for (var i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
``` -->

Two things combine to cause this: `var` scoping and when `setTimeout` runs.

**1. `var` creates one shared variable.**
`var i` is scoped to the whole function (or the global scope here), not to each loop iteration. So there is only a single `i` for the entire loop.

**2. `setTimeout` callbacks run later.**
The loop finishes almost instantly, and the callbacks wait until after it's done (about 100ms). By then, `i` has been incremented to `5`, which is the value that made the condition `i < 5` false and ended the loop.

When each callback finally runs, it looks up `i`, finds the one shared variable, and sees `5`. That's why you get `5` five times.

**The fix: use `let`**

```js
for (let i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
// 0 1 2 3 4
```

`let` creates a new `i` for each loop iteration, so each callback remembers its own copy.

**Older fix (what people did before `let`):** wrap the body in a function so each iteration gets its own variable:

```js
for (var i = 0; i < 5; i++) {
  (function (j) {
    setTimeout(() => console.log(j), 100);
  })(i);
}
```

**Rule of thumb:** prefer `let` and `const`, and avoid `var` in modern JavaScript. This closure-in-a-loop behavior is one of the main reasons why.
