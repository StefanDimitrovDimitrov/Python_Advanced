class Child:
    def __init__(self,food_cost:int, *toys_cost):
        # self.food_cost = food_cost
        # self.toys_cost = toys_cost

        self.cost = food_cost + sum(toys_cost)

