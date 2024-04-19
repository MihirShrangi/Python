import pymysql

conn=pymysql.connect(host="localhost",user="root",password="",database="my_db")

cur=conn.cursor();

id=int(input("Enter the Id number :- "))
rol=input("Enter the Job Roll :- ")
Salary=int(input("Enter the Salary :- "))

qry="update emp set sal=%d,job='%s' where empno=%d" % (Salary,rol,id);

n=cur.execute(qry);
print(n,"records updated");

conn.commit();
conn.close();