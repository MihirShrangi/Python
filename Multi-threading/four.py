from threading import Thread,Lock
from time import sleep

l1=Lock()

class Mycode(Thread):
    def __init__(self,n):
        super().__init__();
        self.n=n;
    def data(self):
        l1.acquire()
        for i in range(1,11):
            print(self.n*i);
            sleep(1)
        print()
        l1.release()
    def run(self):
        self.data()

m1=Mycode(5)
m2=Mycode(9)

m1.start()
m2.start()