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

This is a **debounce** function. It delays calling `fn` until a set amount of time has passed since the last time the returned function was called.

**How it works, step by step:**

1. **`debounce(fn, ms)`** takes the function you want to rate-limit (`fn`) and a wait time in milliseconds (`ms`). It returns a new function.

2. **`let t;`** creates a variable in the closure to hold the timer ID. Because it lives in the closure, it persists across calls to the returned function.

3. **The returned function** `(...args) => { ... }` accepts any arguments and forwards them to `fn`.

4. **`clearTimeout(t);`** cancels any previously scheduled call. If the function was called recently and a timer is still pending, it gets cleared.

5. **`t = setTimeout(() => fn(...args), ms);`** schedules a new call to `fn` after `ms` milliseconds, passing along the most recent arguments. The timer ID is saved in `t` so it can be cleared next time.

**Result:** If the returned function is called repeatedly in quick succession (say, on every keystroke), each call resets the timer. `fn` only actually runs once the calls stop for `ms` milliseconds.

**Example:**

```js
const search = debounce((query) => console.log("Searching:", query), 300);

search("a");
search("ap");
search("app");
search("appl");
search("apple");
// After 300ms of no further calls: "Searching: apple"
```

Only the last call runs, with its arguments.

**Common uses:** search-as-you-type inputs, window resize or scroll handlers, auto-saving drafts, and validating form fields after the user stops typing.

**Note:** This version doesn't return a value from `fn`, and it has no way to cancel the pending call or to run `fn` immediately on the leading edge. Libraries like Lodash's `debounce` add those options (`leading`, `trailing`, `cancel`, `flush`) if you need them.
