# Write your MySQL query statement below
SELECT
  r.contest_id,
  IFNULL(ROUND(COUNT(u.user_id) / (SELECT COUNT(*) FROM Users) * 100, 2), 0) AS percentage
FROM Register r
LEFT JOIN Users u ON r.user_id = u.user_id
GROUP BY r.contest_id
ORDER BY percentage DESC, contest_id;
