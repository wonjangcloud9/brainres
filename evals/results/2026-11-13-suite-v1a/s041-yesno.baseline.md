<!-- Q: Can I use await inside a forEach loop? -->

Technically yes, but it won't do what you expect. `forEach` ignores the return value of its callback, so if you make the callback `async`, each iteration starts a promise and `forEach` moves on without waiting for it.

```js
const items = [1, 2, 3];

items.forEach(async (item) => {
  await doSomething(item);
  console.log(item);
});

console.log("done"); // runs BEFORE any of the awaits finish
```

The `await` works inside each callback, but nothing outside waits for them, and errors become unhandled promise rejections.

**Alternatives:**

1. **Sequential**, one at a time, in order: use `for...of`.
   ```js
   for (const item of items) {
     await doSomething(item);
   }
   ```

2. **Parallel**, all at once, then wait for all: use `map` with `Promise.all`.
   ```js
   await Promise.all(items.map((item) => doSomething(item)));
   ```
   Use `Promise.allSettled` if you don't want one failure to reject the whole batch.

3. **Parallel with a concurrency limit**: use a library like `p-limit` when the list is large or you're hitting rate limits.

Rule of thumb: if you need `await` in a loop, use `for...of` (sequential) or `Promise.all` + `map` (parallel), not `forEach`.
