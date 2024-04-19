import pymysql

conn=pymysql.connect(host="localhost",user="root",password="",database="my_db")

cur=conn.cursor();

id=int(input("Enter the Id number :- "))
name=input("Enter the Name :- ")
rol=input("Enter the Job Roll :- ")
mrg=int(input("Enter the Job Code :- "))
Salary=int(input("Enter the Salary :- "))
ccom=int(input("Enter the Comission :- "))
dep=int(input("Enter the Dept Number :- "))

# qry="insert into emp values(%d,%s,%s,%d,%d,%d,%d)" % (id,name,rol,mrg,Salary,ccom,dep)
# qry="insert into emp values(5,'abhi','dev',2,20000,1000,10)"
qry="insert into emp values(%d,'%s','%s',%d,%d,%d,%d)" % (id,name,rol,mrg,Salary,ccom,dep);
n=cur.execute(qry);
print(n,"recorded")

conn.commit() # to save the data into database
conn.close()

