# MySQL SELECT Docs:
# "You are permitted to specify DUAL as a dummy table name 
# in situations where no tables are referenced"
# FROM DUAL is optional
SELECT (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
    ORDER BY num DESC
    LIMIT 1
) AS num
FROM DUAL;
