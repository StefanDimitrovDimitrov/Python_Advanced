from abc import ABC, abstractmethod


class Card(ABC):

    @abstractmethod
    def __init__(self, name, damage_point: int, health_points: int):
        self.name = name
        self.damage_point = damage_point
        self.health_points = health_points

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Card's name cannot be an empty string.")
        self._name = value

    @property
    def damage_point(self):
        return self._damage_point

    @damage_point.setter
    def damage_point(self, value):
        if value < 0:
            raise ValueError("Card's damage points cannot be less than zero.")
        self._damage_point = value

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        if value < 0:
            raise ValueError("Card's HP cannot be less than zero.")
        self._health_points = value
