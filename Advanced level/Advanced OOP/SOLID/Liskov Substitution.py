'''

- унаследените типове трябва да могат да заменят напълно базовите си типове.
    - defines the relationship between subtypes and supertypes in object-oriented programming

    Derived types(производните типове) must be completely substitutable for their base types

    Whatever the parent can do, the descendants should at least be able to do that too

    Derived classes

        - only extend functionalities of the base class
        - must not remove base class behavior

    tip :
    -   if we have to check the type of let's say person that means that we probably violate the principle
    -   override a method of the superclass by an empty method

'''
from abc import ABC, abstractmethod

'''
Violation

'''


class Robot:
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type


class Android(Robot):
    def android_senzors_count(self):
        return 4


class Chappie(Robot):
    def chappie_senzors_count(self):
        return 6


def count_robot_senzors(robots: list):  # violates:OCP, LSP
    for robot in robots:
        if isinstance(robot, Android):
            print(robot.android_senzors_count())
        elif isinstance(robot, Chappie):
            print(robot.chappie_senzors_count())


# the right way

class Robot1(ABC):
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type

    @abstractmethod
    def get_sensors_count(self):
        pass


class Android1(Robot1):
    def get_sensors_count(self):
        return 4


class Chappie1(Robot):
    def get_sensors_count(self):
        return 6


def count_robot_sensors1(robots: list):  # violates:OCP, LSP
    for robot in robots:
        print(robot.get_senzors_count())


robots = [Android1('Robocop'), Chappie1('XIX')]
count_robot_sensors1(robots)
