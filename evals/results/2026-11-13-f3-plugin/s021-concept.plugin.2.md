<!-- Q: What is a database index? -->

A database index is a separate data structure, usually a B-tree, that maps column values to row locations. This lets the database find rows without scanning the whole table.

Databases use indexes on columns that queries filter, join, or sort by, such as IDs, emails, and timestamps. The cost is extra disk space and slower writes, because each insert or update must also update the index.

Example:

```sql
CREATE INDEX idx_users_email ON users(email);
SELECT * FROM users WHERE email = 'a@example.com';
```

Without the index, the database reads every row in `users`. With it, the database looks up the email in the sorted tree and jumps straight to the matching row. On a table with millions of rows, that is the difference between a full scan and a few page reads.

To check whether a query uses an index, run `EXPLAIN` before it.
