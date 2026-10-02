-- https://leetcode.com/problems/customers-who-never-order/
-- Write a solution to find all customers who never order anything.
-- Return the result table in any order.
-- The result format is in the following example.
-- Create table If Not Exists Customers (id int, name varchar(255))
-- Create table If Not Exists Orders (id int, customerId int)
-- Truncate table Customers
-- insert into Customers (id, name) values ('1', 'Joe')
-- insert into Customers (id, name) values ('2', 'Henry')
-- insert into Customers (id, name) values ('3', 'Sam')
-- insert into Customers (id, name) values ('4', 'Max')
-- Truncate table Orders
-- insert into Orders (id, customerId) values ('1', '3')
-- insert into Orders (id, customerId) values ('2', '1')
-- My solution
SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.customerId IS NULL;
