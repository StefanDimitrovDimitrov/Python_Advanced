# def fibonacci():
#
#     current_int = 0
#     next_number = 1
#     previous_num = 0
#
#     while True:
#         yield current_int
#         previous_num = current_int
#         current_int += next_number
#         next_number = previous_num
#
#
# generator = fibonacci()
# for i in range(15):
#     print(next(generator))


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x


generator = fibonacci_numbers(10)
for _ in range(10):
    print(next(generator))