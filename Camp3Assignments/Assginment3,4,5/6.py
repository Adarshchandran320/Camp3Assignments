class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("student details")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")

class student(person):
    def __init__(self, name, age,roll_no,marks):
        super().__init__(name, age)
        self.roll_no=roll_no
        self.marks=marks

    def display_student(self):
        self.display()
        print(f"roll no : {self.roll_no}")
        print(f"marks   : {self.marks}")

class result(student):
    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age, roll_no, marks)

    def display_result(self):
        super().display_student()

obj1=result("Adarsh",21,6,98)
obj1.display_result()