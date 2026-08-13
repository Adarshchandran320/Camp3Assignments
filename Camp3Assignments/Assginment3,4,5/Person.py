class Person:
    def __init__(self,name="",age=0):
        self.name=input("Enter the Person Name:")
        self.age=int(input("Enter the Person Age:"))

    def display(self):
        print("Person Details \n")
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
class Student(Person):
    def __init__(self, name="", age=0,rollno=0,marks=""):
        super().__init__(name,age)
        self.rollno=int(input("Enter the Roll no:"))
        self.marks=input("Enter the marks:")


    def display_student(self):
        super().display()
        print(f"Roll_no:{self.rollno}")
        print(f"Marks:{self.marks}")

obj1=Student()
obj1.display_student()
        