numbers = list(map(int, input().split(' ')))

negatives = (sum(filter(lambda number: number < 0 , numbers)))
positives = (sum(filter(lambda number: number >= 0, numbers)))

print(negatives)
print(positives)

if abs(negatives) > (positives):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")