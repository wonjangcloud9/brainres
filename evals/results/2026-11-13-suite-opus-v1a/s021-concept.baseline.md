<!-- Q: What is a database index? -->

A **database index** is a separate data structure the database maintains to find rows quickly without scanning the whole table. It works much like the index at the back of a book: instead of reading every page to find "B-tree," you look it up and jump straight to the right page.

## How it works

Without an index, a query like

```sql
SELECT * FROM users WHERE email = 'alice@example.com';
```

forces a **full table scan**, which checks every row. That is O(n).

With an index on `email`, the database keeps a sorted structure (usually a **B-tree** or B+ tree) that maps each email value to the location of its row. A lookup becomes O(log n). On a million rows, that is roughly 20 steps instead of a million.

```sql
CREATE INDEX idx_users_email ON users(email);
```

## Common types

| Type | Good for |
|---|---|
| **B-tree** (default in most DBs) | Equality, ranges (`<`, `>`, `BETWEEN`), sorting, prefix `LIKE 'abc%'` |
| **Hash** | Exact equality only |
| **Composite / multi-column** | Queries filtering on several columns, e.g. `(last_name, first_name)`. Column order matters. |
| **Unique** | Enforcing uniqueness. Primary keys get one automatically. |
| **Clustered** | Physically orders the table's rows by the key (e.g. InnoDB primary key, SQL Server clustered index) |
| **Covering** | Includes every column a query needs, so the table itself never has to be read |
| **Full-text / GIN / GiST** | Text search, arrays, JSON, geospatial data |

## Trade-offs

Indexes speed up reads, but they have costs:

- **Slower writes.** Every `INSERT`, `UPDATE` and `DELETE` must also update each affected index.
- **Storage.** Each index takes disk space and memory.
- **Not always used.** If a query matches a large fraction of the table, or wraps the column in a function (`WHERE LOWER(email) = ...`), the planner may skip the index.

## Rules of thumb

- Index columns that appear often in `WHERE`, `JOIN ... ON`, and `ORDER BY`.
- Favor **high-selectivity** columns, where values are mostly distinct. Indexing a boolean column rarely helps.
- For composite indexes, put the column you filter by equality first, then range columns.
- Use `EXPLAIN` (or `EXPLAIN ANALYZE`) to check whether your queries actually use the index.
- Don't index everything. Each extra index is a tax on writes.

If you share your schema or a slow query, I can suggest specific indexes for it.
