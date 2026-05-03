class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
    def search_books(self, query):
        return [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]
library = Library()
book1 = Book("The Invisible Man", "H.G.Wells", "1897")
book2 = Book("Doomquest", "David Michelinie", "149150")
library.add_book(book1)
library.add_book(book2)
for book in library.search_books("Doomquest"):
    print(book.title, book.author)
library.remove_book("1897")