from collections import deque

def best_list_pureness(list, num):

    pureness = []
    list = deque(list)
    for i in range(num):
        result = 0

        if i > 0:
            num = list.pop()
            list.appendleft(num)

        for i, value in enumerate(list):
            result += i * int(value)
        pureness.append(result)




    result = f"Best pureness {max(pureness)} after {pureness.index(max(pureness))} rotations"
    return result

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)


