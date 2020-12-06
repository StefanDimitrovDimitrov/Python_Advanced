import itertools


def possible_permutations(arg):
    for per in itertools.permutations(arg):
        yield list(per)


[print(n) for n in possible_permutations([1, 2, 3])]
