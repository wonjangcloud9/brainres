<!-- Q: Three questions: what's a race condition, how do I detect one, and how do I fix it in Python? -->

A race condition is a bug where the result depends on the timing of concurrent threads or tasks touching shared state, so the same code gives different results from run to run.

**Example**

```python
import threading

counter = 0

def work():
    global counter
    for _ in range(100_000):
        counter += 1   # load, add, store: not atomic

threads = [threading.Thread(target=work) for _ in range(8)]
for t in threads: t.start()
for t in threads: t.join()
print(counter)  # expected 800000, may print less
```

Two threads can both read 5, both write 6, and one increment is lost. The GIL does not prevent this, because a thread switch can happen between bytecodes.

**Detecting it**

1. Make switches frequent: `sys.setswitchinterval(1e-6)`, then run the code in a loop with many threads. Races are intermittent, so one passing run proves nothing.
2. Review for shared mutable state, especially check-then-act (`if key not in d: d[key] = ...`) and read-modify-write (`+=`).
3. In asyncio, look for state read before an `await` and used after it. Another task can change it in between.
4. For C extensions or free-threaded Python builds, use ThreadSanitizer.

**Fixing it**

1. Lock the critical section (the code that must run by one thread at a time):
   ```python
   lock = threading.Lock()

   def work():
       global counter
       for _ in range(100_000):
           with lock:
               counter += 1
   ```
2. Better, avoid sharing. Pass data between threads with `queue.Queue`, or have each worker compute a local result and combine them after `join()`.
3. In asyncio, use `asyncio.Lock`, or keep the read and write with no `await` between them.
4. Across processes, files or databases, use atomic operations: DB transactions, `os.replace` for file swaps, `open(path, "x")` for create-if-missing.

Next step: if you have a specific piece of code you suspect, paste it or point me to the file and I'll look for the unsafe read-modify-write.
