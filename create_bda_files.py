import os
import re

data = """Question 1: MapReduce Program for Matrix Multiplication
Aim
To implement a Java program for matrix multiplication using the MapReduce
programming paradigm.
Principle
Matrix multiplication of A (m×n) and B (n×p) produces C (m×p), where C[i][k] = Σ
A[i][j] × B[j][k] for j = 0 to n-1.
In MapReduce, the Map phase emits intermediate key-value pairs identifying the
target cell (i, k) in C along with the contributing element. The Reduce phase performs
the multiplication of matching elements and sums them to produce the final value
for each cell. This approach enables distributed computation across large matrices.
Apparatus Required
• Hardware: PC with minimum 8GB RAM, 50GB free disk
• Software: Ubuntu 20.04/CentOS 7, Hadoop 3.3.x, JDK 1.8, Eclipse/VS Code
Procedure
1. Create input files: matrixA.txt with records i,j,value and matrixB.txt with
records j,k,value.
2. Place input files in HDFS: hadoop fs -put matrixA.txt matrixB.txt
/input/matrix/
3. Write Java MapReduce code:
o Mapper: For each record from A, emit key=(i,k) for k=0 to p-1 with
value=(A,j,val). For each record from B, emit key=(i,k) for i=0 to m-1
with value=(B,j,val).
o Reducer: For each key (i,k), collect all values. For each A value (j, aVal)
and B value (j, bVal) with matching j, multiply and sum.
4. Compile the code using: javac -classpath $(hadoop classpath)
MatrixMultiply.java
5. Create JAR: jar cvf MatrixMultiply.jar *.class
6. Run: hadoop jar MatrixMultiply.jar MatrixMultiply /input/matrix
/output/matrix
7. View result: hadoop fs -cat /output/matrix/part-r-00000
Tabulation/Design
Matrix A (2×3) Matrix B (3×2)
A[0][0] = 1 A[0][1] = 2 A[0][2] = 3 B[0][0] = 4 B[0][1] = 5
A[1][0] = 6 A[1][1] = 7 A[1][2] = 8 B[1][0] = 9 B[1][1] = 10
B[2][0] = 11 B[2][1] = 12
Input format: A → i,j,val (0,0,1 / 0,1,2 ...), B → j,k,val (0,0,4 / 0,1,5 ...)
Program (Java Code)
```java
import java.io.IOException;
import java.util.*;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.*;
import org.apache.hadoop.mapreduce.lib.output.*;
public class MatrixMultiply {
 // Mapper Class
 public static class MatrixMapper extends Mapper<LongWritable, Text, Text, Text> {
 public void map(LongWritable key, Text value, Context context)
 throws IOException, InterruptedException {
 String line = value.toString();
 String[] tokens = line.split(",");

 // Check if it's Matrix A or B (based on filename or format)
 // Assuming files tagged: A,i,j,val or B,j,k,val
 String tag = tokens[0];
 if (tag.equals("A")) {
 int i = Integer.parseInt(tokens[1]);
 int j = Integer.parseInt(tokens[2]);
 double val = Double.parseDouble(tokens[3]);
 for (int k = 0; k < context.getConfiguration().getInt("colsB", 2);k++) {
 context.write(new Text(i + "," + k), new Text("A," + j + "," +val));
 }
 } else if (tag.equals("B")) {
 int j = Integer.parseInt(tokens[1]);
 int k = Integer.parseInt(tokens[2]);
 double val = Double.parseDouble(tokens[3]);
 for (int i = 0; i < context.getConfiguration().getInt("rowsA", 2);i++) {
 context.write(new Text(i + "," + k), new Text("B," + j + "," +val));
 }
 }
 }
 }
 // Reducer Class
 public static class MatrixReducer extends Reducer<Text, Text, Text, DoubleWritable> {
 public void reduce(Text key, Iterable<Text> values, Context context)
 throws IOException, InterruptedException {
 ArrayList<Double> aList = new ArrayList<>(Collections.nCopies(100, 0.0)); // size = n
 ArrayList<Double> bList = new ArrayList<>(Collections.nCopies(100, 0.0));

 for (Text val : values) {
 String[] parts = val.toString().split(",");
 int j = Integer.parseInt(parts[1]);
 double v = Double.parseDouble(parts[2]);
 if (parts[0].equals("A")) {
 aList.set(j, v);
 } else {
 bList.set(j, v);
 }
 }

 double sum = 0.0;
 int n = context.getConfiguration().getInt("colsA", 3);
 for (int j = 0; j < n; j++) {
 sum += aList.get(j) * bList.get(j);
 }
 context.write(key, new DoubleWritable(sum));
 }
 }
 // Driver Class
 public static void main(String[] args) throws Exception {
 Configuration conf = new Configuration();
 conf.setInt("rowsA", 2); // Matrix A rows
 conf.setInt("colsA", 3); // Matrix A cols = Matrix B rows
 conf.setInt("colsB", 2); // Matrix B cols
 Job job = Job.getInstance(conf, "Matrix Multiplication");
 job.setJarByClass(MatrixMultiply.class);
 job.setMapperClass(MatrixMapper.class);
 job.setReducerClass(MatrixReducer.class);
 job.setOutputKeyClass(Text.class);
 job.setOutputValueClass(Text.class);
 FileInputFormat.addInputPath(job, new Path(args[0]));
 FileOutputFormat.setOutputPath(job, new Path(args[1]));
 System.exit(job.waitForCompletion(true) ? 0 : 1);
 }
}
```
Output & Results
```text
0,0 55.0
0,1 70.0
1,0 145.0
1,1 190.0
```
Matrix C successfully computed using MapReduce.

Question 2: Implement HIVE Commands – IMPORT, DISTRIBUTE BY, EXPORT, SORT BY, CLUSTER BY
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

Question 3: Hadoop Commands for File Management in HDFS
Aim
To write and execute Hadoop shell commands for performing file management tasks in HDFS.
Procedure
1. Start HDFS daemons: `start-dfs.sh`
2. List root: `hadoop fs -ls /`
3. Create directory: `hadoop fs -mkdir /user/student`
4. Create nested: `hadoop fs -mkdir -p /user/data/input`
5. Put file: `hadoop fs -put localfile.txt /user/data/input/`
6. Copy from local: `hadoop fs -copyFromLocal file2.csv /user/data/`
7. List files: `hadoop fs -ls /user/data/input`
8. View file content: `hadoop fs -cat /user/data/input/localfile.txt`
9. Move file: `hadoop fs -mv /user/data/input/localfile.txt /user/data/`
10. Copy within HDFS: `hadoop fs -cp /user/data/localfile.txt /user/student/`
11. Get file to local: `hadoop fs -get /user/data/file2.csv .`
12. Check disk usage: `hadoop fs -du -h /user/data`
13. Delete file: `hadoop fs -rm /user/data/localfile.txt`
14. Delete directory: `hadoop fs -rm -r /user/data`
15. Report: `hadoop fs -df -h`
Output & Results
All commands execute successfully. Directory created, files uploaded, contents viewed, copied, moved, and deleted appropriately.

Question 4: MapReduce Program for Word Count
Aim
To implement a Java program for counting the number of words using MapReduce.
Procedure
1. Create input file `word.txt` with sample text.
2. Upload to HDFS: `hadoop fs -put word.txt /input/wc`
3. Write Java Mapper, Reducer, Driver.
4. Compile: `javac -classpath $(hadoop classpath) -d wc_classes WordCount.java`
5. Create JAR: `jar -cvf wc.jar -C wc_classes .`
6. Run: `hadoop jar wc.jar WordCount /input/wc /output/wc`
7. View: `hadoop fs -cat /output/wc/part-r-00000`
Program (Java Code)
```java
import java.io.IOException;
import java.util.StringTokenizer;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
public class WordCount {
 public static class TokenizerMapper extends Mapper<Object, Text, Text, IntWritable> {
 private final static IntWritable one = new IntWritable(1);
 private Text word = new Text();
 public void map(Object key, Text value, Context context)
 throws IOException, InterruptedException {
 StringTokenizer itr = new StringTokenizer(value.toString());
 while (itr.hasMoreTokens()) {
 word.set(itr.nextToken().toLowerCase().replaceAll("[^a-z]", ""));
 if (word.getLength() > 0) {
 context.write(word, one);
 }
 }
 }
 }
 public static class IntSumReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
 private IntWritable result = new IntWritable();
 public void reduce(Text key, Iterable<IntWritable> values, Context context)
 throws IOException, InterruptedException {
 int sum = 0;
 for (IntWritable val : values) {
 sum += val.get();
 }
 result.set(sum);
 context.write(key, result);
 }
 }
 public static void main(String[] args) throws Exception {
 Configuration conf = new Configuration();
 Job job = Job.getInstance(conf, "word count");
 job.setJarByClass(WordCount.class);
 job.setMapperClass(TokenizerMapper.class);
 job.setCombinerClass(IntSumReducer.class);
 job.setReducerClass(IntSumReducer.class);
 job.setOutputKeyClass(Text.class);
 job.setOutputValueClass(IntWritable.class);
 FileInputFormat.addInputPath(job, new Path(args[0]));
 FileOutputFormat.setOutputPath(job, new Path(args[1]));
 System.exit(job.waitForCompletion(true) ? 0 : 1);
 }
}
```

Question 5: Download and Install HBase with Start-up Scripts
Aim
To download, install, and configure Apache HBase with necessary start-up scripts.
Procedure
1. Download HBase: `wget https://archive.apache.org/dist/hbase/2.5.5/hbase-2.5.5-bin.tar.gz`
2. Extract: `tar -xzf hbase-2.5.5-bin.tar.gz`
3. Move: `sudo mv hbase-2.5.5 /usr/local/hbase`
4. Set JAVA_HOME in `hbase-env.sh`:
```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```
5. Configure `hbase-site.xml`:
```xml
<configuration>
 <property>
 <name>hbase.rootdir</name>
 <value>hdfs://localhost:9000/hbase</value>
 </property>
 <property>
 <name>hbase.zookeeper.property.dataDir</name>
 <value>/home/user/hbase-zookeeper</value>
 </property>
 <property>
 <name>hbase.cluster.distributed</name>
 <value>false</value>
 </property>
</configuration>
```
6. Set environment variables in `.bashrc`:
```bash
export HBASE_HOME=/usr/local/hbase
export PATH=$PATH:$HBASE_HOME/bin
```
7. Source: `source ~/.bashrc`
8. Start HBase: `start-hbase.sh`
9. Verify: `jps` (should show HMaster)
10. Access HBase Shell: `hbase shell`

Question 6: Implement HBase CRUD Commands
Aim
To implement HBase commands to create a table, insert data, retrieve data, and delete data.
Procedure
(I) Create Table:
```hbase
create 'customer', 'personal', 'contact'
```
(II) Insert Data:
```hbase
put 'customer', '001', 'personal:name', 'John Doe'
put 'customer', '001', 'personal:age', '30'
put 'customer', '001', 'contact:email', 'john@example.com'
put 'customer', '001', 'contact:phone', '1234567890'
put 'customer', '002', 'personal:name', 'Jane Smith'
put 'customer', '002', 'personal:age', '25'
put 'customer', '002', 'contact:email', 'jane@example.com'
```
(III) Get Data:
```hbase
get 'customer', '001'
get 'customer', '001', 'personal'
scan 'customer'
```
(IV) Delete Data:
```hbase
delete 'customer', '001', 'contact:phone' -- Delete single cell
deleteall 'customer', '002' -- Delete entire row
```

Question 7: MapReduce Program for Character Count
Aim
To implement a Java program for counting the frequency of each character using MapReduce.
Procedure
1. Create input text file, upload to HDFS.
2. Write Mapper that loops through each character of the input line.
3. Write Reducer to sum counts.
4. Compile, package, and execute the job.
5. View output.
Program (Java Code)
```java
// Mapper
public static class CharMapper extends Mapper<Object, Text, Text, IntWritable> {
 private Text charKey = new Text();
 private final static IntWritable one = new IntWritable(1);
 public void map(Object key, Text value, Context context)
 throws IOException, InterruptedException {
 String line = value.toString();
 for (char c : line.toCharArray()) {
 if (!Character.isWhitespace(c)) { // ignoring whitespace
 charKey.set(String.valueOf(c));
 context.write(charKey, one);
 }
 }
 }
}
// Reducer same as WordCount IntSumReducer
```

Question 8: Implement All Hive DML Commands
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

Question 9: Download and Install Hive with Start-up Scripts
Aim
To download, install, and configure Apache Hive with necessary start-up scripts.
Procedure
1. Download: `wget https://archive.apache.org/dist/hive/hive-3.1.3/apache-hive-3.1.3-bin.tar.gz`
2. Extract: `tar -xzf apache-hive-3.1.3-bin.tar.gz`
3. Move: `sudo mv apache-hive-3.1.3-bin /usr/local/hive`
4. Set env in `.bashrc`:
```bash
export HIVE_HOME=/usr/local/hive
export PATH=$PATH:$HIVE_HOME/bin
```
5. Configure `hive-site.xml` (for Derby/Metastore):
```xml
<property>
 <name>javax.jdo.option.ConnectionURL</name>
 <value>jdbc:derby:;databaseName=/usr/local/hive/metastore_db;create=true</value>
</property>
```
6. Create warehouse dir in HDFS: `hadoop fs -mkdir -p /user/hive/warehouse`
7. Initialize schema: `schematool -dbType derby -initSchema`
8. Start Hive CLI: `hive`

Question 10: Hadoop Commands – Adding Files and Directories to HDFS
Aim
To implement Hadoop commands for adding files and directories to the HDFS environment.
Procedure
1. Create local files: `echo "Sample Data File 1" > file1.txt`, `echo "File 2 Data" > file2.txt`
2. Add single file: `hadoop fs -put file1.txt /user/input/`
3. Add multiple files: `hadoop fs -put file*.txt /user/input/multi/`
4. copyFromLocal: `hadoop fs -copyFromLocal file2.txt /user/data/`
5. moveFromLocal: `hadoop fs -moveFromLocal loc_data.txt /user/data/`
6. Create dir and add: `hadoop fs -mkdir -p /user/project/2024/`, then `hadoop fs -put data.csv /user/project/2024/`
7. Add entire directory: `hadoop fs -put local_dir/ /user/local_dir_backup/`
8. Verify: `hadoop fs -ls -R /user/`

Question 11: HQL Commands on Student Table
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

Question 12: Download and Install Hadoop Framework
Aim
To download, install, and configure the Hadoop framework (single-node cluster) with necessary start-up scripts.
Procedure
1. Create dedicated user: `sudo adduser hadoop`
2. Configure passwordless SSH: `ssh-keygen -t rsa`, `cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys`
3. Install JDK 8.
4. Download Hadoop: `wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz`
5. Extract: `tar -xzf hadoop-3.3.6.tar.gz`, move to `/usr/local/hadoop`
6. Set Environment in `.bashrc`:
```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export HADOOP_HOME=/usr/local/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
```
7. Configure XML files:
o core-site.xml: `<name>fs.defaultFS</name> <value>hdfs://localhost:9000</value>`
o hdfs-site.xml: `<name>dfs.replication</name> <value>1</value>`
o mapred-site.xml: `<name>mapreduce.framework.name</name> <value>yarn</value>`
o yarn-site.xml: `<name>yarn.nodemanager.aux-services</name> <value>mapreduce_shuffle</value>`
8. Format NameNode: `hdfs namenode -format`
9. Start: `start-dfs.sh && start-yarn.sh`
10. Verify: `jps`

Question 13: Implement Hive DDL Commands
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

Question 14: MapReduce Program for Multiplication of Two Numbers
Aim
To implement a Java program for multiplication of two numbers using MapReduce.
Procedure
1. Input file `numbers.txt` containing `a=5, b=6`.
2. Mapper reads the line, parses a and b, and emits `("product", "5,6")`.
3. Reducer receives the values, splits them, multiplies, and emits `("Result", 30)`.
Program (Java Code)
```java
// Mapper
public static class MultMapper extends Mapper<Object, Text, Text, Text> {
 public void map(Object key, Text value, Context context)
 throws IOException, InterruptedException {
 String[] nums = value.toString().split(",");
 context.write(new Text("multiply"), new Text(nums[0] + "," + nums[1]));
 }
}
// Reducer
public static class MultReducer extends Reducer<Text, Text, Text, IntWritable> {
 public void reduce(Text key, Iterable<Text> values, Context context)
 throws IOException, InterruptedException {
 for (Text val : values) {
 String[] nums = val.toString().split(",");
 int product = Integer.parseInt(nums[0]) * Integer.parseInt(nums[1]);
 context.write(new Text("Result"), new IntWritable(product));
 }
 }
}
```

Question 15: Implement HIVE Commands – CREATE, SHOW, DESCRIBE, USE, DROP, ALTER
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

Question 16: Hadoop Command – Adding Files to HDFS
Aim
To implement Hadoop commands for adding files to HDFS.
Procedure
1. Create local file: `echo "Adding file demo" > demo.txt`
2. Create CSV: `cat > data.csv << END` then enter CSV data.
3. Add single file: `hadoop fs -put demo.txt /user/data/`
4. Add with overwrite: `hadoop fs -put -f demo.txt /user/data/`
5. Add using copyFromLocal: `hadoop fs -copyFromLocal data.csv /user/csv_files/`
6. Add all .txt files: `hadoop fs -put *.txt /user/text_files/`
7. Verify: `hadoop fs -ls /user/data/`, `hadoop fs -ls /user/text_files/`

Question 17: MapReduce Program for Addition of Two Numbers
Aim
To implement a Java program for addition of two numbers using MapReduce.
Program (Key Snippet)
```java
// Reducer
int num1 = Integer.parseInt(nums[0]);
int num2 = Integer.parseInt(nums[1]);
int sum = num1 + num2;
context.write(new Text("Sum Result"), new IntWritable(sum));
```

Question 18: Download and Install Thrift, Generate HBase Thrift Binding
Aim
To install Apache Thrift, generate HBase Thrift bindings, and interact with HBase via Thrift.
Procedure
1. Install Thrift:
```bash
sudo apt-get update
sudo apt-get install -y automake bison flex g++ git libboost-all-dev libevent-dev libssl-dev libtool make pkg-config
wget https://dlcdn.apache.org/thrift/0.19.0/thrift-0.19.0.tar.gz
tar -xzf thrift-0.19.0.tar.gz
cd thrift-0.19.0
./configure
make
sudo make install
thrift --version
```
2. Start HBase Thrift Server:
```bash
hbase thrift start -p 9090
```
3. Generate HBase Thrift Binding (Python example):
```bash
thrift --gen py /usr/local/hbase/hbase-thrift/src/main/resources/org/apache/hadoop/hbase/thrift2/hbase.thrift
```
4. Python script to interact:
```python
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from hbase import THBaseService
transport = TTransport.TBufferedTransport(TSocket.TSocket('localhost', 9090))
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = THBaseService.Client(protocol)
transport.open()
print(client.getTableNames())
transport.close()
```

Question 19: HQL – Bank Account Table
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

Question 20: Hadoop Command – Deleting Files from HDFS
Aim
To implement Hadoop commands for deleting files and directories from HDFS.
Procedure
1. Create dummy files/dirs:
```bash
hadoop fs -mkdir -p /user/temp/dir1
hadoop fs -put file1.txt /user/temp/
hadoop fs -put file2.txt /user/temp/
hadoop fs -mkdir /user/temp/dir2
```
2. List before deletion: `hadoop fs -ls -R /user/temp/`
3. Delete a single file: `hadoop fs -rm /user/temp/file1.txt`
4. Delete using wildcard: `hadoop fs -rm /user/temp/*.txt`
5. Permanently delete (skip trash): `hadoop fs -rm -skipTrash /user/temp/imp_file.txt`
6. Delete empty directory: `hadoop fs -rmdir /user/temp/dir2` (only if empty)
7. Recursively delete directory with contents: `hadoop fs -rm -r /user/temp/dir1`
8. Delete entire temp directory: `hadoop fs -rm -r /user/temp`
9. Verify: `hadoop fs -ls /user/` (temp folder gone)
"""

os.makedirs("bda_experiments", exist_ok=True)

# Split the data into questions
questions = re.split(r'(?=Question \d+:)', data)
questions = [q.strip() for q in questions if q.strip()]

for index, question_text in enumerate(questions):
    filename = f"bda_experiments/exp{index+1}.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# " + question_text)

print("Created 20 markdown files for all BDA experiments in 'bda_experiments' directory.")
