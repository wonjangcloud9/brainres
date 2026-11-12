<!-- Q: Why does my counter sometimes end up lower than the number of requests? -->

Each request reads the counter, adds 1, and writes it back. When two requests read the same value at the same moment, both add 1 to it and both write the same result, so one increment is lost. Because the read and the write are separate steps, another request can slip in between them. So the fix is to make the increment one atomic operation, for example a database UPDATE counter = counter + 1.
