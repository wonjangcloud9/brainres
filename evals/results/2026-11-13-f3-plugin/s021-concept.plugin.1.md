<!-- Q: What is a database index? -->

A database index is a separate data structure, usually a B-tree, that lets the database find rows by a column's value without scanning the whole table. It works like a book's index: you look up the term and jump to the page.

Indexes speed up `WHERE`, `JOIN`, and `ORDER BY` on large tables. The cost is slower writes, because every insert or update must also update the index, and extra disk space.

Example:

```sql
CREATE INDEX idx_users_email ON users (email);
SELECT * FROM users WHERE email = 'a@example.com';
```

Without the index, the database reads every row in `users`. With it, the lookup takes a few steps, even with millions of rows.

To check whether a query uses an index, run `EXPLAIN` before it.
