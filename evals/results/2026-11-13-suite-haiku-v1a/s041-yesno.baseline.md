<!-- Q: Can I use await inside a forEach loop? -->

**Not directly.** `await` is only valid inside an `async` function, and `forEach` doesn't wait for promises. If you pass an `async` callback, each iteration starts but `forEach` ignores the returned promises:

```js
const items = [1, 2, 3];

items.forEach(async (item) => {
  await someAsyncWork(item);
  console.log(item);
});

console.log("done"); // runs before any of the logs above
```

Use one of these instead:

**Sequential** (each iteration waits for the previous one), with `for...of`:

```js
for (const item of items) {
  await someAsyncWork(item);
}
```

**Parallel** (all start at once, and you wait for all to finish), with `map` and `Promise.all`:

```js
await Promise.all(items.map((item) => someAsyncWork(item)));
```

Use `for...of` when order matters or you want to limit concurrency. Use `Promise.all` when the operations are independent and you want speed. Note that `Promise.all` rejects as soon as one promise fails, so use `Promise.allSettled` if you need every result regardless of errors.
