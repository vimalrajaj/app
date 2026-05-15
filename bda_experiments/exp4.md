# Question 4: MapReduce Program for Word Count
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