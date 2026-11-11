<!-- Q: What is a race condition? -->

A **race condition** is a bug where a program's behavior depends on the timing or ordering of events that aren't controlled, typically when multiple threads, processes, or requests access shared state at the same time and at least one modifies it.

**Classic example:** two threads increment a shared counter.

```
counter = 0

Thread A: read counter (0)
Thread B: read counter (0)
Thread A: write counter = 1
Thread B: write counter = 1   # expected 2, got 1
```

`counter += 1` looks atomic but is really read, modify, write. If the steps interleave, one update is lost.

**Common forms:**
- **Read-modify-write:** lost updates, as above.
- **Check-then-act (TOCTOU):** you check a condition (file exists, balance sufficient) and act on it, but the state changes in between.
- **Data race:** unsynchronized concurrent access to memory where at least one access is a write. In languages like C/C++ this is undefined behavior.
- **Ordering issues:** code assumes event X happens before Y, but nothing enforces it.

**Why they're nasty:** they're nondeterministic. They may appear only under load, on certain hardware, or once in a million runs, and adding logging or a debugger can make them vanish.

**Typical fixes:**
- **Mutual exclusion:** locks/mutexes around critical sections.
- **Atomic operations:** atomic increments, compare-and-swap.
- **Immutability / avoiding shared state:** message passing, thread-local data.
- **Database-level protection:** transactions, row locks, unique constraints, optimistic concurrency (version columns).
- **Idempotency:** so retries or duplicate requests don't cause double effects.

**Detection tools:** ThreadSanitizer (C/C++/Go/Rust), `go test -race`, Helgrind, Java's `jcstress`, and stress testing with many iterations.

**Security angle:** race conditions can be exploitable, for example double-spending a coupon by sending parallel requests, or swapping a file between a permission check and its use (TOCTOU).

If you have a specific language or code snippet in mind, I can show a concrete example and fix.
