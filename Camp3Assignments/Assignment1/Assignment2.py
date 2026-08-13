# Assignment 2: Employee Salary
# Create a class named Employee.
# Requirements
# Methods:
# • calculate_bonus()
# • total_salary()
# • display()
# Create an object and assign:
# • name
# • base_salary
# • years_of_service
# Bonus Formula:
# Bonus = base_salary × 5% × years_of_service

class Employee:
    def __init__(self, name, base_salary, years_of_service):
        self.name = name
        self.base_salary = base_salary
        self.years_of_service = years_of_service

    def calculate_bonus(self):
        bonus = self.base_salary * 0.05 * self.years_of_service
        return bonus

    def total_salary(self):
        return self.base_salary + self.calculate_bonus()

    def display(self):
        print(f"Employee: {self.name}")
        print(f"Base Salary: ${self.base_salary:.2f}")
        print(f"Years of Service: {self.years_of_service}")
        print(f"Bonus: ${self.calculate_bonus():.2f}")
        print(f"Total Salary: ${self.total_salary():.2f}")

objEmployee1=Employee("John Doe", 50000, 5)
objEmployee2=Employee("Johan",4000,6)
objEmployee1.display()
objEmployee2.display()