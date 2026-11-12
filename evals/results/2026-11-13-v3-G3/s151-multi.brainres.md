<!-- Q: Three questions: what's a race condition, how do I detect one, and how do I fix it in Python? -->

**A race condition is a bug where the result depends on the timing of concurrent operations on shared state.** In Python, `counter += 1` is a read, an add, then a write, and another thread can run between those steps, so updates get lost.

```python
import threading

counter = 0

def work():
    global counter
    for _ in range(1_000_000):
        counter += 1

threads = [threading.Thread(target=work) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()
print(counter)  # expected 4_000_000, often less
```

The GIL does not prevent this. It only guarantees that one bytecode runs at a time, not that a multi-step operation is atomic. How often it fails varies by Python version and machine, so check on yours.

## Detecting one

Python has no built-in race detector, so you combine a few techniques:

- **Read for shared mutable state.** Look for globals, class attributes, and caches that several threads or tasks write to, and for check-then-act patterns such as `if not exists: create`.
- **Stress and repeat.** Run the test hundreds of times (`pytest --count=500` with `pytest-repeat`) with many threads.
- **Force more thread switches.** `sys.setswitchinterval(1e-6)` makes the interpreter switch threads far more often, which exposes races faster.
- **Insert a `time.sleep(0)` or small sleep** between the read and the write of a suspect operation. If the bug becomes reliable, you found it.
- **For C extensions or free-threaded builds,** use ThreadSanitizer. It does not see pure-Python logic races.

A passing test never proves there is no race. It only means the bad interleaving did not occur.

## Fixing it

Pick the fix that matches the concurrency model:

```python
lock = threading.Lock()

def work():
    global counter
    for _ in range(1_000_000):
        with lock:
            counter += 1
```

- **Threads:** protect the read-modify-write with `threading.Lock`. Keep the locked section as small as possible, and always acquire multiple locks in the same order to avoid deadlock.
- **Better than locking:** avoid sharing. Pass messages through `queue.Queue`, or have each thread compute a local result and combine them after `join()`.
- **asyncio:** races happen across `await` points, not between bytecodes. Code with no `await` in the critical section is safe. Otherwise use `asyncio.Lock`.
- **Processes:** `multiprocessing.Lock`, or `Value`/`Manager` for shared state. Plain globals are not shared between processes.
- **Files:** don't check then create. Use `open(path, "x")` (fails if it exists) and write to a temp file then `os.replace()` for atomic updates.
- **Databases:** use transactions, unique constraints, or `UPDATE t SET n = n + 1` instead of read-then-write in Python.

If you share the code you suspect, I can point to the exact interleaving.
