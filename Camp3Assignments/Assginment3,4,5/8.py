class Company:
    def __init__(self, company_name):
        self.company_name = company_name

    def display_company(self):
        print(f"Company Name : {self.company_name}")

class Employee(Company):
    def __init__(self, company_name, emp_id, emp_name):
        super().__init__(company_name)
        self.emp_id = emp_id
        self.emp_name = emp_name

    def display_employee(self):
        self.display_company()
        print(f"Employee ID   : {self.emp_id}")
        print(f"Employee Name : {self.emp_name}")

class Salary(Employee):
    def __init__(self, company_name, emp_id, emp_name, salary):
        super().__init__(company_name, emp_id, emp_name)
        self.salary = salary

    def display_salary(self):
        self.display_employee()
        print(f"Salary        : ₹{self.salary}")


obj = Salary("Infosys", 101, "Adarsh", 50000)

obj.display_salary()