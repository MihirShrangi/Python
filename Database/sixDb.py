import pymysql

class MyDb:
    def __init__(self):
        self.con=pymysql.connect(host="localhost",user="root",password="",database="my_db");
        self.cur=self.con.cursor();
    
    def operator(self,qry):
        self.cur.execute(qry);
        self.conn.commit();
        print("Done...");
    
    def show(self,qry):
        self.cur.execute(qry);
        data=self.cur.fetchall();
        return data;
        
    def __del__(self) :
        self.con.close();