<!-- Q: What is a race condition? -->

A race condition is a bug where a program's result depends on the timing or order of concurrent operations, such as threads, processes, or requests, that share state without proper coordination.

**Example:** two threads each run `counter += 1` on a shared counter that starts at 0.

1. Thread A reads `counter` (0).
2. Thread B reads `counter` (0).
3. Thread A writes 1.
4. Thread B writes 1.

The final value is 1, not 2, because `counter += 1` is really three steps (read, add, write), and the threads interleaved between them. The bug is intermittent: it only shows up when the timing lines up, which makes it hard to reproduce.

**Common fixes:**

| Approach | How it helps |
|---|---|
| Locks/mutexes | Only one thread touches the shared state at a time |
| Atomic operations | Make read-modify-write a single indivisible step |
| Immutable data / no shared state | Nothing to race on |
| Database transactions or unique constraints | Same idea for concurrent requests hitting one row |

A related variant is TOCTOU (time-of-check to time-of-use), where a check like "does this file exist?" becomes stale before the action that depends on it. That one also has security implications.

If you have code you suspect has a race, point me to the file and I can look for it.
