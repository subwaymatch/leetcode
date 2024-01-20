# Write your MySQL query statement below
SELECT 
    t.category,
    SUM(t.accounts_count) AS accounts_count
FROM (
    SELECT
        CASE
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income <= 50000 THEN 'Average Salary'
            ELSE 'High Salary'
        END AS category,
        COUNT(*) AS accounts_count
    FROM Accounts
    GROUP BY category
    UNION ALL SELECT 'Low Salary', 0
    UNION ALL SELECT 'Average Salary', 0
    UNION ALL SELECT 'High Salary', 0
) t
GROUP BY category;
