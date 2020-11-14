n = int(input())
all_elements = set()

for _ in range(n):
    elements = set(input().split())

    all_elements |= elements

print('\n'.join(all_elements))