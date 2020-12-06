from abc import ABC, abstractmethod

from project.animals.animal import Animal
from project.food import Meat, Vegetable, Fruit


class Mammal(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight: float, living_region: str):
        self.living_region = living_region
        super().__init__(name, weight)

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Mouse(Mammal):

    def __init__(self, name, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if isinstance(food, Fruit) or isinstance(food, Vegetable):
            self.weight += 0.10 * food.quantity
            self.food_eaten += food.quantity
            return
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Dog(Mammal):

    def __init__(self, name, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 0.40* food.quantity
            self.food_eaten += food.quantity
            return
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Cat(Mammal):

    def __init__(self, name, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if isinstance(food, Meat) or isinstance(food, Vegetable):
            self.weight += 0.30* food.quantity
            self.food_eaten += food.quantity
            return
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):

    def __init__(self, name, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 1* food.quantity
            self.food_eaten += food.quantity
            return
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
