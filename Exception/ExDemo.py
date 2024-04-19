from MyExcept import LessAgeException,MoreAgeException;

try:
    a=int(input("Enter Your Age :"))
    if(a<18):
        raise LessAgeException
    
    if(a>50):
        raise MoreAgeException
    print("You are a Valid Person.")

except LessAgeException:
    print("Your Age is Below the Limit.")

except MoreAgeException:
    print("Your Age is above the limit.")