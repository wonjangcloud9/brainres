<!-- Q: What is a race condition? -->

A race condition is a bug where a program's result depends on the timing or order of operations that run concurrently, such as threads, processes, or requests, and that order isn't controlled.

**Example:** two threads each run `counter += 1` on a shared counter that starts at 0.

1. Thread A reads `0`.
2. Thread B reads `0`.
3. A writes `1`.
4. B writes `1`.

The counter ends at 1 instead of 2, because the read-modify-write isn't atomic. It may also come out right on other runs, which makes these bugs hard to reproduce.

**Common fixes:**
- Locks or mutexes around the shared access.
- Atomic operations.
- Immutable data or message passing, so nothing is shared.
- Database transactions or unique constraints, for races between requests.

If you have a specific piece of code you suspect, paste it and I'll point to the racy section.
