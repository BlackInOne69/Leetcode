-- Last updated: 06/07/2026, 17:57:21
# Write your MySQL query statement below
DELETE p
FROM Person p
JOIN Person e
ON p.email = e.email
AND p.id > e.id;