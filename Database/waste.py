# n=int(input("Enter"))
# a=0
# b=1
# print(a, " " , b,end=" ")
# i=1
# while(i<=n):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c
#     i+=1

# n=int(input("Enter :"))
# a=0
# b=1
# print(a," ",b,end=" ")
# i=1
# while(i<=n):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c
#     i+=1

# n = int(input("Enter any number :"))
# sum=0
# i=0
# while(n>0):
#     rwd=n%10;
#     sum=sum+rwd
#     n=n//10

# print(sum)

n = int(input("Enter any number :"))
old=n
rev=0
i=0
while(n>0):
    rwd=n%10;
    rev=(rev*10)+rwd
    n=n//10
print(rev)

if(old==rev):
    print("Its a Pallandrom")
else:
    print("not a")