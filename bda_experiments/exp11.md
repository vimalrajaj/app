# Question 11: HQL Commands on Student Table
Aim
To create a student table and execute SELECT, GROUP BY, WHERE, and ORDER BY HQL queries.
Procedure
1. Create Table:
```sql
CREATE TABLE student (
 sno INT,
 sname STRING,
 department STRING,
 marks INT,
 city STRING
) ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
```
2. Load Data:
```sql
LOAD DATA LOCAL INPATH '/home/students.csv' INTO TABLE student;
```
3. SELECT all fields:
```sql
SELECT * FROM student;
```
4. GROUP BY department:
```sql
SELECT department, AVG(marks) as avg_marks, COUNT(*) as count
FROM student
GROUP BY department;
```
5. WHERE condition:
```sql
SELECT * FROM student WHERE marks > 70 AND city = 'Chennai';
```
6. ORDER BY sno:
```sql
SELECT * FROM student ORDER BY sno;
```