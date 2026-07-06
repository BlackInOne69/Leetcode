-- Last updated: 06/07/2026, 18:08:35
# Write your MySQL query statement below
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;