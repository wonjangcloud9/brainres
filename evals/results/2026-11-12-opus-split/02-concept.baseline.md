<!-- Q: What is a race condition? -->

A **race condition** is a bug where a program's behavior depends on the *timing* or *ordering* of events, such as which of two threads runs first, and that ordering isn't controlled. The program might work 999 times and fail on the 1000th, because the outcome depends on who "wins the race."

## Classic example: a lost update

Two threads each try to increment a shared counter:

```python
counter = 0

def increment():
    global counter
    temp = counter      # 1. read
    temp = temp + 1     # 2. modify
    counter = temp      # 3. write
```

If both threads run `increment()` at the same time, this interleaving can happen:

| Step | Thread A        | Thread B        | `counter` |
|------|-----------------|-----------------|-----------|
| 1    | reads 0         |                 | 0         |
| 2    |                 | reads 0         | 0         |
| 3    | writes 1        |                 | 1         |
| 4    |                 | writes 1        | 1         |

Two increments ran, but `counter` is **1**, not 2. One update was lost.

## Why it happens

The read-modify-write sequence isn't **atomic**, so another thread can step in between the steps. The code that touches shared state is called the **critical section**.

## Common forms

- **Lost updates**: as above.
- **Check-then-act (TOCTOU, "time of check to time of use")**: `if file doesn't exist: create file`. Another process can create the file between the check and the create. This is also a frequent source of security vulnerabilities.
- **Lazy initialization**: two threads both see `instance is None` and both create one.
- **Ordering bugs**: code assumes event X finishes before Y, but nothing guarantees it, such as using data before an async load completes.

## How to prevent them

- **Locks / mutexes**: only one thread enters the critical section at a time.
  ```python
  with lock:
      counter += 1
  ```
- **Atomic operations**: hardware or library primitives that do read-modify-write in one indivisible step, such as `AtomicInteger` or compare-and-swap.
- **Avoid shared mutable state**: use immutable data, message passing (queues, channels, actors), or thread-local data.
- **Database transactions and constraints**: use `SELECT ... FOR UPDATE`, unique constraints, or optimistic locking with version columns.
- **Atomic OS/filesystem operations**: for example, `open(path, O_CREAT | O_EXCL)` instead of checking whether the file exists first.

## Why they're nasty

They're often **non-deterministic and hard to reproduce**. Adding logging or a debugger changes the timing and can make the bug disappear (a "heisenbug"). Tools like ThreadSanitizer, Go's `-race` flag, and stress testing help catch them.

A related term: a **data race** specifically means two threads access the same memory at once, with at least one writing and no synchronization. All data races cause race conditions, but you can have a race condition without a data race, such as the TOCTOU file example.
