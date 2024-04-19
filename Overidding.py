class RBI:
    def IntDeo(self):
        print("Int Must be Payble as per the RBI norms is i.e 6%...")

class SBI(RBI):
    pass

class AXIS(RBI):
    def IntDeo(self):
        print("Int Must be Payble as per the Axis norms is i.e 4.8%...")

class HDFC(RBI):
    def Intdeo(self):
        print("Int Must be Payble as per the Hdfc norms is i.e 6.5%...")

sbi=SBI()
hdfc=HDFC()
axis=AXIS()

sbi.IntDeo()
hdfc.IntDeo()
axis.IntDeo()