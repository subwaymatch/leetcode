CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT salary AS nthHighestSalary
      FROM (
          SELECT salary, salary_rank
          FROM (
              SELECT
                salary,
                DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
              FROM Employee
          ) AS tmp1
          WHERE salary_rank = N
          LIMIT 1
      ) AS tmp2
  );
END
