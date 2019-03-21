# Write your MySQL query statement below
SELECT (
    SELECT num
    FROM my_numbers
    GROUP BY num
    HAVING COUNT(*) = 1
    ORDER BY num desc
    LIMIT 1
) AS num;
