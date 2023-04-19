"""
Write a program that simulates a library, where users can borrow and return books. Your program should have three classes: Library, Book, and User.

The Book class should have the following attributes: title, author, and ISBN. It should also have methods for checking whether it's available (i.e., whether it has been borrowed by a user) and for borrowing and returning the book.

The User class should have the following attributes: name, email, and a list of borrowed books. It should also have methods for borrowing and returning books.

The Library class should have a list of books and a list of users. It should have methods for adding books and users, for displaying the list of books and users, and for borrowing and returning books.

The program should allow users to interact with the library by borrowing and returning books. When a book is borrowed, the user should be added to the book's list of borrowers and the book should be removed from the library's list of available books. When a book is returned, the user should be removed from the book's list of borrowers and the book should be added back to the library's list of available books.

You should use OOP concepts such as inheritance, encapsulation, and polymorphism to implement this program. Additionally, you should make use of the datetime module to keep track of when books are borrowed and returned. Finally, you should include error handling to ensure that users can only borrow books that are available and that they have not already borrowed, and that books can only be returned if they were borrowed in the first place.

"""
from datetime import datetime
    
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.borrowers = {}
    
    def is_available(self):
        if self.available:
            return True
        return False

    def borrow_book(self, user):
        if self.available:
            self.available = False
            self.borrowers[user] = datetime.now()
            print(f"{self.title} has been borrowed by {user.name}.")
        else:
            print(f"{self.title} is not available for borrowing.")
    
    def return_book(self, user):
        if user in self.borrowers:
            self.available = True
            borrow_date = self.borrowers.pop(user)
            return_date = datetime.now()
            days_borrowed = (return_date - borrow_date).days
            print(f"{self.title} has been returned by {user.name}.")
            print(f"{user.name} borrowed this book for {days_borrowed} days.")
        else:
            print(f"{user.name} did not borrow {self.title}.")

            

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.borrowed = []

    def test():


def main():
    if x > 1:
