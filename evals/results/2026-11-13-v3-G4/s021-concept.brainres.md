<!-- Q: What is a database index? -->

A database index is a separate data structure (usually a B-tree) that stores a column's values in sorted order alongside pointers to the matching rows, so the database can find rows without scanning the whole table.

**Why it matters:** Without an index, `SELECT * FROM users WHERE email = 'a@b.com'` reads every row (O(n)). With an index on `email`, it walks the tree to the match (O(log n)).

**Example:**

```sql
CREATE INDEX idx_users_email ON users (email);
```

**Tradeoffs:**

| Benefit | Cost |
|---|---|
| Much faster reads on filtered, sorted, or joined columns | Extra disk space |
| Can enforce uniqueness (`CREATE UNIQUE INDEX`) | Slower `INSERT`/`UPDATE`/`DELETE`, since the index must be updated too |

**Rule of thumb:** index columns you frequently use in `WHERE`, `JOIN`, and `ORDER BY`, and skip columns that are rarely queried or have very few distinct values (like a boolean).

Next step: if you have a slow query, run `EXPLAIN` on it to see whether it's doing a full table scan and which index would help.
