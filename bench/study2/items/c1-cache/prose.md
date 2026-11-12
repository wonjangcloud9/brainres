<!-- Q: Why does my app sometimes show old data after an update? -->

Your app reads from a cache that keeps a copy of the data for 10 minutes. When you update the database, the cache still holds the old copy, so reads return stale data until the 10 minutes run out. Because the cache doesn't know the database changed, only expiry or an explicit invalidation replaces the copy. So the fix is to delete the cache entry whenever you write that record.
