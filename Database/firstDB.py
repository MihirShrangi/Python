#import the relevant package
import pymysql

#establish the connection
conn=pymysql.connect(host="localhost",user="root",password="",database="my_db")
#creating a cursor object
cur=conn.cursor()
#prepare the query
qry="select * from emp";
# dispatch the query to the database engine..
cur.execute(qry);
#fetch the data
data=cur.fetchone();
#Close the connection
conn.close();

print(data)