# Question 9: Download and Install Hive with Start-up Scripts
Aim
To download, install, and configure Apache Hive with necessary start-up scripts.
Procedure
1. Download: `wget https://archive.apache.org/dist/hive/hive-3.1.3/apache-hive-3.1.3-bin.tar.gz`
2. Extract: `tar -xzf apache-hive-3.1.3-bin.tar.gz`
3. Move: `sudo mv apache-hive-3.1.3-bin /usr/local/hive`
4. Set env in `.bashrc`:
```bash
export HIVE_HOME=/usr/local/hive
export PATH=$PATH:$HIVE_HOME/bin
```
5. Configure `hive-site.xml` (for Derby/Metastore):
```xml
<property>
 <name>javax.jdo.option.ConnectionURL</name>
 <value>jdbc:derby:;databaseName=/usr/local/hive/metastore_db;create=true</value>
</property>
```
6. Create warehouse dir in HDFS: `hadoop fs -mkdir -p /user/hive/warehouse`
7. Initialize schema: `schematool -dbType derby -initSchema`
8. Start Hive CLI: `hive`