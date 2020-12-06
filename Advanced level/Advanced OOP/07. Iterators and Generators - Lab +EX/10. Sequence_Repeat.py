class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration
        else:
            self.number -= 1
            self.counter += 1

            if self.counter == len(self.sequence):
                self.sequence += self.sequence
            return self.sequence[self.counter - 1]



result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
