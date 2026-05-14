# 14. Develop automated test scripts for database validation and data integrity testing using SQL queries
## Aim
To develop automated test scripts for database validation and data integrity testing using SQL queries.

## Procedure
1. Identify tables and relationships.
2. Prepare test data and expected database state.
3. Execute application actions.
4. Run SQL queries to verify records.
5. Compare output with expected values.

## Sample SQL Queries
```sql
SELECT * FROM orders WHERE customer_id NOT IN (SELECT customer_id FROM customers);

SELECT order_id, total_amount
FROM orders
WHERE total_amount <> (
    SELECT SUM(qty * unit_price)
    FROM order_items
    WHERE order_items.order_id = orders.order_id
);
```

## Output
Automated SQL validation scripts and database integrity checks are prepared.
