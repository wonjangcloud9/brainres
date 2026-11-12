<!-- Q: What is a race condition? -->

A race condition is a bug where a program's result depends on the timing or order in which concurrent operations run. When two threads, processes, or async tasks touch shared data and at least one writes to it, the outcome can change from run to run.

Here is a simple example. Two threads each increment a shared counter `count` from 0 by reading it, adding 1, and writing it back:

1. Thread A reads `count` (0).
2. Thread B reads `count` (0).
3. Thread A writes 1.
4. Thread B writes 1.

Both increments ran, but `count` is 1 instead of 2. The bug appears only when the operations interleave in that order, so it can pass tests and fail under load.

Common fixes:

- **Locks or mutexes** around the shared access.
- **Atomic operations**, such as `atomic.AddInt64` in Go or `AtomicInteger` in Java.
- **Avoiding shared mutable state**, for example by passing messages between workers.

If you have a specific piece of code you suspect, paste it here and I can point to the exact interleaving that breaks it.
