class Member:
    def __init__(self,members_id,members_name):
        self.members_id=members_id
        self.members_name=members_name

    def display(self):
        print("\nMembers details")
        print(f"Members Id:{self.members_id}")
        print(f"Members Name:{self.members_name}")

class LibraryMember(Member):
    def __init__(self,members_id,members_name,books_issued):
        super().__init__(members_id,members_name)
        self.books_issued=books_issued
    def book(self):
        print("Library Details")
        print(f"Members Id:{self.members_id}")
        print(f"Members Name:{self.members_name}")
        print(f"Books Issued:{self.books_issued}")

obj1=LibraryMember(1,"adarsh",12)
obj1.book()
obj1.display()

