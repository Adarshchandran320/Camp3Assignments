from abc import ABC,abstractmethod
class Vechile(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class Car(Vechile):
    def start_engine(self):
        print("Car engine started")
class Bike(Vechile):
    def start_engine(self):
        print("Bike engine started")

my_car = Car()
my_bike = Bike()


my_car.start_engine()   
my_bike.start_engine()      
    