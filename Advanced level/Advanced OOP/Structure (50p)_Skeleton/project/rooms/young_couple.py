from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name: str, salary_one, salary_two):
        super().__init__(family_name, salary_one + salary_two, 2)
        self.room_cost = 20
        self.appliances =[TV(), Fridge(), Stove(),Laptop(), TV(), Fridge(), Stove(),Laptop()]
        self.calculate_expenses(self.appliances)
