class point:
    def __init__(self,x,y):
        self.x=x;
        self.y=y;
    def __str__(self):
        return "Your Point is :"+str(self.x)+" and "+str(self.y)
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        p=point(x,y)
        return p
    def __mul__(self,other):
        x=self.x*other.x
        y=self.y*other.x
        p=point(x,y)
        return p


o1=point(20,30)
o2=point(30,40) 

print(o1)
print(o2)
o3=o1+o2
print(o3)
o4=o1*o2
print(o4)
