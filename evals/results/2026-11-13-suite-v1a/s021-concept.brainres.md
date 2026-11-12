<!-- Q: What is a database index? -->

A database index is a separate data structure, usually a B-tree, that maps column values to row locations so the database can find rows without scanning the whole table.

Think of the index at the back of a book. To find "caching", you look it up in the sorted index and jump to the page, instead of reading every page.

**Example**

```sql
-- Without an index, this scans every row in users
SELECT * FROM users WHERE email = 'a@example.com';

-- Build the index once
CREATE INDEX idx_users_email ON users (email);
```

After that, the same query walks the sorted tree in about log(n) steps. On a table with millions of rows, that is the gap between milliseconds and seconds.

**Trade-offs**

| Benefit | Cost |
|---|---|
| Much faster reads on indexed columns (`WHERE`, `JOIN`, `ORDER BY`) | Slower `INSERT`, `UPDATE`, `DELETE`, because each index must be updated too |
| Can enforce uniqueness (`UNIQUE INDEX`) | Takes disk space and memory |

**Practical rules**

1. Index columns you filter, join, or sort on often.
2. Skip columns with few distinct values (like a boolean) and very small tables, where a scan is already cheap.
3. For multi-column indexes, column order matters: an index on `(a, b)` helps queries on `a` or on `a` and `b`, but not on `b` alone.

To check whether an index is used, run `EXPLAIN` before your query (for example `EXPLAIN SELECT ...`). Look for an index scan instead of a sequential (full table) scan.

If you tell me which database you use (PostgreSQL, MySQL, SQLite), I can show the exact `EXPLAIN` output to expect.
