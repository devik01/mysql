'''import pythonmysql

def mysqlconnect():

    # To connect MySQL database 
    conn = pythonmysql.connect( 
        host='localhost', 
        user='root',  
        password = "root123", 
        db='employee', 
        ) 
    cur = conn.cursor() 
     # Select query 
    cur.execute("INSERT INTO employee(emp_id,emp_name,emp_salary) VALUES(100,'Devi Krishna',21000),(101,'Diya Krishna',22000);") 
    output = cur.fetchall() 
    for i in output:
        print(i)
    # To close the connection 
    conn.close()
# Driver Code 
if __name__ == "__main__" : 
    mysqlconnect()'''

import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='root123',db='employee')
cur=conn.cursor()
cur.execute("use employee")
cur.execute("insert into employee values(100,'Devi Krishna',12000);")
cur.execute("select * from employee")
emp=cur.fetchall()

for i in emp:
    print(i)

conn.commit()
cur.close()
conn.close()




