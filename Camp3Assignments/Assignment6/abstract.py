from abc import ABC,abstractmethod

class login(ABC):

    @abstractmethod
    def login(self):
        pass

class admin(login):
    def login(self):
        print("admin login")


class user(login):
    def login(self):
        print("user login")



obj=admin()
obj1=user()

obj.login()
obj1.login()
