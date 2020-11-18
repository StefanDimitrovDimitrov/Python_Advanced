number = float(input())

is_number = number >= -100 and number <= 100 and number != 0

if is_number:
    print("Yes")
else:
    print("No")