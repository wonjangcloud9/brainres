<!-- Q: Three questions: what's a race condition, how do I detect one, and how do I fix it in Python? -->

A race condition is a bug where the result depends on the timing of threads or processes touching shared state, such as two threads running `counter += 1` and losing an update because both read the same old value.

**Example (broken)**

```python
import threading

counter = 0

def work():
    global counter
    for _ in range(1_000_000):
        counter += 1   # read, add, write: three steps, not atomic

threads = [threading.Thread(target=work) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()
print(counter)  # expected 4,000,000; often less
```

The GIL does not prevent this because a thread switch can happen between the read and the write. The loss is more reliable on free-threaded builds and varies by Python version.

**Detecting one**

1. Look for read-modify-write on shared data (`+=`, check-then-act like `if key not in d: d[key] = ...`) without a lock.
2. Stress it: run many threads and call `sys.setswitchinterval(1e-6)` to force frequent switches, then repeat the test hundreds of times (for example with `pytest-repeat`).
3. In `asyncio`, races happen only across `await` points, so check any shared state read before an `await` and used after it.
4. For C extensions, use ThreadSanitizer. It does not instrument pure Python code.

**Fixing it**

| Situation | Fix |
|---|---|
| Shared variable, threads | `threading.Lock` |
| Passing work between threads | `queue.Queue` (already thread-safe) |
| Coroutines | `asyncio.Lock` |
| Multiple processes | `multiprocessing.Lock`, or let a database do atomic updates |

```python
lock = threading.Lock()

def work():
    global counter
    for _ in range(1_000_000):
        with lock:
            counter += 1
```

The best fix is usually to avoid shared mutable state: have each thread compute a local result and combine the results after `join()`. This avoids lock contention and is easier to reason about.

Next step: if you have code you suspect, paste it or give me the file path and I'll point to the exact unsafe lines.
