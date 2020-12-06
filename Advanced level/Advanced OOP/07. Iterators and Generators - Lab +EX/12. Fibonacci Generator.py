def fibonacci():

    current_int = 0
    next_number = 1
    previous_num = 0

    while True:
        yield current_int
        previous_num = current_int
        current_int += next_number
        next_number = previous_num


generator = fibonacci()
for i in range(15):
    print(next(generator))
