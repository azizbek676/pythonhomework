class BookNotFoundException(Exception):
    """Exception raised when a book is not found in the library."""
    pass

class BookAlreadyBorrowedException(Exception):
    """Exception raised when trying to borrow a book that is already borrowed."""
    pass

class MemberLimitExceededException(Exception):
    """Exception raised when a member exceeds the limit of borrowed books."""
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.title}' by {self.author}"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} has already borrowed 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{book.title}' is already borrowed.")
        self.borrowed_books.append(book)
        book.is_borrowed = True
        print(f"{self.name} successfully borrowed '{book.title}'.")

    def return_book(self, book):
        if book not in self.borrowed_books:
            raise BookNotFoundException(f"{self.name} hasn't borrowed '{book.title}'.")
        self.borrowed_books.remove(book)
        book.is_borrowed = False
        print(f"{self.name} successfully returned '{book.title}'.")

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added to the library.")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book '{title}' not found in the library.")

    def borrow_book(self, member, title):
        try:
            book = self.find_book(title)
            member.borrow_book(book)
        except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
            print(e)

    def return_book(self, member, title):
        try:
            book = self.find_book(title)
            member.return_book(book)
        except (BookNotFoundException) as e:
            print(e)
library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")
book4 = Book("Moby Dick", "Herman Melville")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
member1 = Member("Alice")
member2 = Member("Bob")
library.add_member(member1)
library.add_member(member2)
library.borrow_book(member1, "The Great Gatsby")
library.borrow_book(member1, "1984")
library.borrow_book(member1, "To Kill a Mockingbird")
library.borrow_book(member1, "Moby Dick")
library.return_book(member1, "The Great Gatsby")
library.borrow_book(member1, "Moby Dick")
library.return_book(member2, "1984")
library.borrow_book(member2, "1984")
