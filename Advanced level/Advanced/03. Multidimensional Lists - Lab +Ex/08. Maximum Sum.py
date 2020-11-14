rows, cols = [int(n) for n in input().split()]
matrix = [[int(n) for n in input().split()] for _ in range(rows)]

max_sum = -999999999999
current_sum = 0
matrix_print = []

for row in range(rows - 2):
    for cow in range(cols - 2):
        first = matrix[row][cow]
        second = matrix[row][cow + 1]
        third = matrix[row][cow + 2]
        fourth = matrix[row + 1][cow]
        fifth = matrix[row + 1][cow + 1]
        sixth = matrix[row + 1][cow + 2]
        seventh = matrix[row + 2][cow]
        eighth = matrix[row + 2][cow + 1]
        ninth = matrix[row + 2][cow + 2]

        current_sum = first + second + third + fourth + fifth + sixth + seventh + eighth + ninth

        if current_sum > max_sum:
            max_sum = current_sum
            matrix_print = [[first, second, third], [fourth, fifth, sixth], [seventh, eighth, ninth]]


print(f"Sum = {max_sum}")

for row in matrix_print:
    print(' '.join([str(x) for x in row]))
