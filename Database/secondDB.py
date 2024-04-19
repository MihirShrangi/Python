import pymysql

conn=pymysql.connect(host="localhost",user="root",password="",database="my_db");

cor=conn.cursor();

qry="select * from emp";

cor.execute(qry);

rows=cor.fetchall();

print("EmpNo\tEmpname\tjob\tMgr\tSalary\tComission\tDeptNo")
print("-------------------------------------------------------------------------------------------------------------------------")

for row in rows:
    print(str(row[0])+"\t"+row[1]+"\t"+row[2]+"\t"+str(row[3])+"\t"+str(row[4])+"\t"+str(row[5])+"\t"+str(row[6])+"\t")

print("--------------------------------------------------------------------------------------------------------------------------")

conn.close();