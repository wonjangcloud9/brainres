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

`debounce` wraps a function so it only runs after calls have stopped for `ms` milliseconds; each new call cancels the pending one and restarts the timer.

**How it works, line by line**

- `let t;` holds the pending timer ID. It lives in the closure, so every call to the returned function shares the same `t`.
- `return (...args) => { ... }` returns the wrapper. `...args` collects whatever arguments the caller passes.
- `clearTimeout(t);` cancels the previous scheduled call, if any. On the first call `t` is `undefined`, which `clearTimeout` safely ignores.
- `t = setTimeout(() => fn(...args), ms);` schedules `fn` to run after `ms` and saves the new timer ID. The arrow function captures the latest `args`.

**Worked example**

```js
const onSearch = debounce((q) => console.log("search:", q), 300);

onSearch("a");     // t=0ms,   timer set
onSearch("ab");    // t=100ms, "a" call cancelled, new timer set
onSearch("abc");   // t=200ms, "ab" call cancelled, new timer set
// t=500ms: logs "search: abc" once
```

Three calls, one execution, using only the last arguments. That is why it suits search boxes, window resize handlers, and autosave: you avoid firing on every keystroke or event.

**Limits of this version**

- It drops `this`. Because the wrapper is an arrow function, `fn` is called without the caller's `this`, so it won't work as a method that relies on `this` unless `fn` is already bound.
- It only fires on the trailing edge (after the pause). It can't run immediately on the first call.
- There is no `cancel()` method, so you can't abort a pending call, for example on component unmount.
- The return value of `fn` is lost, since the call happens inside a timer.

If you need one of these, I can show a version with `cancel()` or leading-edge support.
