class test:
    def __del__(self):
        print("bye")
    def __init__(self) :
        print("Hello...")

    def hello(self):
        print("Welcome Everyone...")

# t1=test()
# t1.hello()
# t2=test()
# t3=test()
# t3.hello()

class first:
    def __init__(self,enam,enum,esal):
        self.empName=enam
        self.empNumber=enum
        self.empsalary=esal
    def show(self):
        print("The Name is :",self.empName)
        print("The Number is :",self.empNumber)
        print("The Salary is :",self.empsalary)

    def __str__(self):
        return "The name is:  "+self.empName + ", The Number is : "+ str(self.empNumber) + ", The Salary is : "+ str(self.empsalary)
       
        

f1=first("mihir",10001,10000)

f2=first("lucy",12034,214345)

print(f1)
print(f2)