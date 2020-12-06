from abc import ABC, abstractmethod

from project.animals.animal import Animal
from project.food import Meat


class Bird(Animal):

    @abstractmethod
    def __init__(self, name, weight: float, wing_size):
        self.wing_size = wing_size
        super().__init__(name, weight)

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Owl(Bird):

    def __init__(self, name, weight: float, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self,food):
        if isinstance(food, Meat):
            self.weight += 0.25 * food.quantity
            self.food_eaten += food.quantity
            return
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

class Hen(Bird):

    def __init__(self, name, weight: float, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self,food):
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity
        return

