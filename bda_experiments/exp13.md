# Question 13: Implement Hive DDL Commands
Aim
To implement all Hive Data Definition Language (DDL) commands.
Procedure
```sql
-- 1. CREATE DATABASE & TABLE
CREATE DATABASE IF NOT EXISTS college_db;
USE college_db;
CREATE TABLE IF NOT EXISTS employee (
 eid INT,
 ename STRING,
 salary FLOAT,
 dept STRING
)
COMMENT 'Employee details table'
PARTITIONED BY (year STRING)
CLUSTERED BY (eid) INTO 3 BUCKETS
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
-- 2. SHOW TABLES
SHOW TABLES;
SHOW TABLES LIKE 'emp*';
-- 3. DESCRIBE
DESCRIBE employee;
DESCRIBE FORMATTED employee;
DESCRIBE EXTENDED employee;
-- 4. ALTER (add column, rename, change)
ALTER TABLE employee ADD COLUMNS (city STRING COMMENT 'city name');
ALTER TABLE employee RENAME TO emp_details;
ALTER TABLE employee CHANGE COLUMN ename emp_name STRING;
-- 5. DROP (table, partition)
ALTER TABLE employee DROP IF EXISTS PARTITION (year='2020');
DROP TABLE IF EXISTS emp_details;
DROP DATABASE college_db CASCADE;
-- 6. TRUNCATE
TRUNCATE TABLE employee;
```