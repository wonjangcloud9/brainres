<!-- Q: What is a race condition? -->

A **race condition** is a bug where a program's behavior depends on the timing or ordering of events that aren't controlled, typically when multiple threads, processes, or requests access shared state concurrently and at least one modifies it.

## Classic example

Two threads increment a shared counter:

```python
counter = 0

def increment():
    global counter
    counter += 1   # read, add, write: three steps, not atomic
```

If both threads read `counter` as 5 before either writes back, both write 6. One increment is lost, and the result is 6 instead of 7.

## Common forms

- **Read-modify-write**: as above; updates get lost.
- **Check-then-act (TOCTOU)**: you check a condition, then act on it, but the condition changes in between. Example: checking a file exists or has certain permissions, then opening it. Another process can swap it in the gap. This is also a common security vulnerability.
- **Ordering assumptions**: code assumes event A finishes before event B (e.g., initialization before use), but nothing enforces it.
- **Data race**: a specific low-level case where unsynchronized memory accesses conflict. In languages like C++ or Go this is often undefined or unpredictable behavior.

## Why they're hard

They're **nondeterministic**: the bug may appear once in thousands of runs, disappear under a debugger, or only show on certain hardware or under load.

## How to prevent them

- **Locks/mutexes** around critical sections
- **Atomic operations** (e.g., atomic increment, compare-and-swap)
- **Immutable data** or avoiding shared mutable state
- **Message passing** or single-owner designs (channels, actors)
- **Database transactions** and proper isolation levels, or unique constraints, for check-then-insert patterns
- **Idempotency keys** for duplicated requests in distributed systems

## How to detect them

- Tools like ThreadSanitizer (`-fsanitize=thread`), Go's `-race` flag, or Java's concurrency analyzers
- Stress testing with many threads and randomized scheduling
- Code review focused on any shared mutable state

If you have a specific piece of code you suspect has one, I can take a look.
