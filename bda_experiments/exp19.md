# Question 19: HQL – Bank Account Table
Aim
To create a bank account table, load data, and display contents using HiveQL.
Procedure
(I) Create Table:
```sql
CREATE TABLE bank_account (
 cid INT,
 cname STRING,
 cage INT,
 acctype STRING,
 balance DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
```
(II) Load Data:
Prepare `bank_data.csv` with sample records.
Load:
```sql
LOAD DATA LOCAL INPATH '/home/bank_data.csv' INTO TABLE bank_account;
```
(III) Display Content:
```sql
SELECT * FROM bank_account;
SELECT cname, balance FROM bank_account WHERE balance > 10000;
SELECT acctype, COUNT(*) as count, AVG(balance) as avg_bal FROM bank_account GROUP BY acctype;
```