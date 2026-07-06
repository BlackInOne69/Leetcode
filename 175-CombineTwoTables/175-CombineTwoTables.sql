-- Last updated: 06/07/2026, 17:36:56
# Write your MySQL query statement below
select p.firstName, p.lastName, a.city, a.state
from Person p
left join Address a
on p.personId = a.personId
