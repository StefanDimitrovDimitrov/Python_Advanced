n=[1, 2, 3, 4, 5]

filter_1 = [
    'baba' if x % 2 ==0 else 'dqdo' #output expression
    for x in n                      # interation over n
]

filter_2 = [
    'baba'              #output expression
    for x in n
    if x % 2 == 0       #filtration
]

print(filter_1)
print(filter_2)