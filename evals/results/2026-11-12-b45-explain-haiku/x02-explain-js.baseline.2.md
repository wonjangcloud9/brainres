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

This is a **debounce** function. It delays calling `fn` until a burst of calls has stopped for `ms` milliseconds.

**How it works, step by step:**

1. **`debounce(fn, ms)`** takes the function you want to wrap and a wait time in milliseconds. It returns a new function.

2. **`let t;`** creates a variable in the closure to hold the current timer ID. It persists across calls to the returned function.

3. **The returned function** `(...args) => { ... }` accepts any arguments and forwards them to `fn`.

4. **`clearTimeout(t);`** cancels any previously scheduled call. If the wrapper was called recently and its timer hasn't fired yet, that timer is dropped.

5. **`t = setTimeout(() => fn(...args), ms);`** schedules a new call to `fn` after `ms` milliseconds and stores its ID in `t`.

**Result:** If the wrapper is called repeatedly, each call resets the timer. `fn` only runs once, `ms` milliseconds after the *last* call.

**Example:**

```js
const log = debounce((msg) => console.log(msg), 300);

log("a");   // timer set
log("b");   // "a" timer cancelled, new timer set
log("c");   // "b" timer cancelled, new timer set
// ...300ms of silence...
// prints "c"
```

**Common uses:**
- Search-as-you-type, so the request fires after the user stops typing
- Window resize or scroll handlers, so expensive layout work runs once at the end
- Auto-saving a form after edits pause

**Compared with throttle:** Debounce waits for quiet, so `fn` may never run during continuous activity. Throttle runs `fn` at most once per interval, even during continuous activity.
