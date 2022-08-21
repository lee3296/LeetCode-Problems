# Write your MySQL query statement below
SELECT Salary AS SecondHighestSalary
FROM Employee
ORDER BY Salary DESC #order table by salary descending, highest first
LIMIT 1 OFFSET 1 #offset of 1 with limit of 1 entry


-- ONE METHOD:
-- STRIP AWAY HIGHEST SALARY AND GET HIGHEST SALARY FROM NEW TABLE
-- SELECT MAX(Salary) AS SecondHighestSalary
-- FROM Employee
-- WHERE Salary NOT IN ( # can also use < instead of NOT IN
    -- SELECT MAX(Salary) FROM Employee
-- )
