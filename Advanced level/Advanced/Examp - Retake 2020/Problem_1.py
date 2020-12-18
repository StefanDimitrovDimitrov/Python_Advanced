from collections import deque

input_male = [int(x) for x in input().split()]
input_females = deque([int(x) for x in input().split()])

successful_matches = 0

while input_male and input_females:
    if input_male[-1] <= 0:
        input_male.pop()
        continue

    if input_females[0] <= 0:
        input_females.popleft()
        continue

    if input_male[-1] % 25 == 0:
        input_male.pop()
        if input_male and input_females:
            input_male.pop()
        else:
            break

    if input_females[-1] % 25 == 0:
        input_females.popleft()
        if input_male and input_females:
            input_females.popleft()
        else:
            break

    if input_male and input_females:
        if input_male[-1] == input_females[0]:
            input_male.pop()
            input_females.popleft()
            successful_matches +=1
        else:
            input_females.popleft()
            input_male[-1] -= 2



print(f'Matches: {successful_matches}')
if not input_male:
    print("Males left: none")
else:
    print(f"Males left: {', '.join([str(male) for male in input_male[::-1]])}")

if not input_females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join([str(female) for female in input_females])}")

