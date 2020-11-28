class vowels:

    def __init__(self, string):
        self.string = string
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i <= (len(self.string) - 1):
            c = self.string[self.i]
            self.i += 1
            if self.is_vowels(c):
                return c
        raise StopIteration

    @staticmethod
    def is_vowels(c):
        vowels = "aouiey"
        return c.lower() in vowels


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
