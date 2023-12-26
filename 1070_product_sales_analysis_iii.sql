# ----------------------------------
# Solution 1 - Using an inner join
# ----------------------------------
SELECT s1.product_id, s1.year AS first_year, s1.quantity, s1.price
FROM Sales s1
INNER JOIN (
    SELECT product_id, MIN(year) AS year
    FROM Sales
    GROUP BY product_id
) s2 ON (s1.product_id = s2.product_id) AND (s1.year = s2.year);


# ----------------------------------
# Solution 2 - Using WHERE IN
# ----------------------------------
SELECT s1.product_id, s1.year AS first_year, s1.quantity, s1.price
FROM Sales s1
WHERE (s1.product_id, s1.year) IN (
    SELECT product_id, MIN(year)
    FROM Sales
    GROUP BY product_id
);


# ----------------------------------
# Solution 3 - Using a window function
# ----------------------------------
WITH cte AS
(
    SELECT 
        *,
        RANK() OVER(PARTITION BY product_id ORDER BY year) AS rn
    FROM Sales
)
SELECT product_id, year as first_year, quantity, price
FROM cte
WHERE rn = 1;
