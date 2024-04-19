class person:
    def __init__(self,nm,age):
        self.name=nm
        self.age=age

    def __str__(self):
        return ("Person name is : ")+ self.name + (", And the age is : ")+ str(self.age)
    
class emp(person):
    def __init__(self,nm,age,sal):
        super().__init__(nm,age)
        self.salary=sal

    def __str__(self):
        s=super().__str__()
        p=("\n and the salary is : ")+str(self.salary)
        return s+p
    

e1=emp("Mihir",20,2200000)
print(e1)

