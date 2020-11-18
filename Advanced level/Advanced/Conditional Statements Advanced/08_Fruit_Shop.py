fruit = input()
day = input()
quantity = float(input())

price = 0

if day == "Monday" or day == "Tuesday" or day == 'Wednesday' or day == "Thursday" or day == "Friday":
    if fruit =="banana":
        price = 2.5
    elif "apple" == fruit:
        price = 1.2
    elif "orange" == fruit:
        price = 0.85
    elif "grapefrui" == fruit:
        price = 1.45
    elif "kiwi" == fruit:
        price = 2.7
    elif "pineapple" == fruit:
        price = 5.5
    elif "grapes" == fruit:
        price = 3.85
elif day == "Saturday" or day == 'Sunday':
    if "banana" == fruit:
        price = 2.7
    elif "apple" == fruit:
        price = 1.25
    elif "orange" == fruit:
        price = 0.9
    elif "grapefruit" == fruit:
        price = 1.6
    elif "kiwi" == fruit:
        price = 3
    elif "pineapple" == fruit:
        price = 5.6
    elif "grapes" == fruit:
        price = 4.2

if price == 0:
    print('error')
else:
    print (f"{price * quantity: .2f}")





