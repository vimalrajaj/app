# Question 2: Implement HIVE Commands – IMPORT, DISTRIBUTE BY, EXPORT, SORT BY, CLUSTER BY
Aim
To implement advanced Hive commands: IMPORT, EXPORT, DISTRIBUTE BY, SORT BY, and CLUSTER BY.
Procedure
1. Start Hive CLI: `hive`
2. Create and load base table:
```sql
CREATE TABLE emp (id INT, name STRING, dept STRING, salary FLOAT)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
LOAD DATA LOCAL INPATH '/home/user/emp.csv' INTO TABLE emp;
```
3. EXPORT:
```sql
EXPORT TABLE emp TO '/user/hive/exports/emp_exp';
```
4. IMPORT:
```sql
DROP TABLE emp;
IMPORT FROM '/user/hive/exports/emp_exp';
```
5. DISTRIBUTE BY:
```sql
INSERT OVERWRITE LOCAL DIRECTORY '/tmp/out_dist'
SELECT * FROM emp DISTRIBUTE BY dept;
```
6. SORT BY:
```sql
SELECT * FROM emp SORT BY salary DESC;
```
7. CLUSTER BY:
```sql
SELECT * FROM emp CLUSTER BY id;
```
Output & Results
• EXPORT creates _metadata and data directories in HDFS.
• IMPORT recreates the emp table.
• DISTRIBUTE BY distributes rows to reducers by dept hash.
• SORT BY shows results sorted within each mapper/reducer output file.
• CLUSTER BY groups same id together and sorts within group.