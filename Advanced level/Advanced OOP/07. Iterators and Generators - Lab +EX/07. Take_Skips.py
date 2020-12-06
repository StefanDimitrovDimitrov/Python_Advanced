class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0
        # self.end = self.start + self.count * self.step - self.step

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        else:
            self.start += self.step
            self.count -= 1
            return self.start - self.step


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
