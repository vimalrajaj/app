# Question 7: MapReduce Program for Character Count
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