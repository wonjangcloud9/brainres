<!-- Q: Can I use await inside a forEach loop? -->

Yes, but only inside an `async` callback, and `forEach` won't wait for it, so the code after the loop runs before the awaited work finishes.

`forEach` ignores the promise each callback returns. Each iteration starts, hits its `await`, and hands control back immediately. Errors thrown inside the callback also become unhandled rejections, because nothing catches them.

```js
// Broken: "done" logs first
items.forEach(async (item) => {
  await save(item);
});
console.log("done");
```

Use one of these instead:

```js
// Sequential: one at a time, in order
for (const item of items) {
  await save(item);
}

// Parallel: all at once, wait for all
await Promise.all(items.map((item) => save(item)));
```

| Need | Use |
|---|---|
| Order matters, or you must limit load | `for...of` |
| Independent tasks, speed matters | `Promise.all` with `map` |

If you have many items, `Promise.all` fires every request at once, so use a concurrency limiter such as `p-limit` to cap it.

If you share the loop you're working on, I can say which pattern fits it.
