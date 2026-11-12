<!-- Q: Three questions: what's a race condition, how do I detect one, and how do I fix it in Python? -->

## What it is

A race condition is a bug where the result depends on the timing of threads, processes, or async tasks that share state, and at least one of them writes. The classic form is read-modify-write. `count += 1` looks like one step, but it is load, add, store. Two threads can both load 5 and both store 6, so one update is lost.

```python
import threading

count = 0
def work():
    global count
    for _ in range(1_000_000):
        count += 1

ts = [threading.Thread(target=work) for _ in range(4)]
for t in ts: t.start()
for t in ts: t.join()
print(count)  # expected 4_000_000; often less
```

## How to detect one

1. **Look for the symptom.** Results change between runs, or tests pass locally and fail in CI.
2. **Read for the three patterns.** Shared mutable state, read-modify-write (`x += 1`), and check-then-act (`if not exists: create`).
3. **Force the bad interleaving.** Call `sys.setswitchinterval(1e-6)` so threads switch far more often. Then run the code or test hundreds of times (for example with `pytest-repeat`). Differing totals confirm a race.
4. **Know the limit.** A passing stress run proves nothing. Whether the race shows up depends on your CPython version and loop size, so verify by running, not by assuming.

## How to fix it in Python

| Situation | Tool |
|---|---|
| Threads sharing a variable | `threading.Lock` |
| Threads passing work around | `queue.Queue` (thread-safe) |
| asyncio tasks | `asyncio.Lock` |
| Processes or database rows | DB transaction or constraint, `multiprocessing.Lock` |

The fix for the example above:

```python
lock = threading.Lock()

def work():
    global count
    for _ in range(1_000_000):
        with lock:
            count += 1
```

Better still, remove the sharing. Give each thread its own counter and sum the results after `join()`. No shared state means no race, and it is faster than locking a million times.

If you paste the code you suspect, I can point out the exact racy lines and pick the right fix.
