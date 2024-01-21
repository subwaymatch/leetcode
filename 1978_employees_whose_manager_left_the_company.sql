# Write your MySQL query statement below
SELECT t1.employee_id
FROM Employees t1
LEFT JOIN Employees t2 ON t1.manager_id = t2.employee_id
WHERE t1.salary < 30000 AND t1.manager_id IS NOT NULL AND t2.employee_id IS NULL
ORDER BY t1.employee_id;
