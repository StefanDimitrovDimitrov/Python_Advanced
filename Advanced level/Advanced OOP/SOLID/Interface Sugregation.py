'''
A client should not depend on methods it does not use
        - a good way of ensuring this is by separation through multiple inheritance
        - this is precisely the purpose of the mix-ins to provide multiple clients specific behaviors

    Python doesn't have interfaces

    не трябва да принуждаваме подкласовете да използват методи, които немогат да имплементират.

    To avoid this we can use mix in or to ad another class with the specific methods. "Composition"

'''

#Violation
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def drew_circle(self):
        pass

    @abstractmethod
    def drew_rectangle(self):
        pass


class Circle():
    def drew_circle(self):
        pass

    def drew_rectangle(self):
        pass


#the right way

from abc import ABC, abstractmethod


class Shape1(ABC):
    @abstractmethod
    def drew(self):
        pass


class Circle1():
    def drew(self):
        pass


#COMPOSITION

class Connector:
    def connect(self, other):
        pass

class  HDMIConnector(Connector):
    pass

class PowerConnector(Connector):
    pass

class EthernetConnector(Connector):
    pass



class Television:
    def __init__(self):
        self.hdmi_connector = HDMIConnector()
        self.power_connector = PowerConnector()
        self.ethernet_connector = EthernetConnector()

class GameConsole:
    def __init__(self):
        self.hdmi_connector = HDMIConnector()
        self.power_connector = PowerConnector()
        self.ethernet_connector = EthernetConnector()

class Router:
    def __init__(self):
        self.ethernet_connector = EthernetConnector()


tv = Television()
game_console = GameConsole()

tv.hdmi_connector.connect(game_console.hdmi_connector)
