

import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='root123',db='employee')
cur=conn.cursor()
cur.execute("use employee")
#create data (insert query)
cur.execute("insert into employeeinfo values(100,'Devi Krishna',12000),(101,'Diya Krishna',13000),(102,'Deepa Krishna',14000);")
#read data(select query)
cur.execute("select * from employeeinfo")
emp=cur.fetchall()
for i in emp:
    print(i)
conn.commit()
#update data(update query)
cur.execute("update employeeinfo set emp_name='Krishna Kumar' where emp_id=102;")
conn.commit()
#delete data (delete query)
cur.execute("delete from employeeinfo where emp_id=100;")
conn.commit()
cur.close()
conn.close()





