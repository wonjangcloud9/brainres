<!-- Q: Can I use await inside a forEach loop? -->

Yes, you can write `await` inside a `forEach` callback if the callback is `async`, but `forEach` won't wait for it, so the loop doesn't pause and the code after it runs before the awaits finish.

```js
// Broken: "done" logs first, and errors become unhandled rejections
items.forEach(async (item) => {
  await save(item);
});
console.log("done");
```

`forEach` ignores the promises the callback returns. Fix it by picking the behavior you want:

**Sequential (one at a time):**
```js
for (const item of items) {
  await save(item);
}
```

**Parallel (all at once, wait for all):**
```js
await Promise.all(items.map((item) => save(item)));
```

Use `for...of` when order matters or you need to limit load on a server. Use `Promise.all` with `map` when the calls are independent. If you have a specific loop in mind, paste it and I'll rewrite it.
