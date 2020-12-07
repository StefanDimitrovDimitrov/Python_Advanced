from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

class Car(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
        self.air_conditioners = 0.9

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.air_conditioners)
        if fuel_needed > self.fuel_quantity:
            return
        self.fuel_quantity -= fuel_needed


    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
        self.air_conditioners = 1.6

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.air_conditioners)
        if fuel_needed > self.fuel_quantity:
            return
        self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

import unittest

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car(100, 2)

    def test_drive_not_enough_fuel(self):
        self.car.drive(40)

        self.assertEqual(self.car.fuel_quantity, 100)

    def test_drive_car_enough_fuel(self):
        self.car.drive(10)

        self.assertEqual(self.car.fuel_quantity, 71)

    def test_refuel(self):
        self.car.refuel(50)
        self.assertEqual(self.car.fuel_quantity,150)


class TestTruck(unittest.TestCase):
    def setUp(self):
        self.truck = Truck(100, 6)

    def test_drive_not_enough_fuel(self):
        #ACT
        self.truck.drive(40)

        #accert
        self.assertEqual(self.truck.fuel_quantity, 100)

    def test_drive_truck_enough_fuel(self):
        self.truck.drive(10)

        self.assertEqual(self.truck.fuel_quantity, 24)

    def test_refuel(self):
        self.truck.refuel(50)
        self.assertEqual(self.truck.fuel_quantity, 147.5)

if __name__ == "__main__":
    unittest.main()