<!-- Q: What is a race condition? -->

A race condition is a bug where a program's result depends on the timing of two or more concurrent operations, so the same code can give different results from run to run.

**Example:** two threads each run `counter += 1` on a shared counter that starts at 0.

1. Thread A reads `counter` (0).
2. Thread B reads `counter` (0).
3. Thread A writes 1.
4. Thread B writes 1.

The counter should be 2 but is 1. The increment looks like one step, but it is really read, add, write, and the threads interleaved between those steps.

**Why they are hard to find:** they depend on scheduling, so they often vanish under a debugger or in tests and show up only under load.

**Common fixes:**

- **Locks (mutexes):** only one thread enters the critical section at a time.
- **Atomic operations:** the read-modify-write happens as one indivisible step.
- **Immutable data or message passing:** threads don't share mutable state.
- **Database transactions or constraints:** the same idea for concurrent requests that touch the same row.

Race conditions also occur outside threads, such as two processes writing one file, or a check-then-act gap like "if the file doesn't exist, create it" (a TOCTOU bug).

If you have a specific piece of code you suspect, paste it and I'll point out where the race is.
