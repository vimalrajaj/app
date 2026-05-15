# Question 18: Download and Install Thrift, Generate HBase Thrift Binding
Aim
To install Apache Thrift, generate HBase Thrift bindings, and interact with HBase via Thrift.
Procedure
1. Install Thrift:
```bash
sudo apt-get update
sudo apt-get install -y automake bison flex g++ git libboost-all-dev libevent-dev libssl-dev libtool make pkg-config
wget https://dlcdn.apache.org/thrift/0.19.0/thrift-0.19.0.tar.gz
tar -xzf thrift-0.19.0.tar.gz
cd thrift-0.19.0
./configure
make
sudo make install
thrift --version
```
2. Start HBase Thrift Server:
```bash
hbase thrift start -p 9090
```
3. Generate HBase Thrift Binding (Python example):
```bash
thrift --gen py /usr/local/hbase/hbase-thrift/src/main/resources/org/apache/hadoop/hbase/thrift2/hbase.thrift
```
4. Python script to interact:
```python
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from hbase import THBaseService
transport = TTransport.TBufferedTransport(TSocket.TSocket('localhost', 9090))
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = THBaseService.Client(protocol)
transport.open()
print(client.getTableNames())
transport.close()
```