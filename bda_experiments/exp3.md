# Question 3: Hadoop Commands for File Management in HDFS
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