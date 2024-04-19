import csv;
f1=open("D:\\doc.csv","w",newline='')
cw=csv.writer(f1)
cw.writerow(["Roll","Name","Class"])
cw.writerow([111,"prabal",12])
cw.writerow([112,"Lucky",11])
cw.writerow([113,"Rahul",12])
f1.close()

print("Done....")