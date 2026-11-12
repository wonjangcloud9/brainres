<!-- Q: What is a race condition? -->

A race condition is a bug where a program's result depends on the timing or order of concurrent operations, so the same code can give different results from run to run.

It happens when two or more threads or processes read and write shared state without coordination. Each step looks correct alone, but the steps can interleave in a harmful way.

**Example: two threads incrementing a counter**

```python
import threading

count = 0

def work():
    global count
    for _ in range(100_000):
        count += 1   # read, add, write: three steps, not one

threads = [threading.Thread(target=work) for _ in range(2)]
for t in threads: t.start()
for t in threads: t.join()
print(count)  # expected 200000, often less
```

`count += 1` is a read, an add, and a write. If both threads read `5` before either writes, both write `6`, and one increment is lost.

**Fixes**, depending on the case:

1. Lock the critical section (`threading.Lock`, `mutex`).
2. Use atomic operations (`AtomicInteger`, `std::atomic`).
3. Avoid shared mutable state (message passing, immutable data).
4. In databases, use transactions or row locks, or a conditional update such as `UPDATE ... WHERE version = ?`.

Races are hard to debug because they are intermittent. Tools like ThreadSanitizer (`-fsanitize=thread`) or Go's `-race` flag can detect them.

If you have a specific piece of code you suspect, paste it and I'll point out where the race is.
