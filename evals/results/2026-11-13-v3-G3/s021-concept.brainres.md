<!-- Q: What is a database index? -->

A database index is a separate data structure, usually a B-tree, that lets the database find rows by a column's value without scanning the whole table.

**How it works:** the index stores the column's values in sorted order, each with a pointer to its row. A lookup like `WHERE email = 'a@b.com'` walks the tree in O(log n) steps instead of reading all n rows.

**Example:**

```sql
CREATE INDEX idx_users_email ON users (email);

-- now fast:
SELECT * FROM users WHERE email = 'a@b.com';
```

**Tradeoffs:**
- Writes get slower, because every INSERT, UPDATE and DELETE must also update the index.
- Indexes use extra disk and memory.
- An index only helps queries that filter, join, or sort on its columns. In a multi-column index, order matters: `(last_name, first_name)` helps `WHERE last_name = ...` but not `WHERE first_name = ...` alone.

To check whether a query uses an index, run `EXPLAIN` before it (PostgreSQL and MySQL both support this). Look for an index scan rather than a sequential or full table scan.
