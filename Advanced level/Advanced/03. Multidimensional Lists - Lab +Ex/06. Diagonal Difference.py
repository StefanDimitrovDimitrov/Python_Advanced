# n = int(input())
#
# matrix = [[int(j) for j in input().split()] for _ in range(n)]
# result_primary = sum([v[j] for j,v in enumerate(matrix)])
# # result_secondary = sum([v[t-1] for t,v in enumerate(matrix)])
#
# result_secondary = 0
# count = n-1
#
# for t,v in enumerate(matrix):
#     result_secondary += v[count]
#     count -= 1
#
#
# total= abs(result_primary - result_secondary)
#
# print(total)


size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for i in range(len(matrix)):
    primary_diagonal_sum += matrix[i][i]
    secondary_diagonal_sum += matrix[i][size - i -1]

difference = abs(primary_diagonal_sum - secondary_diagonal_sum)
print(difference)






