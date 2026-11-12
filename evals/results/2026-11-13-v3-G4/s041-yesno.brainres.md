<!-- Q: Can I use await inside a forEach loop? -->

Yes, syntactically, but it won't behave as you expect: `forEach` ignores the promises returned by an `async` callback, so the loop doesn't wait and code after it runs before the awaits finish.

```js
items.forEach(async (item) => {
  await save(item);   // runs, but forEach doesn't wait for it
});
console.log("done");  // prints before the saves finish
```

Errors inside the callback also become unhandled rejections instead of reaching your `try/catch`.

**Fixes, depending on what you need:**

| Goal | Use |
|---|---|
| One at a time, in order | `for (const item of items) { await save(item); }` |
| All in parallel, wait for all | `await Promise.all(items.map(item => save(item)));` |
| Parallel, but tolerate failures | `await Promise.allSettled(items.map(save));` |

Use the `for...of` form by default; it's the closest to what people expect `forEach` to do. Switch to `Promise.all` only if the iterations are independent and you want speed (and be aware it can overwhelm an API with many items).

If you point me to the loop in your code, I can rewrite it.
