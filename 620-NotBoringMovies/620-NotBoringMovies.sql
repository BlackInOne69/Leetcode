-- Last updated: 07/07/2026, 13:21:06
SELECT id, movie, description, rating
FROM cinema
WHERE id % 2 != 0
  AND description != 'boring'
ORDER BY rating DESC;