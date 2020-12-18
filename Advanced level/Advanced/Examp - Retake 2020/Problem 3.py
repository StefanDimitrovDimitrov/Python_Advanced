

string = input()
n = int(input())
matrix = []
player_pos = None

for row in range(n):
    line = list(input())
    if "P" in line:
        player_pos = [row, line.index("P")]
    matrix.append(line)

m = int(input())

move = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for _ in range(m):
    command = input()
    direction_change = move[command]
    next_row = player_pos[0] + direction_change[0]
    next_col = player_pos[1] + direction_change[1]
    next_pos = [next_row, next_col]

    if 0 <= next_row < n and 0 <= next_col < n:
        if matrix[next_row][next_col] == "-":
            matrix[player_pos[0]][player_pos[1]] = "-"
            player_pos = next_pos
            matrix[player_pos[0]][player_pos[1]] = "P"
        else:
            matrix[player_pos[0]][player_pos[1]] = "-"
            string += matrix[next_row] [next_col]
            player_pos = next_pos
            matrix[player_pos[0]][player_pos[1]] = "P"
    else:
        string = string[:-1]

print(string)
[print(''.join(row)) for row in matrix]
