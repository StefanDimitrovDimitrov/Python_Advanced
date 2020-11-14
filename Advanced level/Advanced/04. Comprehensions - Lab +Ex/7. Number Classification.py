numbers = input().split(", ")


print(f"Positive: {', '.join([f'{int(x)}' for x in numbers if int(x) >= 0])}")
print(f"Negative: {', '.join([f'{int(x)}' for x in numbers if int(x) < 0])}")
print(f"Even: {', '.join([f'{int(x)}' for x in numbers if int(x) % 2 == 0])}")
print(f"Odd: {', '.join([f'{int(x)}' for x in numbers if int(x) % 2 != 0])}")
