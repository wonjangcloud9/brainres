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

A debounce wrapper delays calling `fn` until `ms` milliseconds pass with no new calls, so a burst of calls produces one call.

How it works:

1. **`let t;`** holds the timer ID between calls. It lives in the closure, so every call to the returned function shares it.
2. **`clearTimeout(t)`** cancels the previously scheduled call, if any. Each new call resets the clock.
3. **`t = setTimeout(() => fn(...args), ms)`** schedules `fn` to run after `ms`. The arrow function captures the latest `args`.
4. **`(...args) =>`** passes through whatever arguments the caller uses, so the wrapper is transparent to `fn`.

Example with `ms = 300`:

```js
const log = debounce((x) => console.log(x), 300);
log(1); // timer set
log(2); // timer 1 cancelled, new timer set
log(3); // timer 2 cancelled, new timer set
// after 300ms of silence: prints 3
```

Only `3` prints, because the earlier timers were cancelled before they fired.

Common uses are search-as-you-type, window resize handlers, and autosave. The function returns no value, since the call happens later. If you need the result, you have to use a callback or a promise.
