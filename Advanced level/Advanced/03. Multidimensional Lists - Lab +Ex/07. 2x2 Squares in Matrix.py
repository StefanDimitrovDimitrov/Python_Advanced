rows, cols = [int(x) for x in input().split()]
matrix = [[n for n in input().split()] for n in range(rows)]
counter = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        current = matrix[row][col]
        to_the_right = matrix[row][col+1]
        to_the_bottom = matrix[row+1][col]
        bottom_right = matrix[row+1][col+1]
        if current == to_the_right == to_the_bottom == bottom_right:
            counter+=1

print(counter)

