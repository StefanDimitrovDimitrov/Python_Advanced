from dataclasses import dataclass


@dataclass  # decorator replace the __init__(self, name,author,pages)
class Book:
    name: str
    author: str
    pages: int


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)
