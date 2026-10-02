-- https://leetcode.com/problems/employees-earning-more-than-their-managers/description/
-- Write a solution to find the employees who earn more than their managers.
-- Return the result table in any order.
-- The result format is in the following example.
Create table If Not Exists Employee (id int, name varchar(255), salary int, managerId int)
Truncate table Employee
insert into Employee (id, name, salary, managerId) values ('1', 'Joe', '70000', '3')
insert into Employee (id, name, salary, managerId) values ('2', 'Henry', '80000', '4')
insert into Employee (id, name, salary, managerId) values ('3', 'Sam', '60000', NULL)
insert into Employee (id, name, salary, managerId) values ('4', 'Max', '90000', NULL)
-- My solution
SELECT e.name AS Employee -- Select the Employee's name 
FROM Employee e -- Take the Employee table and call it "e" for employes
JOIN Employee m -- Join the same Employee table and call it "m" for managers
    ON e.managerId = m.id -- Match every employee's managerId to the manager's id
WHERE e.salary > m.salary -- Keep only the rows where the salary of the employees are higher than the managers salary