<!-- Q: What is a race condition? -->

A **race condition** is a bug where a program's outcome depends on the *timing* or *ordering* of events, usually two or more threads or processes touching shared state at the same time, and at least one of them is writing.

## Classic example

Two threads each run `counter = counter + 1` on a shared `counter = 0`:

```
Thread A                 Thread B
--------                 --------
read counter  (0)
                         read counter  (0)
add 1         (1)
                         add 1         (1)
write counter (1)
                         write counter (1)
```

You expect `2` but get `1`. The increment looks like one step, but it is really **read → modify → write**, and the threads interleaved in the middle.

## Common forms

- **Read-modify-write**: lost updates, like the counter above.
- **Check-then-act (TOCTOU, "time of check to time of use")**: you check a condition and then act on it, but the condition changes in between.
  ```python
  if not os.path.exists(path):   # check
      open(path, "w")            # act: another process may have created it
  ```
  This is also a well-known security vulnerability class, for example in symlink attacks on temp files.
- **Ordering assumptions**: code assumes event X happens before Y (e.g., "the config is loaded before the handler runs"), but nothing enforces it.

## Why they're nasty

- **Nondeterministic**: they may appear once in 10,000 runs, or only under load.
- **Heisenbugs**: adding logging or a debugger changes the timing and can hide the bug.
- They often pass every test and then fail in production.

## How to prevent them

- **Mutual exclusion**: locks, mutexes, `synchronized`, so only one thread is in the critical section at a time.
- **Atomic operations**: `AtomicInteger`, `std::atomic`, compare-and-swap, or database operations like `UPDATE ... SET n = n + 1`.
- **Avoid shared mutable state**: immutable data, message passing (channels, actors), or per-thread copies.
- **Atomic system calls** instead of check-then-act, e.g., `open(path, O_CREAT | O_EXCL)` instead of `exists()` followed by `open()`.
- **Transactions and proper isolation levels** in databases.
- **Tooling**: ThreadSanitizer (`-fsanitize=thread`), Go's `-race` flag, Helgrind.

**Related term:** a *data race* is the narrower, language-level case of two threads accessing the same memory at once, with at least one write and no synchronization. You can have a race condition without a data race (e.g., TOCTOU across processes) and, in principle, a data race that is harmless, though in C/C++ data races are undefined behavior.
