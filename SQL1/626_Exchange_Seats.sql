-- Table: Seat

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | student     | varchar |
-- +-------------+---------+
-- id is the primary key column for this table.
-- Each row of this table indicates the name and the ID of a student.
-- id is a continuous increment.
 

-- Write an SQL query to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

-- Return the result table ordered by id in ascending order.

-- The query result format is in the following example.

 

-- Example 1:

-- Input: 
-- Seat table:
-- +----+---------+
-- | id | student |
-- +----+---------+
-- | 1  | Abbot   |
-- | 2  | Doris   |
-- | 3  | Emerson |
-- | 4  | Green   |
-- | 5  | Jeames  |
-- +----+---------+
-- Output: 
-- +----+---------+
-- | id | student |
-- +----+---------+
-- | 1  | Doris   |
-- | 2  | Abbot   |
-- | 3  | Green   |
-- | 4  | Emerson |
-- | 5  | Jeames  |
-- +----+---------+
-- Explanation: 
-- Note that if the number of students is odd, there is no need to change the last one's seat.

Create table If Not Exists Seat (id int, student varchar(255));
Truncate table Seat;
insert into Seat (id, student) values ('1', 'Abbot');
insert into Seat (id, student) values ('2', 'Doris');
insert into Seat (id, student) values ('3', 'Emerson');
insert into Seat (id, student) values ('4', 'Green');
insert into Seat (id, student) values ('5', 'Jeames');
-- insert into Seat (id, student) values ('6', 'SVEN');



SELECT new_id AS id, student
FROM
 ( 
	SELECT *,  CASE
		WHEN id = 1 AND size_ > 1 THEN 2
		WHEN id % 2 = 0 AND size_ % 2 = 0 THEN (SELECT id - 1)
		WHEN id % 2 = 1 AND size_ % 2 = 0 THEN (SELECT id + 1) 
		WHEN id % 2 = 0 AND id < size_ AND size_ % 2 = 1 THEN (SELECT id - 1)
		WHEN id % 2 = 1 AND id < size_ AND size_ % 2 = 1 THEN (SELECT id + 1) 
		WHEN id = size_ AND size_ % 2 = 1 THEN id
		END AS new_id
	FROM Seat
	JOIN (SELECT COUNT(*) AS size_ FROM Seat) AS SIZE ) AS nested
    ORDER BY new_id ASC;


-------------- THIS SOLUTION WORKS AS WELL, BUT NOT ON LEETCODE

-- DELIMITER $$
-- CREATE PROCEDURE TESTS()
-- BEGIN
-- 	SET @Counter = (SELECT min(id) FROM Seat);
--     SET @TOP = (SELECT max(id) FROM Seat);
--     SET @ODDOREVEN = (SELECT COUNT(*) FROM Seat);
-- 	SET @ODDOREVEN = IF(@ODDOREVEN % 2 = 0, @TOP, @TOP - 1);
--     WHILE @Counter < @ODDOREVEN  DO
-- 	SET @NAME1 = (SELECT student FROM Seat WHERE id = (@Counter));
--     SET @NAME2 = (SELECT student FROM Seat WHERE id = (@Counter + 1));
--     UPDATE Seat SET student = @NAME2 WHERE id = @Counter;
-- 	UPDATE Seat SET student = @NAME1 WHERE id = (@Counter  + 1);
--     SET @Counter := @Counter + 2;
--     END WHILE;
--     SELECT * FROM Seat ORDER BY id ASC;
-- END $$

-- CALL TESTS();