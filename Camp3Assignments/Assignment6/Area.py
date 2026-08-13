from abc import ABC,abstractmethod
import math
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi * (self.radius**2)

obj1=Rectangle(5,6)
print(f"Rectangle Area:{obj1.area()}")
obj1=Circle(6)
print(f"Circle Area:{obj1.area()}")