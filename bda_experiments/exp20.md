# Question 20: Hadoop Command – Deleting Files from HDFS
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