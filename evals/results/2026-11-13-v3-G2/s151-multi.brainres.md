<!-- Q: Three questions: what's a race condition, how do I detect one, and how do I fix it in Python? -->

A race condition is a bug where the result depends on the timing of threads or processes that share data, so the same code gives different results from run to run. For example, `counter += 1` is really read, add, write. Two threads can both read 5 and both write 6, and one update is lost.

## How to detect one

1. Check an invariant after a stress run, such as "final count equals threads × iterations". Repeat the run many times, because one pass can succeed by luck.
2. Call `sys.setswitchinterval(1e-6)` at startup. Python then switches threads far more often, so bad interleavings show up sooner.
3. Review every piece of mutable state that more than one thread touches. In `asyncio`, a race can only happen across an `await`, so look there.
4. Log thread IDs and timestamps around the suspect code when the bug only appears in production.

A passing test never proves there is no race. It only means you didn't hit the bad timing.

## How to fix it in Python

```python
import sys, threading
sys.setswitchinterval(1e-6)

counter = 0
lock = threading.Lock()

def work():
    global counter
    for _ in range(100_000):
        with lock:          # remove this line and the assert below fails
            counter += 1

threads = [threading.Thread(target=work) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()
assert counter == 400_000
```

Pick the fix that matches where the shared state lives:

| Situation | Fix |
|---|---|
| Threads share a variable | `threading.Lock` (or `RLock`) around the read-modify-write |
| Threads pass work to each other | `queue.Queue`, which is already thread-safe |
| Separate processes | `multiprocessing.Lock`, or avoid sharing and use `Queue` or `Pool` results |
| `asyncio` tasks | `asyncio.Lock` around the section that contains an `await` |

A database needs the same care. Use one atomic statement (`UPDATE t SET n = n + 1`) or a transaction with row locking, not read-then-write in Python.

The best fix is usually to remove the shared state, so each worker computes its own result and one thread merges them.

If you paste the code you suspect, I can point to the exact racy lines and the smallest fix.
