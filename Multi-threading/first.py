from time import sleep;

from threading import Thread

def sqr(n):
    print("the square is %d 0f %d"% (n*n,n))
    sleep(5)
    print("Square is done...")

def cub(n):
        print("the cude is %d 0f %d"%(n*n*n,n))
        sleep(2)
        print("Cube is done...")


# sqr(5)
# cub(5)
        
t1=Thread(target=sqr,args=[25,])
t2=Thread(target=cub,args=[5,])


t1.start()
t2.start()