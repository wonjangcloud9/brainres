<!-- Q: Write a SQL query for the top 5 customers by total order amount. -->

Assuming typical `customers` and `orders` tables:

```sql
SELECT
    c.customer_id,
    c.name,
    SUM(o.total_amount) AS total_order_amount
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_order_amount DESC
LIMIT 5;
```

Notes:
- **Column names** (`total_amount`, `customer_id`, `name`) are guesses; adjust to your schema.
- **SQL Server / Oracle:** replace `LIMIT 5` with `SELECT TOP 5 ...` (SQL Server) or `FETCH FIRST 5 ROWS ONLY` (Oracle 12c+).
- **Ties:** if you want to include customers tied for 5th place, use `RANK()`:

```sql
SELECT customer_id, name, total_order_amount
FROM (
    SELECT
        c.customer_id,
        c.name,
        SUM(o.total_amount) AS total_order_amount,
        RANK() OVER (ORDER BY SUM(o.total_amount) DESC) AS rnk
    FROM customers c
    JOIN orders o ON o.customer_id = c.customer_id
    GROUP BY c.customer_id, c.name
) ranked
WHERE rnk <= 5;
```

If orders store line items in a separate table (e.g., `order_items` with `quantity * unit_price`), let me know and I'll adjust the sum.
