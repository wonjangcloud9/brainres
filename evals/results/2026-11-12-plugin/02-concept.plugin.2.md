<!-- Q: What is a race condition? -->

A race condition is a bug where a program's result depends on the timing of two or more concurrent operations, such as threads, processes, or requests, that access shared state without proper coordination.

**Example:** two threads each run `counter += 1` on a shared counter that starts at 0.

1. Thread A reads `0`.
2. Thread B reads `0`.
3. Thread A writes `1`.
4. Thread B writes `1`.

The counter ends at 1 instead of 2, because the read-modify-write isn't atomic and the steps interleaved. Run it again and the timing may differ, so the bug appears intermittently and is hard to reproduce.

**Common fixes:**
- Locks or mutexes, so only one thread touches the state at a time.
- Atomic operations, such as an atomic increment.
- Avoiding shared mutable state, through immutability or message passing.
- Database transactions or constraints, when the shared state lives in a database.

Race conditions also cause security bugs. A check-then-use gap (TOCTOU) lets an attacker change a file or balance between the check and the action.

If you have code you suspect has one, paste it and I'll look for the unsynchronized access.
