<!-- Q: Three questions: what's a race condition, how do I detect one, and how do I fix it in Python? -->

A race condition is a bug where the result depends on the timing or interleaving of two or more threads, processes, or async tasks touching shared state. Two threads doing `count += 1` can both read the same value and write back the same result, so one increment is lost.

**How to detect one**

1. **Read for shared mutable state.** Look for globals, class attributes, or objects touched by more than one thread, task, or process, especially read-then-write sequences (`if x not in d: d[x] = ...`).
2. **Stress-test it.** Run the code many times in parallel and check invariants, for example that the final count equals the number of increments:
   ```python
   import threading
   count = 0
   def work():
       global count
       for _ in range(100_000):
           count += 1
   threads = [threading.Thread(target=work) for _ in range(8)]
   for t in threads: t.start()
   for t in threads: t.join()
   print(count)  # expect 800000; often prints less
   ```
3. **Use tools.** ThreadSanitizer (`-fsanitize=thread` for C extensions) and `python -X dev` surface some issues. Pure-Python races are usually found by stress tests, not static tools.

**How to fix it in Python**

Protect the read-modify-write with a lock:

```python
import threading

count = 0
lock = threading.Lock()

def work():
    global count
    for _ in range(100_000):
        with lock:
            count += 1
```

For simple counters, `queue.Queue` or `concurrent.futures` can remove shared state entirely. For async code, use `asyncio.Lock` instead of `threading.Lock`. Keep the critical section short, and never hold a lock while doing I/O.

Next step: if you share the code where the race happens, I can point to the exact shared variable and write the fix for it.
