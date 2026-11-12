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

A debounce wrapper delays a function call until calls stop arriving for `ms` milliseconds.

Each time the returned function runs, it does two things:

1. **`clearTimeout(t)`** cancels the timer from the previous call, if one is still pending.
2. **`t = setTimeout(...)`** starts a new timer. When it fires, it calls the original `fn` with the latest arguments.

So if the wrapped function is called 10 times within 300ms, only the last call's timer survives, and `fn` runs once, `ms` after the final call.

Example:

```js
const save = debounce((text) => console.log("saving", text), 300);

save("a"); // timer set
save("ab"); // "a" timer cancelled, new timer set
save("abc"); // "ab" timer cancelled, new timer set
// ~300ms later: logs "saving abc" once
```

Why the `t` variable lives in the closure: it persists across calls, so each call can reach the previous timer ID. Rest arguments `(...args)` and `fn(...args)` forward whatever the caller passed, and `fn` receives the arguments from the final call.

A common use is search-as-you-type or window resize handlers, where you want to act once the user pauses rather than on every keystroke.
