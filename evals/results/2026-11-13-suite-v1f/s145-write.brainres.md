<!-- Q: Write a SQL query for the top 5 customers by total order amount. -->

```sql
SELECT c.customer_id, c.name, SUM(o.amount) AS total_order_amount
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_order_amount DESC
LIMIT 5;
```

I assumed tables `customers(customer_id, name)` and `orders(customer_id, amount)`. Rename them to match your schema. If orders store line items in a separate table, sum `quantity * price` from that table instead.

For SQL Server use `SELECT TOP 5` instead of `LIMIT 5`; for Oracle use `FETCH FIRST 5 ROWS ONLY`. If you want to exclude cancelled orders, add `WHERE o.status <> 'cancelled'` before `GROUP BY`.

Send me your schema and I'll adjust the query to fit.
