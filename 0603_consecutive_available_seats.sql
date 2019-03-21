# Write your MySQL query statement below
SELECT seat_id
FROM cinema as c
WHERE free = 1
    AND (
        SELECT COUNT(*) 
        FROM cinema 
        WHERE free = 1 
            AND (seat_id = c.seat_id - 1 or seat_id = c.seat_id + 1)
    ) > 0
