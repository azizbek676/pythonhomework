MAX_BORROW_LIMIT = 3
class BookNotFoundException(Exception): pass
class BookAlreadyBorrowedException(Exception): pass
class MemberLimitExceededException(Exception): pass
class Book:
    def __init__(self, title, author):
        self.title, self.author, self.is_borrowed = title, author, False
class Member:
    def __init__(self, name):
        self.name, self.borrowed_books = name, []
    
    def borrow_book(self, book):
        if len(self.borrowed_books) >= MAX_BORROW_LIMIT:
            raise MemberLimitExceededException("Limit reached.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException("Already borrowed.")
        book.is_borrowed = True
        self.borrowed_books.append(book)
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
class Library:
    def __init__(self):
        self.books, self.members = {}, {}
    
    def add_book(self, book): self.books[book.title] = book
    def add_member(self, member): self.members[member.name] = member
    
    def borrow_book(self, member_name, book_title):
        if member_name not in self.members or book_title not in self.books:
            print("Member or book not found."); return
        try:
            self.members[member_name].borrow_book(self.books[book_title])
        except (BookAlreadyBorrowedException, MemberLimitExceededException) as e:
            print(e)
    
    def return_book(self, member_name, book_title):
        if member_name in self.members and book_title in self.books:
            self.members[member_name].return_book(self.books[book_title])
        else:
            print("Invalid return.")
library = Library()
[library.add_book(Book(t, a)) for t, a in [("Python 101", "John Doe"), ("Data Science", "Jane Smith")]]
[library.add_member(Member(n)) for n in ["Alice", "Bob"]]

library.borrow_book("Alice", "Python 101")
library.borrow_book("Alice", "Data Science")
library.borrow_book("Alice", "Machine Learning") 
library.borrow_book("Alice", "Python 101")
library.return_book("Alice", "Python 101")
library.borrow_book("Bob", "Python 101")

