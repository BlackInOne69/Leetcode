-- Last updated: 09/07/2026, 19:45:26
# Write your MySQL query statement below
Select  teacher_id ,
count(distinct subject_id ) as cnt from Teacher
group by teacher_id