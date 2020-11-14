energy = int(input())
n = int(input())

matrix = []
paris_pos = []

dirs = {
    "up": [-1, 0],
    "down": [-1, 0],
    "left": [-1, 0],
    "right": [-1, 0]
}


for row in range(n):
    line = list(input())
    if "P" in line:
        paris_pos = [row, line.index("P")]
    matrix.append(line)

[print(row) for row in matrix]

while True:
    tokens = input().split()
    dir = tokens[0]
    new_enemy_pos = [int(tokens[1]), int(tokens[2])]
    matrix[new_enemy_pos[0]][new_enemy_pos[1]] = "S"

    direction_change = dirs[dir]
    new_paris_row = paris_pos[0] + direction_change[0]
    new_paris_col = paris_pos[1] + direction_change[1]
    energy -= 1

    if new_paris_row < n and 0 <= new_paris_col < n:
        if matrix[new_paris_row][new_paris_col] == "-":
            matrix[paris_pos[0]][paris_pos[1]] = "-"
            matrix[new_paris_row][new_paris_col] = "P"
            paris_pos = [new_paris_row, new_paris_col]
        elif matrix[new_paris_row][new_paris_col] == "S":
            energy -= 2
            matrix[paris_pos[0]][paris_pos[1]] = "-"
            matrix[new_paris_row][new_paris_col] = "P"
            paris_pos = [new_paris_row, new_paris_col]

        elif matrix[new_paris_row][new_paris_col] == "H":
            matrix[paris_pos[0]][paris_pos[1]] = "-"
            matrix[new_paris_row][new_paris_col] = "-"

            print("Paris has successfully abducted Helen")
            break