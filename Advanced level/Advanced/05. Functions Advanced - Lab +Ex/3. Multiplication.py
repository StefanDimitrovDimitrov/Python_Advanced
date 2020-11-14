# 1st solution

# import math
#
# multiply = lambda * args: math.prod(args)
#
# print(multiply(1, 2, 3, 4))
#
# # 2nd solution

# from functools import reduce
#
# multiply = lambda * args: reduce(lambda a, b: a * b, args)
#
# print(multiply(1, 2, 3, 4, 5))

from operator import mul
from functools import reduce

def multiply (*args):
    return reduce(mul, args)