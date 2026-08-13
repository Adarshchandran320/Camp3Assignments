from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,basic_salary):
        self.basic_salary=basic_salary
    @abstractmethod
    def calculate_salary(self):
        pass
    def display_basic_salary(self):
        print(f"Basic Salary:{self.basic_salary}")

class FullTimeEmployee(Employee):

    def calculate_salary(self):
        hra=self.basic_salary*0.20
        da=self.basic_salary*0.10
        total_salary=self.basic_salary+hra+da
        print(f"Total Salary:{total_salary}")

emp1=FullTimeEmployee(300000)
emp1.calculate_salary()
emp1.display_basic_salary()

