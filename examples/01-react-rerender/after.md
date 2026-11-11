Your `useEffect` is almost certainly updating a value it also depends on, so every render schedules the next one.

The loop:

1. Render → effect runs → `setItems(...)`
2. `items` changed → React re-renders
3. `items` is in the dependency array → effect runs again → back to 1

Fix it by depending on the input, not the output:

```js
useEffect(() => {
  fetchItems(query).then(setItems);
}, [query]); // was [items]
```

A second, sneakier version: an object you build during render (`{ page: 1 }`) is a new reference every time, so React always sees it as changed. Move it outside the component or wrap it in `useMemo`.

To confirm, add `console.count("render")` at the top of the component. A count that keeps climbing while you touch nothing means the loop is real.

If neither pattern matches, paste the component and I'll point to the exact line.
