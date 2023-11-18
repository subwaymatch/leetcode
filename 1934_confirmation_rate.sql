# Write your MySQL query statement below
SELECT 
    t1.user_id,
    ROUND(IFNULL(t2.confirmation_rate, 0), 2) AS confirmation_rate
FROM Signups t1
LEFT JOIN (
    SELECT
        s.user_id,
        SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) / COUNT(*) AS confirmation_rate
    FROM Signups s
    INNER JOIN Confirmations c ON s.user_id = c.user_id
    GROUP BY s.user_id
) t2
ON t1.user_id = t2.user_id;

# A much smarter approach by sadhana on the "Solutions" board!
SELECT 
    s.user_id,
    ROUND(AVG(if(c.action = "confirmed", 1, 0)), 2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
ON s.user_id = c.user_id
GROUP BY s.user_id;
