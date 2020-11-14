chessboard = [list(input().split()) for _ in range(8)]

q_fields = []
k_field = []


def search_matrix(chessboard, search):
    for y, row in enumerate(chessboard):
        for x, char in enumerate(row):
            if char == search:
                cordinates = [y, x]
                q_fields.append(cordinates)
    return q_fields


def search_matrix_k(chessboard, search):
    for y, row in enumerate(chessboard):
        for x, char in enumerate(row):
            if char == search:
                cordinates = [y, x]
                k_field.append(cordinates)
    return k_field


search_matrix(chessboard, "Q")
search_matrix_k(chessboard, "K")


def queen_coverage(y, x):
    q_coverage = {
        "Horizontally_right": [[y, x + 1], [y, x + 2], [y, x + 3], [y, x + 4], [y, x + 5], [y, x + 6], [y, x + 7],
                               [y, x + 8]],
        "Horizontally_left": [[y, x - 1], [y, x - 2], [y, x - 3], [y, x - 4], [y, x - 5], [y, x - 6], [y, x - 7],
                              [y, x - 8]],
        "Vertically_up": [[y + 1, x], [y + 2, x], [y + 3, x], [y + 4, x], [y + 5, x], [y + 6, x], [y + 7, x],
                          [y + 8, x]],
        "Vertically_down": [[y - 1, x], [y - 2, x], [y - 3, x], [y - 4, x], [y - 5, x], [y - 6, x], [y - 7, x],
                            [y - 8, x]],
        "Diagonally_prime_up": [[y - 1, x - 1], [y - 2, x - 2], [y - 3, x - 3], [y - 4, x - 4], [y - 5, x - 5],
                                [y - 6, x - 6], [y - 7, x - 7], [y - 8, x - 8]],
        "Diagonally_prime_down": [[y + 1, x + 1], [y + 2, x + 2], [y + 3, x + 3], [y + 4, x + 4], [y + 5, x + 5],
                                  [y + 6, x + 6], [y + 7, x + 7], [y + 8, x + 8]],
        "Diagonally_second_up": [[y - 1, x + 1], [y - 2, x + 2], [y - 3, x + 3], [y - 4, x + 4], [y - 5, x + 5],
                                 [y - 6, x + 6], [y - 7, x + 7], [y - 8, x + 8]],
        "Diagonally_second_down": [[y + 1, x - 1], [y + 2, x - 2], [y + 3, x - 3], [y + 4, x - 4], [y + 5, x - 5],
                                   [y + 6, x - 6], [y + 7, x - 7], [y + 8, x - 8]],
    }
    return q_coverage


list_directions = ["Horizontally_right", "Horizontally_left", "Vertically_up", "Vertically_down", "Diagonally_prime_up",
                   "Diagonally_prime_down", "Diagonally_second_up", "Diagonally_second_down"]

win_list = []

for cordinates in q_fields:
    for dirc in list_directions:
        coverage = queen_coverage(cordinates[0], cordinates[1])
        queen_fields = coverage[dirc]

        for field in queen_fields:
            if field in q_fields and field != cordinates:
                break
            elif field == k_field[0]:
                win_list.append(cordinates)

if win_list == []:
    print("The king is safe!")
else:
    for x in win_list:
        print(x)
