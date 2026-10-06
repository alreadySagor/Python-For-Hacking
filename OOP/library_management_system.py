class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display(self):
        print(f"{self.title} by {self.author}")

class Library:
    def __init__(self):
        self.books = [] # list data type
    def addbook(self, book):
        self.books.append(book)
        print(f"book '{book.title}' added to the library.")
    def showbook(self):
        if self.books:
            print("Books in the library")
            for book in self.books:
                book.display()
        else:
            print("The library is empty!!!")

book1 = Book("The red ship", "max")
book2 = Book("Doomsday", "Dr. Doom")

library = Library()
library.addbook(book1)
library.addbook(book2)
library.showbook()