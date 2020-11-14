# from collections import deque
#
#
# def solve(people, tosses_count):
#     people = deque(people)
#     index = 0
#
#     while people:
#         index += 1
#         person = people.popleft()
#         if index == tosses_count:
#             if people:
#                 index = 0
#                 print(f'Removed {person}')
#             else:
#                 print(f'Last is {person}')
#         else:
#             people.append(person)
#
# solve(input().split(' '),
#       int(input())
# )

from collections import deque

people = deque(input().split(' '))
n_toss = int(input())

while len(people) > 1:
    people.rotate(-n_toss)
    loser = people.pop()
    print(f'Removed{loser}')

winner = people.pop()
print(f'last is {winner}')
