-- Last updated: 07/07/2026, 13:21:12
# Write your MySQL query statement below

SELECT s.name
FROM salesperson s
LEFT JOIN (
    SELECT o.sales_id, o.order_id
    FROM company c
    JOIN orders o
      ON c.com_id = o.com_id
    WHERE c.name = 'red'
) t
ON s.sales_id = t.sales_id
WHERE t.order_id IS NULL;