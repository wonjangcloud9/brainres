<!-- Q: What is a database index? -->

A **database index** is a data structure that speeds up lookups on a table by letting the database find rows without scanning every row.

**How it works:** An index stores a sorted copy of one or more columns, along with pointers to the matching rows. When you query on an indexed column, the database searches this smaller, sorted structure (often a B-tree) and jumps straight to the matching rows, rather than reading the whole table (a "full table scan").

**Example:** Given a `users` table with millions of rows, this query:

```sql
SELECT * FROM users WHERE email = 'alice@example.com';
```

is much faster with an index on `email`:

```sql
CREATE INDEX idx_users_email ON users(email);
```

**Tradeoffs:**
- **Faster reads:** Lookups, joins, `ORDER BY`, and range filters on indexed columns get much faster.
- **Slower writes:** `INSERT`, `UPDATE`, and `DELETE` must also update each index, adding overhead.
- **Storage cost:** Indexes take up disk space and memory.

**Common types:**
- **B-tree:** The default in most databases; good for equality and range queries.
- **Hash:** Fast for exact-match lookups only.
- **Unique index:** Enforces that no two rows share the same value.
- **Composite index:** Covers multiple columns, e.g., `(last_name, first_name)`. Column order matters.
- **Full-text, GIN, GiST, etc.:** Specialized indexes for text search, arrays, or geospatial data.

**Rule of thumb:** Index columns you frequently filter, join, or sort on, and avoid indexing columns that are rarely queried or that change constantly. You can check whether the database is using an index with `EXPLAIN` (PostgreSQL, MySQL) or `EXPLAIN QUERY PLAN` (SQLite).
