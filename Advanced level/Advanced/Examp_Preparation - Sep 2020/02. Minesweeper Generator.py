def fill_the_matrix(matrix,bombs_coordinates):
    for coordinate in bombs_coordinates:


        y = int(coordinate.split(", ")[0].replace("(",""))
        x = int(coordinate.split(", ")[1].replace(")",""))
        bombs_locatiion = [y, x]
        list_bomb_location.append(bombs_locatiion)
        matrix[y][x] = "*"
    return list_bomb_location

list_bomb_location =[]
size = int(input())
bombs = int(input())

matrix = [[0 for number in range(size)]for _ in range(size)]

bombs_coordinates = []
for x in range(bombs):
    bombs_coordinates.append(input())

dict = {

    "Horizontally_right": [0, + 1],
    "Horizontally_left": [0, - 1],
    "Vertically_up": [+ 1, 0],
    "Vertically_down": [- 1, 0],
    "Diagonally_prime_up": [- 1, - 1],
    "Diagonally_prime_down": [+ 1, + 1],
    "Diagonally_second_up": [- 1, + 1],
    "Diagonally_second_down": [+ 1, - 1],

}

fill_the_matrix(matrix,bombs_coordinates)
for location in list_bomb_location:
    for key,item in dict.items():
        new_y = location[0]+item[0]
        new_x = location[1]+item[1]

        if 0 <= new_y < size and 0 <= new_x < size:
            if matrix[new_y][new_x] != "*":
                matrix[new_y][new_x] +=1

for row in matrix:
    print(' '.join([str(x) for x in row]))
