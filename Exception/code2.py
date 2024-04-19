c = 0


try:
    a = int(input("Enter first number..."));
    b = int(input("Enter second number..."));
    c =a/b;
except ZeroDivisionError:
    print("the demonator can't be xero10")
    b = int(input("re-Enter second number..."));
    try:
        c =a/b;
    except ZeroDivisionError:
        print("the demonator can't be xero10")
        b = int(input("re-Enter second number..."));
        c =a/b;

except ValueError:
    print("invalid Eorror")

except :
    print("Something is wrong")

else:
    print("All good")

finally:
    print("End Game")

print(c)

