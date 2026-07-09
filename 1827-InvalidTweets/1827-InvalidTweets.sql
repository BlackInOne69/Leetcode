-- Last updated: 09/07/2026, 19:45:46
# Write your MySQL query statement below
SELECT tweet_id FROM Tweets
WHERE LENGTH(content) > 15;