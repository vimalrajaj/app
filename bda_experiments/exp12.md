# Question 12: Download and Install Hadoop Framework
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