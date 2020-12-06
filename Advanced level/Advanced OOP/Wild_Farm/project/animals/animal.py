from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass


class Bird(Animal):
    @abstractmethod
    def __init__(self, name, weight: float):
        super().__init__(name, weight)


class Mammal(Animal):
    @abstractmethod
    def __init__(self, name, weight: float):
        super().__init__(name, weight)
