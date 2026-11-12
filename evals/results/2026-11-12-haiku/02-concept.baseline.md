<!-- Q: What is a race condition? -->

A **race condition** is a bug that happens when a program's correct behavior depends on the timing or ordering of events, and two or more threads, processes, or operations access shared resources in an unsynchronized way. The outcome changes depending on which one "wins the race."

**A simple example:**

Two threads both increment a shared counter `x` (initially 0):

```
Thread A: read x (0) → add 1 → write x (1)
Thread B: read x (0) → add 1 → write x (1)
```

If both read before either writes, the final value is 1 instead of 2. One update is lost.

**Common types:**

- **Data races:** Concurrent reads and writes to the same memory without synchronization.
- **Check-then-act (TOCTOU):** You check a condition, then act on it, but the condition changes in between. For example, checking whether a file exists and then opening it.
- **Read-modify-write:** Like the counter example above.
- **Order violations:** Operation B assumes A has already finished, but B sometimes runs first.

**Why they're hard:**

- They're nondeterministic. The bug may appear only occasionally, under load, or on certain hardware.
- Testing often doesn't reproduce them, and adding debug output can change the timing and hide them.

**Common fixes:**

- **Locks/mutexes:** Ensure only one thread accesses the shared data at a time.
- **Atomic operations:** Hardware-supported operations like compare-and-swap or atomic increment.
- **Message passing:** Avoid sharing state by having threads communicate through channels or queues.
- **Immutable data:** If data can't change, it can't be raced on.
- **Proper ordering primitives:** Semaphores, condition variables, or memory barriers when ordering matters.

Race conditions are related to, but distinct from, **deadlocks** (threads waiting on each other forever) and **livelocks** (threads actively running but making no progress).
