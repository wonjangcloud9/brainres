<!-- Q: Three questions: what's a race condition, how do I detect one, and how do I fix it in Python? -->

A **race condition** happens when a program's correct behavior depends on the timing or interleaving of two or more threads, processes, or async tasks, and they touch shared state without coordination. The result can change from run to run depending on which one gets there first.

A classic example is a counter incremented from two threads:

```python
counter = 0

def work():
    global counter
    for _ in range(100_000):
        counter += 1  # read, add, write: not atomic

threads = [threading.Thread(target=work) for _ in range(2)]
```

`counter += 1` is three steps (read, add, write). If two threads interleave between read and write, one increment is lost. You might get 150,000 instead of 200,000, and the number changes between runs.

## How to detect one

- **Stress testing:** Run the code repeatedly under load, with many threads and iterations, and check whether results are inconsistent. Add `time.sleep(0)` or small sleeps inside critical sections to widen the window.
- **ThreadSanitizer-style tools:** Python doesn't have a built-in race detector. For C extensions, use TSan. For pure Python, `sys.setswitchinterval(1e-6)` forces frequent thread switches, which makes races show up more often.
- **Static review:** Look for shared mutable state (module globals, class attributes, shared dicts or lists) that is accessed from multiple threads or tasks without a lock.
- **Assertions on invariants:** Check that totals, balances, or counts match what they should after concurrent operations.
- **Tools like `hypothesis` or `pytest-repeat`:** Useful for running concurrent tests many times.

## How to fix one in Python

**1. Use a lock** to make the critical section atomic:

```python
import threading

counter = 0
lock = threading.Lock()

def work():
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1
```

**2. Use a thread-safe data structure.** For example, `queue.Queue` handles its own locking, so producers and consumers don't need an extra lock.

**3. Avoid sharing state.** Give each thread its own data and merge the results at the end. This is often the simplest and fastest fix:

```python
from concurrent.futures import ThreadPoolExecutor

def work(n):
    return sum(1 for _ in range(n))  # local state only

with ThreadPoolExecutor() as ex:
    total = sum(ex.map(work, [100_000, 100_000]))
```

**4. Use `multiprocessing` with its own primitives** (`Value`, `Lock`, `Queue`) if you need true parallelism for CPU-bound work, since the GIL limits threads for that.

**5. For asyncio code,** race conditions happen at `await` points. Use `asyncio.Lock` around shared state, and keep the critical section free of `await` when you can.

**6. Use atomic operations where available.** Some libraries provide them, and `itertools.count()` is effectively thread-safe for generating unique IDs in CPython, though relying on that is an implementation detail.

Keep critical sections small, always acquire locks in a consistent order if you use more than one, and prefer higher-level tools (queues, executors) over hand-rolled locking when they fit.
