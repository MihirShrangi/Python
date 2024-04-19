li=[11,12,13,14,15,16,17,18,19,20]
print(li)
li.append(200)
li.append(300)
print(li)
# l2=[1,2,3,4,5]
# li.append(l2)
# print(li)

# li.extend(l2)
# print(li)

# li.insert(3,500)
# print(li)

# li.remove(13)
# print(li)

# li.pop()
# print(li)

# li.pop(3)
# print(li)

# li.clear()
# print(li)\

# print(li.count(11))
# print(li.index(200))
# li.sort()
# print(li)
# li.reverse()
# print(li)
# l3=li.copy()
# print(l3)

# print(max(li))
# print(min(li))

for p in li:
    for i in range(2,p):
        if(p%i==0):
            break;
    else:
         print("The prime numbers is:",p)