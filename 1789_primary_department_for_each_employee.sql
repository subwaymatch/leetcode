# Write your MySQL query statement below
SELECT 
    t1.employee_id,
    t2.department_id
FROM (
    SELECT employee_id
    FROM Employee
    GROUP BY employee_id
    HAVING COUNT(department_id) = 1
) t1
INNER JOIN Employee t2 ON t1.employee_id = t2.employee_id
UNION
SELECT 
    t1.employee_id,
    t2.department_id
FROM (
    SELECT employee_id
    FROM Employee
    GROUP BY employee_id
    HAVING COUNT(department_id) > 1
) t1
INNER JOIN Employee t2 ON t1.employee_id = t2.employee_id
WHERE t2.primary_flag = "Y";
