# Write your MySQL query statement below
SELECT
    ROUND(COUNT(*) / (SELECT COUNT(DISTINCT(player_id)) FROM Activity), 2) AS fraction
FROM (
    SELECT 
        player_id,
        DATE_ADD(MIN(event_date), INTERVAL 1 DAY) AS second_day
    FROM Activity
    GROUP BY player_id
) t1
WHERE EXISTS (
    SELECT 1
    FROM Activity t2
    WHERE t1.player_id = t2.player_id AND
        t1.second_day = t2.event_date
);
