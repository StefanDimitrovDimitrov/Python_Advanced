numbers_from_input = input().split()

numbers = map(int, numbers_from_input)
print(sorted(numbers))

print(list(map(lambda s: sorted(int(s), reverse=True), numbers_from_input)))
