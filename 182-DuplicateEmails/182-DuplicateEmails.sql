-- Last updated: 06/07/2026, 17:36:53
# Write your MySQL query statement below
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;