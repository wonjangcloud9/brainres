<!-- Q: Can you explain this?

```js
const debounce = (fn, ms) => {
  let t;
  return (...args) => {
    clearTimeout(t);
    t = setTimeout(() => fn(...args), ms);
  };
};
``` -->

`debounce` wraps a function so it only runs after calls have stopped for `ms` milliseconds; every new call cancels the pending one and restarts the timer.

**How it works, line by line:**

1. `let t;` holds the timer ID. It lives in the closure, so every call to the returned function shares the same `t`.
2. `return (...args) => {...}` returns the wrapper you actually call. `...args` collects whatever arguments it receives.
3. `clearTimeout(t)` cancels the previous scheduled run, if any. On the first call `t` is `undefined`, and `clearTimeout(undefined)` does nothing, so that is safe.
4. `t = setTimeout(() => fn(...args), ms)` schedules `fn` to run in `ms` milliseconds with the latest arguments, and saves the new timer ID.

**Example:**

```js
const onSearch = debounce((q) => fetchResults(q), 300);

onSearch("c");     // scheduled for t=300, then cancelled
onSearch("ca");    // scheduled for t=~100+300, then cancelled
onSearch("cat");   // no more calls, so fetchResults("cat") runs once
```

If the user types three letters quickly, you make one request instead of three. Typical uses are search boxes, window resize handlers, and autosave.

**Limits of this version:**

- It drops `this`. The arrow functions don't bind it, so debouncing a method that uses `this` breaks unless you bind it first.
- The return value of `fn` is lost, because `setTimeout` discards it.
- There is no `cancel()` or `flush()`. If you need to cancel on unmount (for example in React), add one or use lodash's `debounce`.

Next step: if you want, I can add a `cancel` method to this version.
