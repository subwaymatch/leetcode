# Write your MySQL query statement below
SELECT DISTINCT p1.product_id, IFNULL(p4.new_price, 10) AS price
FROM products p1
LEFT JOIN (
    SELECT p2.product_id, p2.change_date, p2.new_price
    FROM Products p2
    INNER JOIN (
        SELECT product_id, MAX(change_date) AS change_date
        FROM Products
        WHERE change_date <= '2019-08-16'
        GROUP BY product_id
    ) p3 ON p2.product_id = p3.product_id AND p2.change_date = p3.change_date
) p4 ON p1.product_id = p4.product_id;
