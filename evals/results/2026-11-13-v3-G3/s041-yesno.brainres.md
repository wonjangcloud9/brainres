<!-- Q: Can I use await inside a forEach loop? -->

Syntactically yes, but it won't do what you expect: `forEach` ignores the promises your async callback returns, so it doesn't wait for any iteration, and the code after the loop runs before the awaits finish.

```js
const ids = [1, 2, 3];

ids.forEach(async (id) => {
  await save(id);
  console.log('saved', id);
});
console.log('done'); // prints first, before any "saved"
```

Errors thrown inside the callback also become unhandled rejections, because nothing catches them.

**Sequential** (one at a time, in order): use `for...of`.

```js
for (const id of ids) {
  await save(id);
}
console.log('done'); // runs after all saves
```

**Parallel** (all at once, then wait): use `map` with `Promise.all`.

```js
await Promise.all(ids.map((id) => save(id)));
console.log('done');
```

Use `Promise.allSettled` instead of `Promise.all` if one failure shouldn't reject the whole batch. For large arrays, limit concurrency (for example with `p-limit`) rather than firing everything at once.
