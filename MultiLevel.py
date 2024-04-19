class Tire:
    def stop(self):
        print("You break the car")
    def Speed(self):
        print("You just unbreak the car")
class Light(Tire):
    def buld(self):
        print("Light is On")

class Car(Light):
    def Run(self):
        print("The car is running...")

C1=Car()

C1.stop()
C1.Speed()
C1.buld()
C1.Run()