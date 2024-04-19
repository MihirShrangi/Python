from time import sleep
from threading import Thread
class Emp(Thread):

    def __init__(self,ename,sal) :
        super().__init__();
        self.ename=ename
        self.sal=sal

    def salProcess(self):
        print("The sal of employee :",self.ename, " is :", self.sal);
        print("The HRA of employee :",self.ename, " is :", self.sal*20);
        print("The DA of employee : ",self.ename, " is :", self.sal*32);
        if(self.ename=='abhi'):
            sleep(5)
        print("The PF of employee :",self.ename, "is :", self.sal*12);
        print("**************************",self.ename,"***********************************")


    def run(self):
        self.salProcess()


e1=Emp("vipin",20000)
e2=Emp("abhi",28000)
e3=Emp("lucky",30000)


print("-------------------Welcome to TLC---------------------------");

e1.start()
e2.start()
e3.start()

e2.join();

print("-------------------Bye Bye to TLC---------------------------");


