<!-- Q: Three questions: what's a race condition, how do I detect one, and how do I fix it in Python? -->

# Race conditions

## 1. What it is

A race condition happens when the correctness of a program depends on the timing or interleaving of multiple threads/processes/tasks accessing shared state. If two operations that should be atomic get interleaved, you get wrong results that vary from run to run.

Classic example: `counter += 1` is really three steps (read, add, write). Two threads can both read `5`, both write `6`, and one increment is lost.

Common variants:
- **Read-modify-write** (lost updates, as above)
- **Check-then-act / TOCTOU** (`if not os.path.exists(f): create(f)`: another process creates it in between)
- **Lazy init** (two threads both see `_instance is None` and both create one)

## 2. How to detect one

- **Symptoms:** nondeterministic results, failures that appear only under load, "works on my machine," bugs that vanish when you add print statements or a debugger (which change timing).
- **Stress test it:** run the suspect code with many threads and many iterations, and assert on the invariant.
  ```python
  import threading
  n = 0
  def work():
      global n
      for _ in range(1_000_000):
          n += 1
  ts = [threading.Thread(target=work) for _ in range(4)]
  [t.start() for t in ts]; [t.join() for t in ts]
  print(n)  # expected 4_000_000; often less
  ```
  The GIL makes this less reproducible than in other languages, and recent CPython versions have narrowed the window further. Lowering the switch interval with `sys.setswitchinterval(1e-6)` makes races much easier to trigger.
- **Code review:** look for shared mutable state (globals, class attributes, caches, files, DB rows) touched without a lock, and for check-then-act sequences.
- **Tools:** run under `pytest` with repeated runs (`pytest-repeat`, `pytest-xdist`), use `faulthandler` to debug hangs, and try free-threaded Python (3.13+), which exposes races the GIL used to hide. For native extensions, ThreadSanitizer (TSan) works. For databases, inspect isolation levels and look for duplicate or lost rows.
- **Logging:** log thread IDs and timestamps around the critical section to see the interleaving.

## 3. How to fix it in Python

**Pick the approach by removing sharing first, then synchronizing.**

1. **Avoid shared mutable state.** Use message passing: `queue.Queue` (threads), `multiprocessing.Queue` (processes), or have each worker return a result and combine at the end.

2. **Use a lock around the critical section:**
   ```python
   lock = threading.Lock()
   def work():
       global n
       for _ in range(1_000_000):
           with lock:
               n += 1
   ```
   Keep the locked section small, always use `with` so it releases on exceptions, and acquire multiple locks in a consistent order to avoid deadlock.

3. **Make check-then-act atomic**, either by holding the lock across both the check and the act, or by using an atomic primitive:
   ```python
   # files: let the OS decide atomically
   try:
       with open(path, "x") as f: ...   # fails if it exists
   except FileExistsError: ...
   ```
   ```python
   # dicts: setdefault is atomic for simple keys
   cache.setdefault(key, value)
   ```

4. **Use the right primitive:** `RLock` (re-entrant), `Semaphore` (limit concurrency), `Event`/`Condition` (signaling), `threading.local()` (per-thread data), `asyncio.Lock` (for coroutines; `threading.Lock` is wrong there).

5. **For processes:** `multiprocessing.Lock`, or file locks (`fcntl.flock`, the `filelock` package).

6. **For databases:** use transactions, `SELECT ... FOR UPDATE`, atomic updates (`UPDATE t SET n = n + 1`), or unique constraints and optimistic locking with a version column.

7. **Lazy init:** use `functools.lru_cache`/module-level init, or double-checked locking with a lock.

**Rule of thumb:** don't rely on the GIL for correctness. It protects the interpreter's internals, not your multi-step logic, and it isn't guaranteed in free-threaded builds.
