<!-- Q: What is a race condition? -->

A race condition is a bug where a program's result depends on the timing or order of concurrent operations, so the same code can give different results from run to run.

It happens when two or more threads or processes touch shared state, at least one writes, and nothing forces an order between them.

**Example:** two threads each run `counter += 1` on a shared counter that starts at 0.

1. Thread A reads `counter` (0).
2. Thread B reads `counter` (0).
3. Thread A writes 1.
4. Thread B writes 1.

The final value is 1, not 2, because `counter += 1` is really three steps (read, add, write), and the threads interleaved between them.

**Fixes:**

- **Lock** the critical section (mutex, `synchronized`, `threading.Lock`).
- **Atomic operations** for simple cases (`AtomicInteger`, `atomic.AddInt64`).
- **Avoid shared mutable state** by using immutable data, message passing, or per-thread copies.

Race conditions are hard to debug because they depend on timing and often vanish under a debugger. Tools like ThreadSanitizer (`-fsanitize=thread`) or Go's `go test -race` can find them.

If you have a specific piece of code you suspect, paste it and I'll point to the racy lines.
