days_stayed = int(input())
room_type = input()
feedback = input()

nights = days_stayed - 1
price = 1
discount = 0

if room_type == 'apartment':
    price = 25
    if nights < 10:
        discount = 0.3
    elif 10 <= nights <= 15:
        discount = 0.35
    elif nights > 15:
        discount = 0.5
elif room_type == "president apartment":
    price = 35
    if nights < 10:
        discount = 0.1
    elif 10 <= nights <= 15:
        discount = 0.15
    elif nights > 15:
        discount = 0.2
elif room_type == 'room for one person':
    price = 18

total_price = nights * price
if discount != 0:
    total_price -= total_price * discount

if feedback == "positive":
    total_price += total_price * 0.25
else:
    total_price -= total_price * 0.1

print(f'{total_price:.2f}')