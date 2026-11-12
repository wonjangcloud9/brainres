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

This is a **debounce** function: it delays running `fn` until calls have stopped for `ms` milliseconds. If the wrapper is called again before the delay expires, the timer restarts.

**Line by line**

```js
const debounce = (fn, ms) => {
```
Takes the function to wrap (`fn`) and the quiet period in milliseconds (`ms`).

```js
  let t;
```
Holds the timer ID. It lives in the closure, so every call to the returned function shares the same `t`.

```js
  return (...args) => {
```
Returns a new function that collects whatever arguments it's called with.

```js
    clearTimeout(t);
```
Cancels any pending timer from a previous call. This is what "resets" the wait.

```js
    t = setTimeout(() => fn(...args), ms);
```
Schedules `fn` to run after `ms` and stores the new timer ID.

**Example**

```js
const onResize = debounce(() => console.log("resized"), 300);

window.addEventListener("resize", onResize);
```
While the user drags the window, `resize` fires dozens of times. Each call cancels the previous timer, so `"resized"` logs only once, 300ms after the last event.

**Common uses**
- Search-as-you-type inputs (fire the request after the user pauses)
- Window resize/scroll handlers
- Auto-save

**Caveats**
- **`this` is lost.** The arrow functions don't forward `this`, so it won't work for methods that rely on it. Use a `function` wrapper with `fn.apply(this, args)` if you need that.
- **Trailing-only.** It runs on the *last* call, not the first. A "leading" variant (run immediately, then ignore calls until quiet) needs extra logic.
- **No return value.** The wrapper returns `undefined`, not `fn`'s result, because `fn` runs asynchronously.
- **No cancel.** You can't abort a pending call from outside. Libraries like lodash add `.cancel()` and `.flush()`.

**Debounce vs. throttle:** debounce waits for silence, while throttle runs at most once per interval during continuous activity.
