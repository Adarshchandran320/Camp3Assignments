# Assignment 5: Library Book
# Create a class named LibraryBook.
# Methods
# • issue_book(quantity)
# • return_book(quantity)
# • display()
# Rules
# • Issue only if copies are available.
# • Return cannot exceed issued copies.
# Assign manually
# • book_title
# • author
# • total_copies
# • issued_copies 
class LibraryBook:
    def __init__(self,book_title,author,total_copies,issued_copies):
        self.book_title=book_title
        self.author=author
        self.total_copies=total_copies
        self.issued_copies=issued_copies
    def issue_book(self,quantity):
        available = self.total_copies - self.issued_copies
        if quantity <=0:
            print("quantity must be greater than 0")
        elif quantity <= available:
            self.issued_copies += quantity
            print(f"Successfully issued {quantity} copy/copies.")
        else:
            print("Cannot issue!")


    def return_book(self, quantity):
        if quantity <= 0:
            print("Quantity must be greater than 0.")
        elif quantity <= self.issued_copies:
            self.issued_copies -= quantity
            print(f"Successfully returned {quantity} copy/copies.")
        else:
            print(f"Cannot return more copies than currently issued ({self.issued_copies}).")

    def display(self):
        available = self.total_copies - self.issued_copies
        print(f"--- Library Book Details ---")
        print(f"Title: {self.book_title}")
        print(f"Author: {self.author}")
        print(f"Total Copies: {self.total_copies}")
        print(f"Issued Copies: {self.issued_copies}")
        print(f"Available Copies: {available}\n")

objLibraryBook=LibraryBook("Fire and Ice","George R.R Martin",40,12)
objLibraryBook.display()


