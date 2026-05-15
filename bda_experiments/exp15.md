# Question 15: Implement HIVE Commands – CREATE, SHOW, DESCRIBE, USE, DROP, ALTER
Aim
To implement basic Hive management commands: CREATE, SHOW, DESCRIBE, USE, DROP, and ALTER.
Procedure
```sql
-- CREATE Database and Table
CREATE DATABASE test_db;
USE test_db;
CREATE TABLE products (
 pid INT,
 pname STRING,
 price DOUBLE
) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
-- SHOW
SHOW DATABASES;
SHOW TABLES;
-- DESCRIBE
DESCRIBE products;
DESCRIBE EXTENDED products;
-- USE another DB
USE default;
-- ALTER
ALTER TABLE test_db.products ADD COLUMNS (category STRING);
ALTER TABLE test_db.products RENAME TO inventory;
-- DROP
DROP TABLE test_db.inventory;
DROP DATABASE test_db CASCADE;
```