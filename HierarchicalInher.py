class Mobile:
    def call(self):
        print("You can call...")

class Android(Mobile):
    def Playstore(self):
        print("You can download app for android..")

class Iphone(Mobile):
    def Appstore(self):
        print("You can Download app for Apple..")


I1=Iphone()

I1.call()
I1.Appstore()

A1=Android()
A1.Playstore()
A1.call()

M1=Mobile()
M1.call()