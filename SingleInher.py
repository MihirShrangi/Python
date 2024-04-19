class Mobile:
    def call(self):
        print("U can call..")
class Android(Mobile):
    def internet(self):
        print("Use Internet...")

a1=Android()

a1.call()
a1.internet()