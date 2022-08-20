# Write your MySQL query statement below
SELECT (
    SELECT salary AS secondHighestSalary
    FROM (
        SELECT
            id,
            salary,
            DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
        FROM Employee
    ) AS tmp
    WHERE salary_rank = 2
    LIMIT 1
) AS SecondHighestSalary
FROM dual;
