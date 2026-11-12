<!-- Q: What is a race condition? -->

A race condition is a bug where a program's result depends on the timing of two or more operations that touch shared data. When the timing changes, the result changes too.

**Example: two threads incrementing a counter**

`counter += 1` looks like one step, but the CPU does three:

1. Read `counter` from memory.
2. Add 1.
3. Write the result back.

Suppose `counter = 5` and two threads run it at once:

| Time | Thread A | Thread B | `counter` in memory |
|------|----------|----------|---------------------|
| 1 | reads 5 | | 5 |
| 2 | | reads 5 | 5 |
| 3 | writes 6 | | 6 |
| 4 | | writes 6 | 6 |

Two increments ran, but the counter only went up by 1. If Thread A had finished before Thread B started, you'd get 7. The outcome depends on who "wins the race."

**Why it's hard to catch**

Race conditions are intermittent because thread scheduling varies on each run. A test can pass 999 times and fail once. They often show up only under load or on different hardware.

**Common fixes**

- **Locks (mutexes):** only one thread can enter the critical section at a time.
- **Atomic operations:** the hardware performs read-modify-write as one indivisible step.
- **Avoid shared mutable state:** use message passing, immutable data, or per-thread copies.

**Beyond threads**

The same pattern appears elsewhere. A "check-then-act" file bug is one case: you check that a file doesn't exist, then create it, but another process creates it in between. This specific security variant is called TOCTOU (time-of-check to time-of-use). Two web requests updating the same database row can also race.

If you have code you suspect has a race, share it and I can point out the shared state and suggest a fix.
