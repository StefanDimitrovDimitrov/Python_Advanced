'''

    Design principle by which we protect our code by making it independent of things that are fragile, volatile or out of our control
    чрез него премахваме зависимости от други класове

    - Dependency Injection
    - Decreases coupling

*monkey patching
    Dynamically add an attribute to a instance of a class

'''
from abc import abstractmethod, ABC


class Book:
    def __init__(self, title, author, content: str):
        self.title = title
        self.author = author
        self.content = content


class Formatter:
    def format(self, book: Book):
        return book.content

class AuthorFormatter:
    def format(self, book: Book):
        return book.author


class Printer:
    def get_book(self, book: Book):
        formatter = Formatter()
        formatted_book = formatter.format(book)
        return formatted_book

    def get_author(self, book):
        formatter= AuthorFormatter()
        return formatter.format(book)


book = Book('Principles', 'Ray Dalio', 'Lorem lorem')
printer = Printer()
print(printer.get_author(book))

# Dependency inversion


class Book1:
    def __init__(self, title, author, content: str):
        self.title = title
        self.author = author
        self.content = content

class Formatter1(ABC):
    @abstractmethod
    def format(self, book: Book):
        pass

class ContentFormatter(Formatter):
    def format(self, book: Book):
        return book.content

class AuthorFormatter1(Formatter):
    def format(self, book: Book):
        return book.author


class Printer:
    def print(self, book, formatter):
        return formatter.format(book)

book = Book('Principles', 'Ray Dalio', 'Lorem lorem')
printer = Printer()
print(printer.print(book, AuthorFormatter1))
print(printer.print(book,ContentFormatter))
