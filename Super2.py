class X:
    def __init__(self):
        print("X is Running...")

class Y(X):
    def __init__(self):
        super().__init__()
        print("Y is Running....")

class Z(Y):
    def __init__(self):
        print("Z is Running...")
        super().__init__()

z1=Z()

print(z1)