-- Last updated: 07/07/2026, 13:21:08
# Write your MySQL query statement below
SELECT MAX(num) as num
FROM (
    SELECT num
    FROM mynumbers
    GROUP BY num
    HAVING COUNT(num) = 1
)t