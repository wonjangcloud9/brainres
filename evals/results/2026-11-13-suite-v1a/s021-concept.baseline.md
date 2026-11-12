<!-- Q: What is a database index? -->

A database index is a separate data structure that lets the database find rows quickly without scanning the entire table. It works like a book's index: instead of reading every page to find a topic, you look it up in a sorted list that points to the right pages.

**How it works**

- You create an index on one or more columns (e.g., `email` in a `users` table).
- The database stores those column values in a structure optimized for lookup, along with pointers to the corresponding rows.
- When a query filters or sorts on that column, the database uses the index to jump directly to matching rows instead of doing a full table scan.

**Common types**

- **B-tree** (the default in most databases): keeps values sorted, good for equality, range queries (`<`, `>`, `BETWEEN`), and `ORDER BY`.
- **Hash**: very fast for exact-match lookups, but no range support.
- **Composite**: covers multiple columns; column order matters (an index on `(a, b)` helps queries on `a` or `a AND b`, but generally not `b` alone).
- **Unique**: enforces that no two rows share the same value.
- **Specialized**: full-text, GIN/GiST (Postgres), spatial, bitmap, etc.

**Example**

```sql
CREATE INDEX idx_users_email ON users (email);

-- Now this can use the index instead of scanning every row:
SELECT * FROM users WHERE email = 'a@example.com';
```

**Tradeoffs**

- **Faster reads**: lookups go from O(n) to roughly O(log n) with a B-tree.
- **Slower writes**: every `INSERT`, `UPDATE`, and `DELETE` must also update the indexes.
- **Extra storage**: indexes take disk space and memory.
- **Not always used**: on small tables or low-selectivity columns (e.g., a boolean), the planner may ignore the index.

**Rule of thumb**: index columns that appear often in `WHERE`, `JOIN`, and `ORDER BY` clauses, and use your database's `EXPLAIN` command to confirm the index is actually being used.
