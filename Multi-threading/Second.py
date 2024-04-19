from threading import   Thread

class Mycls(Thread):
    def __init__(self,n):
        super().__init__();
        self.n=n;
    def run(self):
        print("The thread is running ",self.n)


m1=Mycls(22);
m2=Mycls(55);

m1.start();
m2.start();