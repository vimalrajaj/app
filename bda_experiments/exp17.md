# Question 17: MapReduce Program for Addition of Two Numbers
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