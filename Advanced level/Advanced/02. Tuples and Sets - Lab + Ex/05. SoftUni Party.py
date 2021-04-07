
#Solution 1
def solution1():
    def input_to_list(lines_count):
        return [input() for _ in range(lines_count)]


    def input_to_list_until_command(command):
        result = []

        while True:
            line = input()
            if line == command:
                break
            result.append(line)

        return result


    def get_not_arrived_guests(guests, guests_arrived):
        return set(guests) - set(guests_arrived)


    def print_result(result):
        result = sorted(result)
        print(len(result))
        [print(guest) for guest in result if guest[0].isdigit()]
        [print(guest) for guest in result if not guest[0].isdigit()]


    guests = input_to_list(int(input()))
    guests_arrived = input_to_list_until_command('END')

    print_result(
        get_not_arrived_guests(guests, guests_arrived)
    )

#Solution 2
def solution2():
    n = int(input())
    guests = set()
    attended = set()

    for _ in range(n):
        num = input()
        guests.add(num)

    while True:
        command = input()
        if command == "END":
            break
        attended.add(command)

    unattended = guests - attended
    print(len(unattended))
    print('\n'.join(sorted(unattended)))