<!-- Q: What can I do to speed up a slow database query? -->

Add an index on the columns you filter by, which lets the database skip most rows. Select only the columns you need instead of SELECT *. Add a LIMIT if you only show the first page. And cache the result if the data changes rarely.
