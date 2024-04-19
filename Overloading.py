class overloading:
    def __init__(self,panm="unknown",pid="0",pam="00") :
        self.proname=panm
        self.proid=pid
        self.proamount=pam

    def __str__(self):
        return "The Name of the Product is : "+self.proname+", The id of product is : "+str(self.proid)+", The Amount of Product is"+str(self.proamount)
    
o1=overloading("Iphone",11132,1413123)
o2=overloading("TV",pam=445823)
o3=overloading("Mobile")
o4=overloading(pid=1413123)
o5=overloading(pam=1413123)

print(o1)
print(o2)
print(o3)
print(o4)
print(o5)