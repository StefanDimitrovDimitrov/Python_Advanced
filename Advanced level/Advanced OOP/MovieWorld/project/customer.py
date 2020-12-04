from typing import List


class Customer:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

        self.rented_dvds: List = []

    def __repr__(self):
        dvds_names = ", ".join([dvd.names for dvd in self.rented_dvds])
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({dvds_names})"

