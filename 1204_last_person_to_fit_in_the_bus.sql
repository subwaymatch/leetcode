# Write your MySQL query statement below
SELECT 
    t.person_name
FROM (
    SELECT
        turn,
        person_id,
        person_name,
        weight,
        SUM(weight) OVER (ORDER BY turn) AS total_weight
    FROM Queue
) t
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1;
