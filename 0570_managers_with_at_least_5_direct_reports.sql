# Write your MySQL query statement below
SELECT e2.name
FROM Employee e1
JOIN Employee e2 ON e1.managerId = e2.id
WHERE e1.managerId IS NOT NULL
GROUP BY e1.managerId
HAVING COUNT(*) >= 5;
