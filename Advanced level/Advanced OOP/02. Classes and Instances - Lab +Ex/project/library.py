from typing import Dict, List, ClassVar, Tuple
from project.user import User


class Library:
    user_records: ClassVar[List[User]] = []
    books_available: ClassVar[Dict[str, List[str]]] = {}
    rented_books: ClassVar[Dict[str, Dict[str, int]]] = {}
    rented_books_by_book_name: ClassVar[Dict[str, Tuple[str, int]]] ={}


    # def __init__(self):
    #     self.user_records = []
    #     self.books_available = {}
    #     self.rented_books = {}
    #
    def add_user(self, user: User):
        if user in self.user_record:
            return f"User with id = {User.self.user_id} already registered in the library!"

        self.user_records.append(user)

    def remove_user(self, user: User):
        if user not in self.user_records:
            return "We could not find such user to remove!"

        self.user_records.remove(user)
        self.rented_books.remove(self.rented_books[user])

    #     del self.rented_books[User.username]

    def change_user(self, user_id: int, new_username: str):
        users.ids = [u.id for u in self.records]
        if user_id not in user_ids:
            return f"There is no user with id = {user_id}!"

        user = self.user_records[users.ids.index(user_id)]
        if User.username == new_isername:
            return "Please check again the provided username\
                    - it should be different than the" \
                   "username used so far!"
