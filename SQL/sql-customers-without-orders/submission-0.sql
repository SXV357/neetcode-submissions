-- Write your query below

SELECT
    c.name
FROM
    customers c
WHERE c.id NOT IN (
    SELECT customer_id
    FROM orders
)