text = input()
n = int(input())

dirs = {
    "up": [-1, 0],
    "down": [-1, 0],
    "left": [-1, 0],
    "right": [-1, 0]
}

field = []
player_pos = []

for row in range(n):
    line = list(input())
    if "P" in line:
        player_pos = [row, line.index("P")]
    field. append(line)

commands_count = int(input())

for _ in range(commands_count):
    command = input()
    direction_change = dirs[command]
    next_row = player_pos[0] + direction_change[0]
    next_col = player_pos[1] + direction_change[1]
    next_pos = [next_row, next_col]

    if 0 <= next_row < n and 0 <= next_col < n:
        if field[next_row][next_col] == "-":
            field[player_pos[0]][player_pos[1]] = "-"
            player_pos = next_pos
            field[player_pos[0]][player_pos[1]] = "P"
        else:
            field[player_pos[0]][player_pos[1]] = "-"
            text+= field[next_row] [next_col]
            player_pos = next_pos
            field[player_pos[0]][player_pos[1]] = "P"
    else:
        text = text[:-1]

print(text)
[print(''.join(row)) for row in field]