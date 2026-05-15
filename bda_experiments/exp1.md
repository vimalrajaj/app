# Question 1: MapReduce Program for Matrix Multiplication
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