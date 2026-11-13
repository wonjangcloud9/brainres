<!-- Q: Write a SQL query for the top 5 customers by total order amount. -->

```sql
SELECT c.customer_id, c.name, SUM(o.total_amount) AS total_order_amount
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_order_amount DESC
LIMIT 5;
```

I assumed tables `customers(customer_id, name)` and `orders(customer_id, total_amount)`. Adjust the names to your schema.

- **SQL Server:** replace `LIMIT 5` with `SELECT TOP 5` at the start.
- **Oracle 12c+:** use `FETCH FIRST 5 ROWS ONLY`.
- **Ties at 5th place:** `LIMIT` cuts them arbitrarily. Use `RANK()` over the totals if you want all tied customers.
- **Cancelled orders:** add a `WHERE o.status <> 'cancelled'` filter if they shouldn't count.

If you share your schema, I'll match the query to it.
