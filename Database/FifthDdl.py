import pymysql

conn = pymysql.connect(host="localhost",user="root",password="",database="my_db")
cur = conn.cursor()

# qry="create table items(id int(4) primary key , itemnm varchar(20),price int(10))"

# qry ="alter table items add remark varchar(20)"

# qry ="alter table items drop column remark "

# qry ="rename table items to product"

qry="drop table product"


cur.execute(qry)

conn.close();

print("Donee...")