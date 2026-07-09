-- Last updated: 09/07/2026, 19:45:57
# Write your MySQL query statement below
SELECT 
    u.name, SUM(t.amount) AS balance
FROM 
    Users u
JOIN 
    Transactions t
ON 
    u.account = t.account
GROUP BY u.account
HAVING 
    balance > 10000