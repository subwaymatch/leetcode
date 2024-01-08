# Write your MySQL query statement below
SELECT
    DISTINCT num AS ConsecutiveNums
FROM (
    SELECT id, num,
    num = LAG(num, 1) OVER (ORDER BY id) AND 
    num = LAG(num, 2) OVER (ORDER BY id) AS three_consecutive
    FROM Logs
) AS t
WHERE t.three_consecutive = 1;
