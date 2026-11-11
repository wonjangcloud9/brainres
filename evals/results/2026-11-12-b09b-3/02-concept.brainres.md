<!-- Q: What is a race condition? -->

A race condition is a bug where a program's result depends on the timing or order of operations that run concurrently, such as threads, processes, or requests, and that order isn't controlled.

**Example:** two threads each add 1 to a shared counter that starts at 0.

```python
counter = 0

def increment():
    global counter
    for _ in range(100_000):
        counter += 1   # read, add, write: three steps, not one
```

`counter += 1` reads the value, adds 1, then writes it back. If both threads read 0 before either writes, both write 1, and one increment is lost. Two threads running 100,000 increments each can end with a total below 200,000, and the number changes from run to run.

**Why it's hard to catch:** the bug only appears for certain interleavings, so tests often pass and production fails occasionally.

**Common fixes:**
- **Locks or mutexes:** only one thread enters the critical section at a time.
- **Atomic operations:** the read-modify-write happens as one indivisible step.
- **Immutable data or message passing:** threads don't share mutable state.
- **Database transactions or unique constraints:** for races between requests, such as two users claiming the last item.

Race conditions also show up in security, as time-of-check to time-of-use (TOCTOU) bugs, where a file or permission changes between the check and the use.

If you have code you suspect has one, point me to the file and I'll look for it.
