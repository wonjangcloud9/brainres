<!-- Q: 이 쿼리 뭐 하는 거야?

```sql
SELECT user_id, COUNT(*) AS c
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY user_id
HAVING COUNT(*) >= 3
ORDER BY c DESC;
``` -->

Users with 3 or more orders in the last 30 days, sorted by order count (highest first).

- `WHERE created_at >= NOW() - INTERVAL '30 days'`: keeps only orders from the last 30 days.
- `GROUP BY user_id`: collapses the rows into one per user.
- `COUNT(*) AS c`: counts each user's orders.
- `HAVING COUNT(*) >= 3`: drops users with fewer than 3 orders. `HAVING` filters after grouping, which is why it can use the count and `WHERE` cannot.
- `ORDER BY c DESC`: puts the most active buyers first.

The result is a list of frequent buyers, which could feed a loyalty or re-engagement campaign. This is PostgreSQL syntax (`INTERVAL '30 days'`), so it will fail on engines that lack that form.
