def Welcome():
    print("Hello Everyone....")


def sum(a,b):
    
    print(a+b)

# sum("hello","heheh")

def sqr(a):
    s=a*a
    return s

# p=sqr(25)
# print(p)
# print(sqr(45))

# a=int(input("Enter Any Number:-"))

def sqr(j):
    for i in range(1,11):
        print(j*i,end=" ")
    print("")    
    

# for a in range(11,26):
    # sqr(a)

def operation(x,y):
    if(x==1):
        return y*y;
    elif(x==2):
        return y*y*y;
    elif(x==3):
        c=1
        for i in range(1,y+1):
            c=c*i
        return c;
    else:
        return y;

y=int(input("Enter Any Number:-"))

x=int(input("Operation to be performed (1,2,3) for (square , cube and factorial):-"))

ans=operation(x,y)

print("The answer is:",ans)
    
