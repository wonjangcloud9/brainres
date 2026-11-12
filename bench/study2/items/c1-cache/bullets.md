<!-- Q: Why does my app sometimes show old data after an update? -->

- Your app reads from a cache
- The cache keeps a copy for 10 minutes
- Updates go to the database
- The cache still holds the old copy
- Reads return stale data until expiry
- The cache doesn't know the database changed
- Fix: delete the cache entry when you write that record
