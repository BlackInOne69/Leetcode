-- Last updated: 07/07/2026, 13:21:02
# Write your MySQL query statement below
select p.product_name,s.year,s.price
from sales s
join product p
where s.product_id= p.product_id

