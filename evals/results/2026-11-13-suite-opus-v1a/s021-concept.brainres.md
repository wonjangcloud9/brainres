<!-- Q: What is a database index? -->

A database index is a separate, sorted data structure that lets the database find rows without scanning the whole table. It works like the index at the back of a book: you look up a term and jump straight to the page.

## How it works

Without an index, a query like `WHERE email = 'a@b.com'` forces a **full table scan**, meaning the database reads every row. With an index on `email`, the database keeps the email values sorted, each with a pointer to its row. It can then find a match in a few steps instead of millions.

Most databases (PostgreSQL, MySQL, SQLite) use a **B-tree** by default. A B-tree is a balanced, sorted tree, so lookups, range queries (`>`, `<`, `BETWEEN`) and `ORDER BY` all get faster.

## Worked example

```sql
-- Slow on a large table: scans every row
SELECT * FROM users WHERE email = 'a@b.com';

-- Create the index once
CREATE INDEX idx_users_email ON users (email);

-- Same query now uses the index
EXPLAIN SELECT * FROM users WHERE email = 'a@b.com';
```

`EXPLAIN` shows the query plan. You should see "Index Scan" (PostgreSQL) or `key: idx_users_email` (MySQL) instead of "Seq Scan" or `type: ALL`.

## The trade-off

| | Benefit | Cost |
|---|---|---|
| Reads | Much faster lookups and sorts | — |
| Writes | — | Every `INSERT`/`UPDATE`/`DELETE` must also update the index |
| Storage | — | Extra disk space per index |

So index the columns you filter, join or sort on often. Don't index every column.

To see the effect yourself, run `EXPLAIN` on one of your slow queries before and after adding an index.
