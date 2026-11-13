<!-- Q: Can I use await inside a forEach loop? -->

**No, not usefully.** `forEach` ignores the promise your async callback returns, so the loop doesn't wait. The code after it runs before the awaited work finishes.

```js
// Broken: logs "done" before any file is saved
files.forEach(async (file) => {
  await save(file);
});
console.log("done");
```

Use one of these instead:

**Sequential (one at a time):**
```js
for (const file of files) {
  await save(file);
}
console.log("done"); // runs after all saves
```

**Parallel (all at once, then wait):**
```js
await Promise.all(files.map((file) => save(file)));
console.log("done");
```

| Need | Use |
|---|---|
| Order matters, or rate limits apply | `for...of` |
| Independent tasks, faster overall | `Promise.all` + `map` |

Errors also get lost with `forEach`. A rejection inside the callback becomes an unhandled rejection, so a surrounding `try/catch` won't catch it. Both alternatives above propagate errors to your `await`.

Pick `for...of` if the order of operations matters; otherwise use `Promise.all`.
