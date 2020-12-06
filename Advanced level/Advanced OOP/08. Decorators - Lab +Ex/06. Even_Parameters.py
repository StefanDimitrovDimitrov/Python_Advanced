def even_parameters(fn):

    def wrapper(*args):
        list_is_correct = True
        for par in args:
            if type(par) != int and type(par) != float:
                list_is_correct = False
            elif par % 2 != 0:
                list_is_correct = False

        if list_is_correct:
            return fn(*args)
        return "Please use only even numbers!"

    return wrapper

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
