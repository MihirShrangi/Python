# 1) Required or positonal Arguments

def ops(a,b,c):
    s=a+(b*c)
    print("answer:",s)

# ops(11,22,33)
# ops(22,33,11)
# ops(33,22,11)

# 2) Keyword Arguments

def gg(i,j,k):
    ans=i+(j*k)
    print("Answer:",ans)

# gg(i=22,j=11,k=33)

# 3) Default Arguments

def add(a=1,b=2,c=3,d=4,e=5):
    sum=a+b+c+d+e;
    print(sum)

# add(11,22,33,44,55)
# add(11,22,33,44)
# add(11,22,33)
# add(11,22)
# add()

# 4) Varible Length Argument 

def sum(*n):
    s=0
    for i in n:
        s=s+i
    # print("The Sum is ",s)

# sum(11,22,3,123,12,123,123,123)

# 5) Lambda Argument
 

add= lambda a,b : print("sum is ",a+b)

add(20,30)

