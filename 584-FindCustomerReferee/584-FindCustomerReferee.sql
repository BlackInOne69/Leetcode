-- Last updated: 06/07/2026, 18:19:36
# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;