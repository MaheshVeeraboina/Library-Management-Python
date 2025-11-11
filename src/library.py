from src.book import Book
from src.borrower import Borrower

class Library:
    def __init__(self):
        self.books = {}
        self.borrowers = {}
        self.borrowed = {}

    def add_book(self):
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        isbn = input("Enter ISBN: ")
        genre = input("Enter Genre: ")
        quantity = int(input("Enter Quantity: "))

        book = Book(title, author, isbn, genre, quantity)
        self.books[isbn] = book
        self.borrowed[isbn] = 0
        print("✅ Book Added Successfully.\n")

    def update_book(self):
        isbn = input("Enter ISBN to Update: ")
        if isbn in self.books:
            title = input("New Title (leave blank to skip): ")
            author = input("New Author (leave blank to skip): ")
            quantity = input("New Quantity (leave blank to skip): ")

            if title: self.books[isbn].title = title
            if author: self.books[isbn].author = author
            if quantity: self.books[isbn].quantity = int(quantity)
            print("✅ Book Updated Successfully.\n")
        else:
            print("❌ Book Not Found.\n")

    def remove_book(self):
        isbn = input("Enter ISBN to Remove: ")
        if isbn in self.books:
            del self.books[isbn]
            del self.borrowed[isbn]
            print("✅ Book Removed Successfully.\n")
        else:
            print("❌ Book Not Found.\n")

    def add_borrower(self):
        membership_id = input("Enter Membership ID: ")
        name = input("Enter Name: ")
        contact = input("Enter Contact: ")

        borrower = Borrower(membership_id, name, contact)
        self.borrowers[membership_id] = borrower
        print("✅ Borrower Added Successfully.\n")

    def update_borrower(self):
        membership_id = input("Enter Membership ID to Update: ")
        if membership_id in self.borrowers:
            name = input("New Name (leave blank to skip): ")
            contact = input("New Contact (leave blank to skip): ")

            if name: self.borrowers[membership_id].name = name
            if contact: self.borrowers[membership_id].contact = contact
            print("✅ Borrower Updated Successfully.\n")
        else:
            print("❌ Borrower Not Found.\n")

    def remove_borrower(self):
        membership_id = input("Enter Membership ID to Remove: ")
        if membership_id in self.borrowers:
            del self.borrowers[membership_id]
            print("✅ Borrower Removed Successfully.\n")
        else:
            print("❌ Borrower Not Found.\n")

    def borrow_book(self):
        membership_id = input("Enter Membership ID: ")
        isbn = input("Enter ISBN: ")

        if membership_id in self.borrowers and isbn in self.books:
            if self.borrowed[isbn] < self.books[isbn].quantity:
                self.borrowed[isbn] += 1
                print("✅ Book Borrowed Successfully.\n")
            else:
                print("❌ No Copies Available.\n")
        else:
            print("❌ Invalid Membership ID or ISBN.\n")

    def return_book(self):
        membership_id = input("Enter Membership ID: ")
        isbn = input("Enter ISBN: ")

        if membership_id in self.borrowers and isbn in self.books:
            if self.borrowed[isbn] > 0:
                self.borrowed[isbn] -= 1
                print("✅ Book Returned Successfully.\n")
            else:
                print("❌ This Book Was Not Borrowed.\n")
        else:
            print("❌ Invalid Membership ID or ISBN.\n")

    def search_books(self):
        keyword = input("Enter Title/Author/Genre to Search: ").lower()
        print("\n🔍 Search Results:")
        for book in self.books.values():
            if (keyword in book.title.lower() or
                keyword in book.author.lower() or
                keyword in book.genre.lower()):
                available = book.quantity - self.borrowed[book.isbn]
                print(f"{book.title} | {book.author} | {book.genre} | Available: {available}")
        print()
