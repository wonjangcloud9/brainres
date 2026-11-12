<!-- Q: In the browser console I get: TypeError: undefined is not a function at main.js:42. How do I track it down? -->

Line 42 of `main.js` is calling something that is `undefined`, so find the call on that line and check what it really is.

1. **Open the line.** In DevTools, click `main.js:42` in the console error, which jumps to Sources. If the file is minified or bundled, enable source maps so it shows your original code.
2. **Break on the error.** In Sources, turn on "Pause on exceptions" (the stop-sign icon). Reload, and execution stops at the failing call with all variables inspectable.
3. **Check each callee on the line.** In the console, evaluate each function-like piece with `typeof`. For example, if line 42 is `user.getName()`, run `typeof user.getName`. Anything other than `"function"` is your culprit.
4. **Read the call stack.** The right-hand panel shows who called it. The bug is often upstream, where a value was never set.

Common causes:

| Cause | Example |
|---|---|
| Typo or wrong case | `arr.forEech(...)` |
| Method used before it loads | script runs before a library's `<script>` tag |
| Wrong import | `import foo from "x"` when it needs `import { foo } from "x"` |
| Callback never passed | `cb()` where `cb` is `undefined` |

The error text is usually clearer in the stack trace than in the one-line message, so expand it in the console.

If you paste line 42 and a few lines around it, I can point to the exact cause. If the project is on disk, tell me the path and I'll read it directly.
