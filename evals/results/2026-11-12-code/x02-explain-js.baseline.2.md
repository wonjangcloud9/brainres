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

This is a **debounce** function: it delays running `fn` until calls have stopped coming in for `ms` milliseconds.

**Line by line**

```js
const debounce = (fn, ms) => {
```
Takes the function to wrap (`fn`) and a delay in milliseconds (`ms`).

```js
  let t;
```
Holds the pending timer ID. It lives in the closure, so it persists across calls to the returned function, and each debounced function gets its own `t`.

```js
  return (...args) => {
```
Returns a new function that captures whatever arguments it's called with.

```js
    clearTimeout(t);
```
Cancels any timer that's still waiting from a previous call. This is the "reset" step.

```js
    t = setTimeout(() => fn(...args), ms);
```
Starts a new timer. If no further call arrives within `ms`, `fn` runs with the most recent arguments.

**Behavior**

Calling the wrapped function repeatedly in quick succession keeps resetting the timer, so `fn` fires only once, `ms` after the last call.

```js
const onSearch = debounce((q) => fetchResults(q), 300);

onSearch("h");
onSearch("he");
onSearch("hel");   // only this one triggers fetchResults("hel"), 300ms later
```

**Common uses:** search-as-you-type inputs, window resize handlers, auto-save, anything where you only care about the final value after a burst of events.

**Limitations of this minimal version**

- **`this` is lost**: arrow functions don't bind `this`, so it won't work for methods that depend on it. Use a regular `function` and `fn.apply(this, args)` if needed.
- **No cancel/flush**: you can't abort a pending call (for example on component unmount).
- **Trailing only**: it never fires on the first call (a "leading" edge). Libraries like lodash's `debounce` offer these options.
- **Return value**: the wrapper returns `undefined`, not `fn`'s result, since `fn` runs asynchronously.

Don't confuse it with **throttle**, which guarantees `fn` runs at most once per interval during a burst rather than waiting for the burst to end.
