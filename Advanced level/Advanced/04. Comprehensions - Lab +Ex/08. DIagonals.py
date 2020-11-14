size = int(input())

matrix = [[int(x) for x in input().split(", ")]for _ in range(size)]


primary_diagonal = [matrix[i][i] for i in range(size)]
secondary_diagonal = [matrix[i][size - i - 1] for i in range(size)]

print(f"First diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Second diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
