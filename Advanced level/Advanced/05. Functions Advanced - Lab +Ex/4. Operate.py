from functools import reduce


def operate(op, *args):
    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }
    return reduce(ops[op], args)


print(operate('/', *[i for i in range(1, 10)]))
