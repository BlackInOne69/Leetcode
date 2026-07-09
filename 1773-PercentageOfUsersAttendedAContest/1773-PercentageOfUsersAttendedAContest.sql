-- Last updated: 09/07/2026, 19:45:50
# Write your MySQL query statement below
select 
contest_id, 
round(count(distinct user_id) * 100 /(select count(user_id) from Users) ,2) as percentage
from  Register
group by contest_id
order by percentage desc,contest_id