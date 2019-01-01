--Problem Number: 184
--Difficulty level: Medium
--Link: https://leetcode.com/problems/department-highest-salary/
--Author: namratabilurkar

-- SQL Schema

-- Example :
--Create table If Not Exists Employee (Id int, Name varchar(255), Salary int, DepartmentId int)
--Create table If Not Exists Department (Id int, Name varchar(255))
--Truncate table Employee
--insert into Employee (Id, Name, Salary, DepartmentId) values ('1', 'Joe', '70000', '1')
--insert into Employee (Id, Name, Salary, DepartmentId) values ('2', 'Henry', '80000', '2')
--insert into Employee (Id, Name, Salary, DepartmentId) values ('3', 'Sam', '60000', '2')
--insert into Employee (Id, Name, Salary, DepartmentId) values ('4', 'Max', '90000', '1')
--Truncate table Department
--insert into Department (Id, Name) values ('1', 'IT')
--insert into Department (Id, Name) values ('2', 'Sales')


-- Input:

-- Employee

--+----+-------+--------+--------------+
--| Id | Name  | Salary | DepartmentId |
--+----+-------+--------+--------------+
--| 1  | Joe   | 70000  | 1            |
--| 2  | Henry | 80000  | 2            |
--| 3  | Sam   | 60000  | 2            |
--| 4  | Max   | 90000  | 1            |
--+----+-------+--------+--------------+

-- Department

--+----+----------+
--| Id | Name     |
--+----+----------+
--| 1  | IT       |
--| 2  | Sales    |
--+----+----------+

-- Output:

--+------------+----------+--------+
--| Department | Employee | Salary |
--+------------+----------+--------+
--| IT         | Max      | 90000  |
--| Sales      | Henry    | 80000  |
--+------------+----------+--------+

--Write your MySQL query statement below
SELECT d.name AS Department,
       e.name AS Employee,
       salary
FROM   department d
       INNER JOIN employee e
               ON d.id = e.departmentid
WHERE  ( d.id, salary ) IN (SELECT e.departmentid AS id,
                                   Max(e.salary)  AS Salary
                            FROM   employee e
                            GROUP  BY e.departmentid);