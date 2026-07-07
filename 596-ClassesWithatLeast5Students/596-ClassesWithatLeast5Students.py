# Last updated: 07/07/2026, 12:47:13
# Write your MySQL query statement below

SELECT *, IF(x+y>z and y+z>x and z+x>y, "Yes", "No") as triangle FROM Triangle