# Question 8: Implement All Hive DML Commands
Aim
To implement all Hive Data Manipulation Language (DML) commands.
Procedure
1. Set up table for transactional operations:
```sql
SET hive.support.concurrency=true;
SET hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager;
CREATE TABLE student_dml (id INT, name STRING, marks INT)
CLUSTERED BY (id) INTO 2 BUCKETS
STORED AS ORC
TBLPROPERTIES('transactional'='true');
```
2. LOAD DATA:
```sql
LOAD DATA LOCAL INPATH '/home/student_data.txt' INTO TABLE student_dml;
```
3. INSERT:
```sql
INSERT INTO student_dml VALUES (101, 'Ajay', 85);
INSERT OVERWRITE DIRECTORY '/output/students' SELECT * FROM student_dml WHERE marks > 60;
```
4. UPDATE:
```sql
UPDATE student_dml SET marks = 90 WHERE id = 101;
```
5. DELETE:
```sql
DELETE FROM student_dml WHERE marks < 40;
```
6. MERGE:
```sql
MERGE INTO student_dml AS T
USING new_student_data AS S
ON T.id = S.id
WHEN MATCHED THEN UPDATE SET marks = S.marks
WHEN NOT MATCHED THEN INSERT VALUES (S.id, S.name, S.marks);
```