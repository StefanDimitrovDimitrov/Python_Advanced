from  collections import deque

def list_manipulator(*arg):

    list_1 = arg
    temp_list = deque(list_1[0].copy())

    if list_1[1] == "remove":
        if list_1[2] == "end":
            if len(list_1) < 4:
                temp_list.pop()
            else:
                for _ in range(list_1[3]):
                    temp_list.pop()
        elif list_1[2] == "beginning":
            if len(list_1) < 4:
                temp_list.popleft()
            else:
                for _ in range(list_1[3]):
                    temp_list.popleft()
    elif list_1[1] == "add":
        if list_1[2] == "end":
            for item,i in enumerate(list_1):
                if item >= 3:
                    temp_list.append(i)
        elif list_1[2] == "beginning":
            temp = []
            for i,item in enumerate(list_1):
                if i >= 3:
                    temp.append(item)
            for item in reversed(temp):
                temp_list.appendleft(item)


    return list(temp_list)
#
print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
