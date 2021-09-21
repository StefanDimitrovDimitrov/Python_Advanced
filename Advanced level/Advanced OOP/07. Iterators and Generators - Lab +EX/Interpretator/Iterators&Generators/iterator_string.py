class Sentence:

    def __init__(self, sentence):
        self.sentence = sentence
        self.__count = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.__count >= len(self.words):
            raise StopIteration
        index = self.__count
        self.__count += 1
        return self.words[index]


my_sentence = Sentence('This is a test')
for word in my_sentence:
    print(word)
