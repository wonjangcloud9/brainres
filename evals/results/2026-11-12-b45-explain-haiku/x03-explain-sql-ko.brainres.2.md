<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

This query lists users who placed at least 3 orders in the last 30 days, sorted by order count from highest to lowest.

How it works, step by step:

1. **`WHERE created_at >= NOW() - INTERVAL '30 days'`**: keeps only orders from the last 30 days.
2. **`GROUP BY user_id`**: combines the remaining rows so there is one group per user.
3. **`COUNT(*) AS c`**: counts the orders in each group and names the count `c`.
4. **`HAVING COUNT(*) >= 3`**: drops groups with fewer than 3 orders. `HAVING` filters after grouping, so it can check the count, while `WHERE` cannot.
5. **`ORDER BY c DESC`**: puts the most active users first.

The result has two columns, `user_id` and `c`. It is a common way to find frequent buyers or repeat customers in a recent window.

`NOW() - INTERVAL '30 days'` is PostgreSQL syntax. In MySQL, use `NOW() - INTERVAL 30 DAY`. The exact start boundary depends on the time zone of `created_at`, which you can check against your schema.
