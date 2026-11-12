<!-- Q: Why does my counter sometimes end up lower than the number of requests? -->

- Each request reads the counter
- It adds 1
- It writes the value back
- The read and the write are separate steps
- Another request can run between them
- Two requests can read the same value at once
- Both write the same result
- One increment is lost
- Fix: atomic increment (UPDATE counter = counter + 1)
