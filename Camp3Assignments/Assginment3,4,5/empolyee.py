class Employee:

    def __init__(self, employee_id, employee_name):
        self.employee_id = employee_id
        self.employee_name = employee_name


class Manager(Employee):

    def __init__(self, employee_id, employee_name, department):
        super().__init__(employee_id, employee_name)
        self.department = department

    def display(self):
        print("\nEmployee and Manager Details:")
        print(f"Employee ID: {self.employee_id}")
        print(f"Employee Name: {self.employee_name}")
        print(f"Department: {self.department}")
        
obj1 = Manager(1, "Adarsh", "HR")
obj1.display()