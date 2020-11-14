n = int(input())
matrix = [[int(j) for j in input().split()] for _ in range(n)]
result = sum([v[j] for j,v in enumerate(matrix)])

print(result)
