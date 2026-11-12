<!-- Q: What can I do to speed up a slow database query? -->

- Add an index on the columns you filter by (skips most rows)
- Select only the columns you need, not SELECT *
- Add a LIMIT if you only show the first page
- Cache the result if the data changes rarely
