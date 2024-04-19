class Computer:
    def PowerPoint(self):
        print("You can make presentation....")

class Mobile:
    def Camera(self):
        print("Yon can Click Photo")

class smartphone(Computer,Mobile):
    def Internet(self):
        print("You can connect to the internet....")


s1=smartphone()
s1.Internet()
s1.Camera()
s1.PowerPoint()

m1=Mobile()
m1.Camera()

c1=Computer()
c1.PowerPoint()