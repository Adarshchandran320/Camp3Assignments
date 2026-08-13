class Vehicle:
    def start(self):
        print("Vehicle is started.")
class Car(Vehicle):
    def drive(self):
        print("Car is driving.")

mycar=Car()
mycar.start()
mycar.drive()
