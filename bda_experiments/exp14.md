# Question 14: MapReduce Program for Multiplication of Two Numbers
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