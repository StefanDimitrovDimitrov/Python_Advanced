from collections import deque

input_male = [int(x) for x in input().split()]
input_females = deque([int(x) for x in input().split()])

successful_matches = 0

while input_male and input_females:
    current_female = input_females[0]
    current_male = input_male[-1]

    if current_female <= 0:
        input_females.popleft()

    elif current_male <= 0:
        input_male.pop()

    elif current_male == current_female:
        input_females.popleft()
        input_male.pop()
        successful_matches += 1

    elif current_female % 25 == 0:
        input_females.popleft()
        input_females.popleft()

    elif current_male % 25 == 0:
        input_male.pop()
        input_male.pop()

    else:
        input_females.popleft()
        input_male.append(input_male.pop() - 2)



print(f'Matches: {successful_matches}')
if not input_male:
    print("Males left: none")
else:
    print(f"Males left: {', '.join([str(male) for male in input_male[::-1]])}")

if not input_females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join([str(female) for female in input_females])}")