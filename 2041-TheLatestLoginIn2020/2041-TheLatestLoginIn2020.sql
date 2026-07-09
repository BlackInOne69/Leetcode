-- Last updated: 09/07/2026, 19:45:22
# Write your MySQL query statement below
select user_id,
max(time_stamp) as last_stamp
from logins 
where year(time_stamp)=2020
group by user_id;