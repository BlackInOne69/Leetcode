-- Last updated: 09/07/2026, 19:45:24
# Write your MySQL query statement below

SELECT user_id, email
FROM Users
WHERE email REGEXP '^[a-z0-9_]+@[^@0-9]+\\.com$' order by user_id