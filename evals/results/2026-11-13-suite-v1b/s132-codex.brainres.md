<!-- Q: Explain this:

```js
const total = items.reduce((sum, it) => sum + it.price * it.qty, 0);
``` -->

This line computes the total cost of all items by summing `price * qty` for each one.

`reduce` walks through `items` and carries a running value, `sum`, from one item to the next:

1. It starts with `sum = 0` (the second argument to `reduce`).
2. For each item `it`, it returns `sum + it.price * it.qty`.
3. That return value becomes `sum` for the next item.
4. After the last item, `reduce` returns the final `sum`, which is stored in `total`.

Worked example:

```js
const items = [
  { price: 10, qty: 2 },  // 20
  { price: 5,  qty: 3 },  // 15
];
// sum: 0 -> 20 -> 35
// total === 35
```

Two things to watch:
- **Keep the `0`.** Without it, `reduce` uses the first item object as the starting `sum`, so you'd get a string or `NaN` instead of a number. An empty `items` array would also throw a `TypeError`.
- If `price` or `qty` can arrive as strings (for example from form input), `*` converts them, but a missing field gives `NaN`. Validate or default them first.

Next, if you want, I can show a version that handles missing fields or rounds to cents.
