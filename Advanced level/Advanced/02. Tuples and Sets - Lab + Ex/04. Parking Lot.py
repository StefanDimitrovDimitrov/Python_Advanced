# Input:
    # 10
    # IN, CA2844AA
    # IN, CA1234TA
    # OUT, CA2844AA
    # IN, CA9999TT
    # IN, CA2866HI
    # OUT, CA1234TA
    # IN, CA2844AA
    # OUT, CA2866HI
    # IN, CA9876HH
    # IN, CA2822UU

# Output
    # CA2844AA
    # CA9999TT
    # CA2822UU
    # CA9876HH


# Solution 1
def Solution_1():
    parking_lot = set()

    commands_count = int(input())

    for _ in range(commands_count):
        command, car = input().split(', ')
        if command == 'IN':
            parking_lot.add(car)
        else:
            parking_lot.remove(car)

    if parking_lot:
        [print(car) for car in parking_lot]
    else:
        print('Parking Lot is Empty')

# Solution 2
def Solution_2():
    n = int(input())
    parking = set()

    for _ in range(n):
        direction, req_num = input().split(', ')
        operations = {
            "IN": parking.add,
            "OUT": parking.remove,
        }
        operations[direction](req_num)

    if parking:
        print("\n".join(parking))
    else:
        print("Parking Lot is Empty")
