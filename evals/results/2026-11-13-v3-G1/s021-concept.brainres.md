<!-- Q: What is a database index? -->

A database index is a separate data structure that lets the database find rows without scanning the whole table. It works like a book's index: instead of reading every page to find a topic, you look it up in a sorted list that points to the page.

**How it works:** the index stores the values of one or more columns in sorted order (usually a B-tree), each paired with a pointer to the full row. A lookup on an indexed column walks the tree in O(log n) steps instead of checking all n rows.

**Example:**

```sql
CREATE INDEX idx_users_email ON users (email);

SELECT * FROM users WHERE email = 'a@example.com';
```

Without the index, the database reads every row in `users`. With it, the database jumps straight to the matching row.

**Trade-offs:**

| Benefit | Cost |
|---|---|
| Much faster reads on `WHERE`, `JOIN`, `ORDER BY` | Slower writes, because each insert, update, or delete must also update the index |
| Can enforce uniqueness (`UNIQUE` index) | Uses extra disk and memory |

**Rule of thumb:** index columns you filter, join, or sort on often, and skip small tables or columns with few distinct values (like a boolean).

To check whether a query uses an index, run `EXPLAIN` before it (for example, `EXPLAIN SELECT ...`) and look for an index scan instead of a full table scan.

If you tell me which database you use, I can show the exact syntax and `EXPLAIN` output to expect.
