<!-- Q: What is a database index? -->

A database index is a separate data structure, usually a B-tree, that lets the database find rows by a column's value without scanning the whole table.

It works like a book's index: the database keeps the column values in sorted order, each pointing to its row's location. A lookup like `WHERE email = 'a@b.com'` then takes about O(log n) steps instead of O(n).

**Cost.** Indexes speed up reads but slow down writes, because every `INSERT`, `UPDATE`, and `DELETE` must also update each index on the table. They also use extra disk and memory.

**Common types:**

| Type | Good for |
|---|---|
| B-tree (default) | equality, ranges, sorting |
| Hash | equality only |
| Composite (multi-column) | queries filtering on several columns together |
| Unique | enforcing no duplicates, plus fast lookup |

**Example (SQL):**

```sql
CREATE INDEX idx_users_email ON users (email);
```

**When to add one:** on columns used often in `WHERE`, `JOIN`, or `ORDER BY`, especially on large tables. Skip them on tiny tables or columns with few distinct values, since the planner may ignore them anyway.

To check whether a query uses an index, run `EXPLAIN` on it (in PostgreSQL, `EXPLAIN ANALYZE`) and look for an index scan rather than a sequential scan.

If you tell me which database you use, I can show how to inspect or design indexes for it.
