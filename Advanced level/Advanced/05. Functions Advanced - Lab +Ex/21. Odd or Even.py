command = input()

numbers = list(map(int, input().split()))

sum_odd = (sum(filter(lambda number: number %2 != 0, numbers)))
sum_even =(sum(filter(lambda number: number %2 == 0, numbers)))


print(sum_odd * len(numbers) if command == "Odd" else sum_even * len(numbers))

