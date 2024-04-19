a = 20 
b = 10 
c = 0
try:
    c = a + 'b'
except TypeError:
    print("invalid varible////")

except NameError:
    print("invalid name...")


print("the answer is ", c)
print("code is running'''")