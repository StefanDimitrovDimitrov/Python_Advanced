import math

class Point:

    x = float
    y = float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x
        return self.x

    def set_y(self, new_y):
        self.y = new_y
        return self.y

    def distance(self, x, y):

        p1,p2 = self.x, self.y
        p3,p4 = x, y

        distance = math.sqrt(((p1 - p3) ** 2 + (p2 - p4) ** 2))
        return f"{distance}"

p = Point(2, 4)
p.set_x(3.5)
p.set_y(5.3)
print(p.distance(10, 2))
