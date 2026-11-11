An index is a sorted copy of one column with a pointer back to each row, so the database can search it instead of reading every row.

Without an index, `SELECT * FROM users WHERE email = 'a@b.com'` checks every row: 1,000,000 users means 1,000,000 comparisons. With an index on `email`, the database walks a sorted tree of emails and finds the row in about 20 comparisons, because each step halves what is left.

Think of a book's index: you jump straight to the page instead of reading the whole book. The analogy breaks on writes. The database must also update the index on every insert, so writes get a little slower.

So index the columns you filter or join on often, not every column.

To check, run `EXPLAIN` on the query in Postgres. `Seq Scan` means no index was used, and `Index Scan` means it was.
