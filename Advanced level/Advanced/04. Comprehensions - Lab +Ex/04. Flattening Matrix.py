n = int(input())

print([int(n) for _ in range(n) for n in input().split(', ')])