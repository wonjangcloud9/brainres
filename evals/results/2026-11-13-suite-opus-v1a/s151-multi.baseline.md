<!-- Q: Three questions: what's a race condition, how do I detect one, and how do I fix it in Python? -->

# Race Conditions in Python

## 1. What is a race condition?

A race condition happens when the correctness of a program depends on the **timing or interleaving** of operations that run concurrently, such as threads, processes, async tasks, or even separate programs touching the same file. The classic cause is **shared mutable state** accessed by more than one actor, where at least one of them writes, with no coordination between them.

The textbook example is a read-modify-write:

```python
import threading, time

counter = 0

def work():
    global counter
    for _ in range(10_000):
        tmp = counter        # 1. read
        time.sleep(0)        # (any work here lets another thread run)
        counter = tmp + 1    # 2. write, possibly overwriting another thread's update

threads = [threading.Thread(target=work) for _ in range(8)]
for t in threads: t.start()
for t in threads: t.join()

print(counter)  # expected 80000; you'll get much less
```

Two threads both read `5`, both write `6`, and one increment is lost.

**"Doesn't the GIL prevent this?"** No. The GIL makes individual bytecode instructions safe. It does not make *your* multi-step operations atomic. Even `counter += 1` is several bytecodes: load, add, store. On modern CPython a bare `+=` may *appear* to work most of the time, which makes it more dangerous. On free-threaded builds (3.13t/3.14t, no GIL), it breaks readily.

Common shapes of race conditions:
- **Read-modify-write**: `x += 1`, `balance = balance - amount`
- **Check-then-act**: `if key not in cache: cache[key] = compute()`
- **Lazy initialization**: `if _instance is None: _instance = Thing()`
- **TOCTOU (time-of-check to time-of-use)**: `if not os.path.exists(p): open(p, "w")`
- **Async races**: state checked before an `await` and used after it. Other tasks run during the `await`.

## 2. How do you detect one?

Races are nondeterministic. They show up as intermittent failures, "works on my machine," or bugs that vanish when you add print statements. Detection mixes inspection with making the bug more likely to happen.

**Inspect the code.** For each piece of shared mutable data (globals, class attributes, objects passed to threads, files, DB rows), ask:
- Can two actors touch it at the same time?
- Is at least one of them writing?
- Is there a gap between reading/checking and acting?

If all three answers are yes and nothing synchronizes the access, you likely have a race.

**Make the race more likely to happen:**
```python
import sys
sys.setswitchinterval(1e-6)   # force very frequent thread switches (default is 5ms)
```
- Insert `time.sleep(0)` or `time.sleep(random.random() / 1000)` at suspicious points to widen the window.
- Use many threads and many iterations, and check an invariant at the end, such as "the total equals N" or "no duplicate IDs."
- Run the test many times: `pip install pytest-repeat`, then `pytest --count=500 -x test_foo.py`.
- Test on a free-threaded Python build. It exposes races the GIL was masking.

**Gather evidence:**
- Log with thread/task identity and high-resolution timestamps (`%(threadName)s`, `time.perf_counter_ns()`) to reconstruct the interleaving.
- Add assertions on invariants inside the code, not only at the end.
- For C extensions or free-threaded builds, ThreadSanitizer (`-fsanitize=thread`) can detect data races at the native level.

## 3. How do you fix it?

Choose a strategy based on the situation, roughly in order of preference.

### a) Don't share state
This is often the cleanest fix. Have each worker return its result and combine the results afterward:
```python
from concurrent.futures import ThreadPoolExecutor

def work(n):
    return sum(1 for _ in range(n))

with ThreadPoolExecutor() as ex:
    total = sum(ex.map(work, [10_000] * 8))
```
Alternatively, pass messages through a `queue.Queue`, which is thread-safe, and keep state owned by a single thread.

### b) Use a lock around the critical section
```python
import threading

counter = 0
lock = threading.Lock()

def work():
    global counter
    for _ in range(10_000):
        with lock:              # read + write now happen as one unit
            counter += 1
```
The same pattern fixes check-then-act:
```python
with cache_lock:
    if key not in cache:
        cache[key] = compute(key)
```
Lock tips:
- Keep critical sections small.
- Always use `with` so the lock is released even if an exception occurs.
- Use `threading.RLock` if the same thread may need to re-acquire the lock.
- To avoid deadlocks, always acquire multiple locks in the **same order**.

### c) asyncio: lock across `await`s
```python
import asyncio
lock = asyncio.Lock()

async def withdraw(account, amount):
    async with lock:
        if account.balance >= amount:
            await asyncio.sleep(0)   # e.g. a DB call; other tasks run here
            account.balance -= amount
```
Code between two `await`s is effectively atomic in asyncio. Any check that spans an `await` needs protection.

### d) Processes: use multiprocessing primitives
```python
from multiprocessing import Value

counter = Value("i", 0)
with counter.get_lock():
    counter.value += 1
```

### e) Files and databases: make the operation itself atomic
Instead of checking and then acting, try the operation and handle failure (EAFP):
```python
# Instead of: if not os.path.exists(p): open(p, "w")
try:
    with open(p, "x") as f:   # "x" = fail if the file exists (O_CREAT | O_EXCL)
        ...
except FileExistsError:
    ...
```
- For atomic file replacement, write to a temp file, then call `os.replace(tmp, target)`.
- For databases, use transactions, unique constraints, `SELECT ... FOR UPDATE`, or atomic updates like `UPDATE t SET n = n + 1`, rather than reading in Python and writing back.

### f) Per-thread state
If each thread needs its own copy rather than a shared one, use `threading.local()`. For async code, use `contextvars.ContextVar`.

---

**Rule of thumb:** If data is shared and mutable, then sharing must be removed, mutation must be removed, or access must be serialized. Avoid relying on "this op is atomic under the GIL." That guarantee is fragile, undocumented in many cases, and goes away under free-threaded Python.
