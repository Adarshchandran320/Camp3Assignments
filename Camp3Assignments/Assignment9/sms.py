from abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self,id):
        self.id=id
    @abstractmethod
    def get_role_details(self):
        pass
    def display(self):
        print(f"ID:{self.id}")

class Teacher(Person):
    def __init__(self, id,subject,department):
        super().__init__(id)
        self.subject=subject
        self.department=department
    def get_role_details(self):
        print(f"Subject:{self.subject}")
        print(f"Department:{self.department}")

pers=Teacher(1,"English","CSE")
pers.get_role_details()
pers.display()
