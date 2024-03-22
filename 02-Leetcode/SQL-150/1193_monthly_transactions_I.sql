"""
Table: Transactions

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].

"""
SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') AS month, 
    country,
    COUNT(trans_date) AS trans_count,
    COUNT(IF(transactions.state='approved', state, NULL)) AS approved_count,
    SUM(amount) AS trans_total_amount, 
    SUM(IF(state='approved', amount, 0)) AS approved_total_amount 
FROM 
    Transactions 
GROUP BY 
    month, 
    country;
