numbers = [int(x) for x in input().split(", ")]
index = int(input())

target = numbers[index]
total_clock_cycles = 0

clock_cycles = 0


for i, num in enumerate(numbers):
    if num <= target and i != index:
        clock_cycles += num

total_clock_cycles = clock_cycles + target


print (total_clock_cycles)
