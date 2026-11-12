<!-- Q: What is a database index? -->

A database index is a separate data structure that lets the database find rows without scanning the whole table. It works like a book's index: instead of reading every page to find a topic, you look it up in a sorted list that points to the page.

Most indexes are B-trees, a sorted tree where each lookup takes a few steps even for millions of rows. Without an index, a query like `WHERE email = 'a@b.com'` reads every row (a full table scan). With an index on `email`, the database jumps straight to the matching rows.

```sql
CREATE INDEX idx_users_email ON users(email);
```

**Trade-off:** each index speeds up reads on its columns but slows down `INSERT`, `UPDATE`, and `DELETE`, because the index must be updated too. It also uses extra disk space. Index only the columns you filter, join, or sort on most often.

To check whether a query uses an index, run `EXPLAIN` (PostgreSQL, MySQL) or `EXPLAIN QUERY PLAN` (SQLite) before the query. If the output shows a full scan on a large table, an index on the filtered column is the usual fix.
