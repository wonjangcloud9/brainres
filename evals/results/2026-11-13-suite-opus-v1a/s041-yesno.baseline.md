<!-- Q: Can I use await inside a forEach loop? -->

Technically yes, but it won't do what you probably expect. `forEach` doesn't wait for the promise your async callback returns, so all iterations start at once and the code after the loop runs before any of them finish.

```js
// ❌ Doesn't wait
items.forEach(async (item) => {
  await process(item);
});
console.log("done"); // runs before any process() completes
```

Errors thrown inside also become unhandled rejections instead of propagating to a surrounding `try/catch`.

## What to use instead

**Sequential (one at a time, in order):** use `for...of`

```js
for (const item of items) {
  await process(item);
}
console.log("done"); // runs after all complete
```

**Parallel (all at once, wait for all):** use `Promise.all` with `map`

```js
await Promise.all(items.map(item => process(item)));
console.log("done");
```

**Parallel, but tolerate individual failures:** use `Promise.allSettled`

```js
const results = await Promise.allSettled(items.map(process));
// each result: { status: "fulfilled", value } or { status: "rejected", reason }
```

**Limited concurrency** (e.g. at most 5 at a time, to avoid hammering an API): use a library like `p-limit`, or process in batches.

## Which to pick

- Order matters or each step depends on the previous one: `for...of`
- Independent tasks where speed matters: `Promise.all`
- Large lists or rate-limited resources: limited concurrency

The same caveat applies to `filter`, `reduce`, `some`, etc. None of them are promise-aware.
