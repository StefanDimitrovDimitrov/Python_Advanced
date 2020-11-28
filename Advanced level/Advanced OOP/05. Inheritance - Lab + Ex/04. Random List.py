import random

class RandomList(list):

    def get_random_element(self):
        element = random.choice(self)
        self.pop(self.index(element))
        return element


d = RandomList([1, 2, 4, 5, 6])
print(d.get_random_element())
print(list(d))