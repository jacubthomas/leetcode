'''
Difficulty Medium

Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.

Write a solution to find managers with at least five direct reports.
Return the result table in any order.

The result format is in the following example.


Example 1:
Input: 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
Output: 
+------+
| name |
+------+
| John |
+------+
'''

SELECT name                                                     -- 2) Match the employee name back to those managers
FROM Employee                                                   -- by inner joining on those id = managerId
JOIN 
(
    SELECT managerId, COUNT(managerId) AS directReports         -- 1) First identify the managerIds with at least
    FROM Employee                                               -- five people under them
    WHERE managerId IS NOT null
    GROUP BY managerId
    HAVING directReports > 4
) AS ManagerIDsWith5Reports
ON Employee.id = ManagerIDsWith5Reports.managerId;

"""
It's critical we use an (INNER) JOIN here. I very often default to LEFT JOINs.
A LEFT JOIN would return all names from Employee, despite the condition of the subquery.
An INNER JOIN works here, because like a Venn Diagram, it only combines rows from both
tables where the join condition (ON) is met.
"""