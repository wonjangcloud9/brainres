<!-- Q: What is a race condition? -->

A **race condition** is a bug where a program's behavior depends on the timing or ordering of events that aren't properly controlled, typically when multiple threads, processes, or requests access shared state concurrently and at least one modifies it.

**Classic example:** two threads increment a shared counter.

```
counter = 0

Thread A: read counter (0)
Thread B: read counter (0)
Thread A: write counter = 1
Thread B: write counter = 1   # expected 2
```

The increment looks like one step but is really read, modify, write. If the steps interleave, one update is lost.

**Common forms:**
- **Read-modify-write:** as above, lost updates.
- **Check-then-act (TOCTOU):** you check a condition (file exists, balance sufficient) and act on it, but the state changes in between. This is also a frequent source of security vulnerabilities.
- **Data race:** unsynchronized concurrent access to memory where one access is a write. In languages like C, C++, and Rust (unsafe), this is undefined behavior.

**Why they're hard:** they're nondeterministic. The code may work thousands of times and then fail under load or on different hardware, and adding logging or a debugger can change the timing enough to hide the bug.

**How to prevent them:**
- **Locks/mutexes** around critical sections.
- **Atomic operations** (e.g., atomic increment, compare-and-swap).
- **Immutability / avoiding shared state**, or message passing between threads.
- **Database transactions** and appropriate isolation levels, or unique constraints and optimistic locking for distributed cases.
- **Idempotent operations** so retries and duplicates are harmless.

**How to find them:** tools like ThreadSanitizer (`-fsanitize=thread`), Go's `go test -race`, and Java's concurrency testing tools, plus stress tests and careful code review of shared state.

Note that race conditions aren't limited to threads: they also occur between processes, across web requests (e.g., two simultaneous "redeem coupon" calls), and in distributed systems.
