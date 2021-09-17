def print_rhombus(n):
    growing: int = 1 # global nameSpace
    shrinking: int = -1

    # fn- fn -fn -closure
    def print_line(i, direction):# local Namespace visible only in print_rhombus
        if i == 0:
            return
        line = ' ' * (n - i) + "* " * i
        print(line.rstrip())  # remove all spaces from the right
        if i == n:
            direction = shrinking
        print_line(i + direction, direction)

    print_line(1, growing)


print_rhombus(int(input()))
