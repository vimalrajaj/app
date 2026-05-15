# Question 16: Hadoop Command – Adding Files to HDFS
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