<!-- Q: What is a race condition? -->

A race condition is a bug where a program's result depends on the timing of two or more threads or processes that touch the same shared data, and at least one of them writes to it.

**Why it happens:** an operation that looks like one step is often several steps, and another thread can run in between them.

**Worked example:** two threads each run `count += 1` on a shared `count = 0`. That line is really three steps:

1. Read `count` into a register.
2. Add 1.
3. Write the result back.

One bad interleaving:

| Step | Thread A | Thread B | `count` in memory |
|---|---|---|---|
| 1 | reads 0 | | 0 |
| 2 | | reads 0 | 0 |
| 3 | writes 1 | | 1 |
| 4 | | writes 1 | 1 |

Both threads incremented, but `count` ends at 1 instead of 2. Most runs may still give 2, so the bug appears only intermittently and is hard to reproduce.

**Common fixes:**
- **Locks (mutexes):** only one thread runs the critical section at a time.
- **Atomic operations:** the hardware does read-modify-write as one indivisible step, e.g. `AtomicInteger.incrementAndGet()` in Java or `std::atomic<int>` in C++.
- **Avoid shared mutable state:** give each thread its own data, or pass messages instead of sharing variables.

Races also occur outside threads. A classic case is check-then-act on files ("TOCTOU", time-of-check to time-of-use): a program checks that a file exists, then opens it, and another process swaps the file in between.

Tools like ThreadSanitizer (`-fsanitize=thread` in Clang/GCC) or Go's `go test -race` can detect many data races automatically. If you have code you suspect has a race, share it and I can walk through the interleavings.
