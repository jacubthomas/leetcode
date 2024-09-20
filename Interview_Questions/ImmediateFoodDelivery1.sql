'''
Table: Delivery
+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id is the primary key (column with unique values) of this table.
The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).

If the customer\'s preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.
Write a solution to find the percentage of immediate orders in the table, rounded to 2 decimal places.

The result format is in the following example.

Example 1:
Input: 
Delivery table:
+-------------+-------------+------------+-----------------------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
+-------------+-------------+------------+-----------------------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 5           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-11                  |
| 4           | 3           | 2019-08-24 | 2019-08-26                  |
| 5           | 4           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
+-------------+-------------+------------+-----------------------------+
Output: 
+----------------------+
| immediate_percentage |
+----------------------+
| 33.33                |
+----------------------+
Explanation: The orders with delivery id 2 and 3 are immediate while the others are scheduled.
'''

-- We want a final decimal value rounded to 2 decimal places named `immediate_percentage`
-- To calculate that final value, we need the percent of immediate / total deliveries

-- Approach 1: Using AVG aggregation
SELECT ROUND(((COUNT(CASE WHEN order_date = customer_pref_delivery_date THEN 1 END) / COUNT(*))*100), 2) AS immediate_percentage
FROM Delivery;

-- Approach 2: Using COUNT aggregations
SELECT ROUND((AVG(order_date = customer_pref_delivery_date)*100), 2) AS immediate_percentage
FROM Delivery;

-- Approach 3: Using CTEs and nested subquery
SELECT ROUND((Immediate / Total) * 100, 2) AS immediate_percentage
FROM
(
    -- Get all the delivery_ids in the Delivery table
    WITH total_orders AS
    (
        SELECT delivery_id
        FROM Delivery
    ), 
    -- Get only the immediate delivery_ids in the Delivery table
    immediate_orders AS 
    (
        SELECT delivery_id
        FROM Delivery 
        WHERE order_date = customer_pref_delivery_date
    )
    -- Aggregate the results of the the above CTE into a two column table {Total, Immediate}
    SELECT COUNT(total_orders.delivery_id) AS Total, COUNT(immediate_orders.delivery_id) AS Immediate
    FROM total_orders 
    LEFT JOIN immediate_orders
    ON immediate_orders.delivery_id = total_orders.delivery_id
) AS aggregated_counts;