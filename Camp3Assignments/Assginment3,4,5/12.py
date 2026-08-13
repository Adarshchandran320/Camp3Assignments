class PersonalInfo:
    def personal_details(self, name, age):
        self.name = name
        self.age = age


class JobInfo:
    def job_details(self, emp_id, department):
        self.emp_id = emp_id
        self.department = department


class Employee(PersonalInfo, JobInfo):
    def display(self):
        print("Employee Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Department:", self.department)


emp = Employee()
emp.personal_details("Rahul", 30)
emp.job_details("EMP101", "IT")
emp.display()