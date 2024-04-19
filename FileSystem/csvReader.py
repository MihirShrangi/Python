import csv;
f1=open("D:\\doc.csv","r")
cw=csv.reader(f1)
# for i in cw:
#     print(i)

for i in cw:
    print(i[0],"\t",i[1],"\t",i[2])

f1.close()