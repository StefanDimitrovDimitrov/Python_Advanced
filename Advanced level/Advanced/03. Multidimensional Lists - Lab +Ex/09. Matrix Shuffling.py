def is_the_coomand_valid(command):

    is_valid = True

    if command[0] != "swap":
        is_valid = False

    if len(command[1:]) != 4:
        is_valid = False
    else:
        i1,j1,i2,j2 = tuple(map(int, command[1:]))

        if i1 < 0 or i1 >= rows:
            is_valid = False
        if i2< 0 or i2 >= rows:
            is_valid = False
        if j1 <0 or j1 >= cows:
            is_valid = False
        if j2 <0 or j2 >= cows:
            is_valid = False


    # for x in coordinates:
    #     if int(x) > cows:
    #         is_valid = False
    #         break

    return is_valid

rows, cows = [int(n) for n in input().split()]

matrix = [[n for n in input().split()] for _ in range(rows)]


while True:
    command = input()
    if command == "END":
        break
    command = command.split()

    if is_the_coomand_valid(command):
        r1,c1,r2,c2 = tuple(map(int,command[1:]))

        matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]

        for row in matrix:
            print(' '.join(row))
    else:
        print("Invalid input!")