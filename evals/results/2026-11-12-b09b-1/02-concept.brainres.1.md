<!-- Q: What is a race condition? -->

A race condition is a bug where a program's result depends on the timing or order of concurrent operations, so the same code can give different results from run to run.

It happens when two or more threads or processes access shared data, at least one writes, and nothing forces them into a safe order.

**Example:** two threads each run `counter += 1` on a shared counter that starts at 0.

1. Thread A reads `counter` (0).
2. Thread B reads `counter` (0).
3. Thread A writes 1.
4. Thread B writes 1.

The final value is 1, not 2, because `counter += 1` is really three steps (read, add, write) and the threads interleaved between them.

**Common fixes:**

| Fix | How it helps |
|---|---|
| Lock or mutex | Only one thread runs the critical section at a time |
| Atomic operations | The read-modify-write happens as one indivisible step |
| Immutable data or message passing | Nothing shared gets mutated |
| Database transactions | The database serializes conflicting updates |

Race conditions are hard to debug because they often vanish under a debugger or logging, which changes the timing. Tools like ThreadSanitizer (`-fsanitize=thread` in clang/gcc) or Go's `-race` flag can detect them.

If you have code you suspect has one, paste it or point me to the file and I'll look.
