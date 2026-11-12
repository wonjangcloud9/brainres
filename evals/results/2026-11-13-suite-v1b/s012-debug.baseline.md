<!-- Q: In the browser console I get: TypeError: undefined is not a function at main.js:42. How do I track it down? -->

This error means something at line 42 is being called like a function (`foo()`), but `foo` is `undefined`. Here's how to find out which one.

**1. Go to the exact spot**
- Click the `main.js:42` link in the console to open it in the Sources panel.
- If the file is minified, click the `{}` (pretty-print) button at the bottom of the editor. The line number may shift, so check the column number in the stack trace too.

**2. Identify which call is `undefined`**
Look at line 42 for every `something()` or `obj.method()`. Candidates:
- A method name that's misspelled or has the wrong case (`obj.getItem` vs `obj.getitem`).
- A function from a library that hasn't loaded yet, or loaded under a different name.
- A callback argument that wasn't passed (`cb()` when `cb` is missing).
- An import that doesn't match the export (`import { foo }` when the module exports `default`, or vice versa).
- A function used before it's defined (e.g. `const fn = ...` assigned later, or a script-order problem).

**3. Confirm with a breakpoint**
- Click the line number 42 in Sources to set a breakpoint, then reload.
- When it pauses, hover over each called name, or type them in the Console (e.g. `typeof obj.method`). The one that prints `"undefined"` is your culprit.
- Alternatively, tick "Pause on exceptions" (the pause icon in Sources) to stop right at the throw, then inspect the Call Stack and Scope panels.

**4. Trace why it's undefined**
- Check the Call Stack panel: the caller may have passed the wrong argument.
- In the Network tab, confirm every script loaded (no 404s) and in the right order.
- If it's a library function, check the version and docs; the API may have changed.

**5. Quick-and-dirty alternative**
Temporarily add above line 42:
```js
console.log(typeof suspectFn, suspectFn);
```

If you paste line 42 (and a few lines around it), or tell me where the code lives in this project, I can point to the likely culprit directly.
