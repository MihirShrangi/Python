#) Static Memory allocation

class student:
    faculty="alpha"
    def set(self,r,nm,age):
        self.roll=r
        self.name=nm
        self.age=age
        
    def show(self):
        print("-------------------------------------")
        print("The Roll number is:",self.roll)
        print("The Student Name is:",self.name)
        print("The age is:",self.age)
        print("The Faculty Name is:",student.faculty) #) static varible alway refer to their class 
        print("-------------------------------------")

    def welcome():
        print("Welcome Everyone...")

s1=student()
s2=student()
s3=student()


student.welcome()

s1.set(111,"mihir",22)
s2.set(112,"lucky",21)
s3.set(113,"lucy",20)


s1.show()
s2.show()
s3.show()

