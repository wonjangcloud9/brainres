<!-- Q: Explain this:

```js
const total = items.reduce((sum, it) => sum + it.price * it.qty, 0);
``` -->

This line computes the total cost of a list of items by summing `price × quantity` for each one.

**Breaking it down**

- `items` is an array of objects, each with a `price` and a `qty` (e.g. `{ price: 9.99, qty: 3 }`).
- `reduce` walks through the array, carrying a running value (the accumulator) from one item to the next and returning the final value.
- `(sum, it) => sum + it.price * it.qty` is the callback:
  - `sum` is the running total so far.
  - `it` is the current item.
  - It returns the new running total: the previous sum plus this item's line total.
- `0` is the initial value of `sum`, so the first iteration starts from zero.

**Example**

```js
const items = [
  { price: 10, qty: 2 },  // 20
  { price: 5,  qty: 3 },  // 15
  { price: 1,  qty: 10 }, // 10
];

const total = items.reduce((sum, it) => sum + it.price * it.qty, 0);
// total = 45
```

Step by step: `0 → 20 → 35 → 45`.

**Things to know**

- The `0` initial value matters. Without it, `reduce` would use the first item object as the starting `sum`, producing nonsense like `[object Object]...`. With it, an empty array safely returns `0` instead of throwing a `TypeError`.
- Floating-point prices can produce results like `0.30000000000000004`. For money, store prices in integer cents, or round at the end (e.g. `Math.round(total * 100) / 100`).
- If `price` or `qty` can be missing or a string, you'll get `NaN` or string concatenation surprises, so validate or coerce inputs first.
