<!-- Q: Can I use await inside a forEach loop? -->

Technically yes, but it won't do what you expect. `forEach` ignores the promises returned by an async callback, so the loop doesn't wait for anything.

```js
items.forEach(async (item) => {
  await save(item);   // awaits only inside this callback
});
console.log("done");  // runs before any save() finishes
```

Each callback runs on its own, so the `await` pauses only that callback. The code after `forEach` continues immediately, and errors become unhandled rejections.

**Pick the fix by what you need:**

| Goal | Use |
|---|---|
| One at a time, in order | `for (const item of items) { await save(item); }` |
| All at once, wait for all | `await Promise.all(items.map(save))` |
| All at once, tolerate failures | `await Promise.allSettled(items.map(save))` |

Use `for...of` when order matters or when you must limit load on an API. Use `Promise.all` when the calls are independent and you want speed.

If you show me the loop you're working with, I can rewrite it.
