# Write your MySQL query statement below
SELECT
    t.id,
    CASE 
        WHEN t.id % 2 = 1 THEN next_student
        ELSE prev_student
    END AS student
FROM (
    SELECT
        id,
        student,
        IFNULL(LEAD(student) OVER (ORDER BY id), student) AS next_student,
        LAG(student) OVER (ORDER BY id) AS prev_student
    FROM Seat
) t;
