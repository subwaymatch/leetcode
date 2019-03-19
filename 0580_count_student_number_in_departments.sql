# Write your MySQL query statement below
SELECT d.dept_name, COUNT(s.student_id) as student_number
FROM department d
LEFT JOIN student s on s.dept_id = d.dept_id
GROUP BY d.dept_id
ORDER BY COUNT(s.student_id) desc, d.dept_name
