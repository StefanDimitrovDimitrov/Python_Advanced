

def print_rhombus(n):
    growing = 1
    shrinking = -1

    # fn- fn -fn -closure
    def print_line(i, direction):
        if i == 0:
            return
        line = ' ' * (n - i) + "* " * i
        print(line.rstrip()) # remove all spaces from the right
        if i == n:
            direction = shrinking
        print_line(i + direction, direction)

    print_line(1, growing)


print_rhombus(int(input()))
