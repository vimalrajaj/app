# Question 5: Download and Install HBase with Start-up Scripts
Aim
To download, install, and configure Apache HBase with necessary start-up scripts.
Procedure
1. Download HBase: `wget https://archive.apache.org/dist/hbase/2.5.5/hbase-2.5.5-bin.tar.gz`
2. Extract: `tar -xzf hbase-2.5.5-bin.tar.gz`
3. Move: `sudo mv hbase-2.5.5 /usr/local/hbase`
4. Set JAVA_HOME in `hbase-env.sh`:
```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```
5. Configure `hbase-site.xml`:
```xml
<configuration>
 <property>
 <name>hbase.rootdir</name>
 <value>hdfs://localhost:9000/hbase</value>
 </property>
 <property>
 <name>hbase.zookeeper.property.dataDir</name>
 <value>/home/user/hbase-zookeeper</value>
 </property>
 <property>
 <name>hbase.cluster.distributed</name>
 <value>false</value>
 </property>
</configuration>
```
6. Set environment variables in `.bashrc`:
```bash
export HBASE_HOME=/usr/local/hbase
export PATH=$PATH:$HBASE_HOME/bin
```
7. Source: `source ~/.bashrc`
8. Start HBase: `start-hbase.sh`
9. Verify: `jps` (should show HMaster)
10. Access HBase Shell: `hbase shell`