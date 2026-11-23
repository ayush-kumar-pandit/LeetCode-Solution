/* Write your T-SQL query statement below */
-- MS SQL Server 

SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) AS rank FROM scores;