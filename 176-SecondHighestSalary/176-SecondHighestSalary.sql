-- Last updated: 09/07/2026, 19:46:40
# Write your MySQL query statement below
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);