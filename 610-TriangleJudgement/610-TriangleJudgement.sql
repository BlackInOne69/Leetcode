-- Last updated: 07/07/2026, 13:21:10
# Write your MySQL query statement below
SELECT *, IF(x+y>z and y+z>x and z+x>y, "Yes", "No") as triangle FROM Triangle