# class test:
#     a=10
#     def welcome(self):
#         print("Welcome everyone")

# t1=test()

# # print(t1.a)
# # t1.welcome()

class math:
    def set(self,p,q):
        self.a=p
        self.b=q
    def sum(self):
        print("The sum is :",self.a+self.b)
    def product(self):
        print("The product is :",self.a*self.b)
    def div(self):
        print("The divison is :",self.a/self.b)
m1=math()
m1.set(20,30)
m1.sum()
m1.product()
m1.div()