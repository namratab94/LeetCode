--Problem Number: 196
--Difficulty level: Easy
--Link: https://leetcode.com/problems/delete-duplicate-emails/description/
--Author: namratabilurkar


-- SQL Schema

--Input:
--
--+----+------------------+
--| Id | Email            |
--+----+------------------+
--| 1  | john@example.com |
--| 2  | bob@example.com  |
--| 3  | john@example.com |
--+----+------------------+
--Id is the primary key column for this table.
--
--
--Output:
--
--+----+------------------+
--| Id | Email            |
--+----+------------------+
--| 1  | john@example.com |
--| 2  | bob@example.com  |
--+----+------------------+

DELETE
    p1.*
FROM
    Person p1, Person p2
WHERE
    p1.Email = p2.Email
    AND
    p1.Id > p2.Id;