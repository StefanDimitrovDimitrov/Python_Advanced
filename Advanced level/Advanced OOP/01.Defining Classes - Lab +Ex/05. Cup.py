class Cup():

    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        current_size = self.size - self.quantity
        if milliliters <= current_size:
            self.quantity += milliliters

    def status(self, ):
        return self.size - self.quantity


cup = Cup(100, 10)
cup.fill(50)
cup.fill(10)
print(cup.status())
