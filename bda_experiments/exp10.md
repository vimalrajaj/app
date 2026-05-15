# Question 10: Hadoop Commands – Adding Files and Directories to HDFS
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