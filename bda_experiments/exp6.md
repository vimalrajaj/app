# Question 6: Implement HBase CRUD Commands
Aim
To implement HBase commands to create a table, insert data, retrieve data, and delete data.
Procedure
(I) Create Table:
```hbase
create 'customer', 'personal', 'contact'
```
(II) Insert Data:
```hbase
put 'customer', '001', 'personal:name', 'John Doe'
put 'customer', '001', 'personal:age', '30'
put 'customer', '001', 'contact:email', 'john@example.com'
put 'customer', '001', 'contact:phone', '1234567890'
put 'customer', '002', 'personal:name', 'Jane Smith'
put 'customer', '002', 'personal:age', '25'
put 'customer', '002', 'contact:email', 'jane@example.com'
```
(III) Get Data:
```hbase
get 'customer', '001'
get 'customer', '001', 'personal'
scan 'customer'
```
(IV) Delete Data:
```hbase
delete 'customer', '001', 'contact:phone' -- Delete single cell
deleteall 'customer', '002' -- Delete entire row
```