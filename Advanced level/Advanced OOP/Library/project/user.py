from project.library import Library

class User:

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library: 'Library'):
        if author in library.books_available and book_name in library.books_available[author]:
            self.books.append(book_name)

            if self.username not in library.rented_books:
                library.rented_books[self.username] = {}

            library.rented_books[self.username][book_name ]= days_to_return
            library.books_available[author].remove(book_name)
            library.rented_books_by_book_name[book_name] = (self.username, days_to_return)

        elif book_name in library.rented_books_by_book_name:
            _, days_to_return = library.rented_books_by_book_name[book_name]
            return f'The book "{book_name}" is already rented and will be available in {days_to_return} days!'

    def return_book(self,author:str, book_name:str, library: Library):
        if book_name  not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"

        self.books.remove(book_name)
        library.books_available[author].append(book_name)
        del library.rented_books[self.username][book_name]

    def info(self):
        pass

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"