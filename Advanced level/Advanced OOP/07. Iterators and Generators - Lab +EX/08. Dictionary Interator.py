class dictionary_iter:

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter+1 == len(self.dictionary.items()):
            raise StopIteration
        else:
            r = [(k, v) for (k, v) in self.dictionary.items()]
            self.counter += 1
            return r[self.counter]



result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
