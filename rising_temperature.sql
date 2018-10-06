--Problem Number: 197
--Difficulty level: Easy
--Link: https://leetcode.com/problems/rising-temperature/description/
--Author: namratabilurkar


-- SQL Schema

--Create table If Not Exists Weather (Id int, RecordDate date, Temperature int)
--Truncate table Weather
--insert into Weather (Id, RecordDate, Temperature) values ('1', '2015-01-01', '10')
--insert into Weather (Id, RecordDate, Temperature) values ('2', '2015-01-02', '25')
--insert into Weather (Id, RecordDate, Temperature) values ('3', '2015-01-03', '20')
--insert into Weather (Id, RecordDate, Temperature) values ('4', '2015-01-04', '30')

# Write your MySQL query statement below
SELECT
    w1.Id
FROM
    Weather w1
        INNER JOIN
    Weather w2
        ON
        w1.RecordDate = DATE_ADD(w2.RecordDate, INTERVAL 1 DAY)
WHERE
    w1.Temperature > w2.Temperature;
