<!-- Q: Can I use await inside a forEach loop? -->

No. `forEach` ignores the promise each callback returns, so the loop finishes before any `await` completes.

```js
const ids = [1, 2, 3];

ids.forEach(async (id) => {
  await save(id); // runs concurrently; forEach does not wait
});
console.log("done"); // logs before the saves finish
```

Use one of these instead:

- **Sequential:** `for...of` runs each `await` in order.
  ```js
  for (const id of ids) {
    await save(id);
  }
  ```
- **Parallel:** `Promise.all` starts every call at once and waits for all of them.
  ```js
  await Promise.all(ids.map((id) => save(id)));
  ```

Pick `for...of` when order or rate limits matter, and `Promise.all` when the calls are independent and can run together.
