# Write your MySQL query statement below
SELECT FirstName, lastName, City, State
FROM Person 
LEFT JOIN Address 
    ON Person.PersonId = Address.PersonId
