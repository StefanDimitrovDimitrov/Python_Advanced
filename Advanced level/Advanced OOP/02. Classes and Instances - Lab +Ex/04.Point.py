import math

class Point:

    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, new_x: int):
        self.x = new_x

    def set_y(self, new_y: int):
        self.y = new_y

    def distance(self, x, y):

        delta_x = abs(x - self.x)
        delta_y = abs(y - self.y)

        return math.sqrt(delta_x ** 2 + delta_y ** 2)

p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
