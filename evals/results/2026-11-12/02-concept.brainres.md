<!-- Q: What is a race condition? -->

A race condition is a bug where a program's result depends on the timing or order of concurrent operations, so the same code can give different results from run to run.

It happens when two or more threads, processes, or requests access shared state and at least one modifies it, with no synchronization to enforce an order.

**Worked example:** two threads each run `counter += 1` on a shared counter that starts at 0.

```python
# Each thread does: read counter, add 1, write back
counter = 0

def increment():
    global counter
    counter += 1   # not atomic: read -> add -> write
```

If both threads read `0` before either writes, both write `1`. The final value is 1, not 2. One update is lost.

**Common fixes:**

1. **Locks/mutexes:** only one thread enters the critical section at a time.
2. **Atomic operations:** use primitives like `AtomicInteger` or `atomic_fetch_add` that do read-modify-write as one step.
3. **Avoid shared mutable state:** use immutable data, message passing, or per-thread copies.
4. **Database-level guards:** transactions, row locks, or unique constraints (for example, to stop two requests both claiming the last item in stock).

A related security form is TOCTOU (time-of-check to time-of-use), where a file or permission is checked and then changed before it's used.

Race conditions are hard to debug because they're nondeterministic. Tools like ThreadSanitizer (`-fsanitize=thread` in clang/gcc) or Go's `go test -race` detect many of them.

Next step: if you suspect one in your code, tell me the language and the shared variable, and I can look for the unsynchronized access.
