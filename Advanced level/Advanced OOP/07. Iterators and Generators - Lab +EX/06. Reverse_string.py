def reverse_text(string):
    a = string[::-1]
    yield a


for char in reverse_text("step"):
    print(char, end='')
