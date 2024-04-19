f1=open("FileSystem//myFile.text","r+")
# data=f1.read()
print(f1.read())

print("\n Our positon is :",f1.tell())

print("\n New Content Will be...\n")

f1.write(" \n Additional Line has been added to the file.. \ n")
f1.seek(0)
print(f1.read())

print("\n Our positon is :",f1.tell())

f1.close()