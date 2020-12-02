from typing import Dict, List, ClassVar, Tuple


class Library:
    user_records: ClassVar[List[User]] = []
    books_available: ClassVar[Dict[str, List[str]]] = {}
    rented_books: ClassVar[Dict[str, Dict[str, int]]] = {}
    rented_books_by_book_name: ClassVar[Dict[str, Tuple[str, int]]] = {}

    # def __init__(self):
    #     self.user_records = []
    #     self.books_available = {}
    #     self.rented_books = {}
    #
    def add_user(self, user: User):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        self.user_records.append(user)

    def remove_user(self, user: User):
        if user not in self.user_records:
            return "We could not find such user to remove!"

        self.user_records.remove(user)

        del self.rented_books[user.username]

    def change_username(self, user_id: int, new_username: str):
        users_ids = [u.id for u in self.user_records]
        user = self.user_records[users_ids.index(user_id)]

        if user_id == user.user_id:
            if user.username == new_username:
                return "Please check again the provided username - it should be different than the username used so far!"

            user.username = new_username
            return f"Username successfully changed to: {new_username} for userid: {user_id}"

        return f"There is no user with id = {user_id}!"


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

            library.rented_books[self.username][book_name] = days_to_return
            library.books_available[author].remove(book_name)
            library.rented_books_by_book_name[book_name] = (self.username, days_to_return)

        elif book_name in library.rented_books_by_book_name:
            _, days_to_return = library.rented_books_by_book_name[book_name]
            return f'The book "{book_name}" is already rented and will be available in {days_to_return} days!'

    def return_book(self, author: str, book_name: str, library: Library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"

        self.books.remove(book_name)
        library.books_available[author].append(book_name)
        del library.rented_books[self.username][book_name]

    def info(self):
        pass

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
